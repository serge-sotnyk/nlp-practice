#Lua 5.3 参考手册
作者 Roberto Ierusalimschy, Luiz Henrique de Figueiredo, Waldemar Celes

##1 – 简介

Lua是一门扩展式程序设计语言，它被设计成支持通用过程式编程（procedural programming），并有相关数据结构描述设施。同时，Lua也支持面向对象编程、函数式编程和数据驱动式（data-driven）编程。Lua作为一门强大的轻量的嵌入式的语言，可以被任何需要的程序使用。Lua是一个用Clean C（一个标准C和C++的子集）撰写的库。

作为一个扩展语言，Lua没有"main"函数概念，即：Lua只有被嵌入到宿主程序中才能工作。宿主程序能够调用一些函数来执行一段Lua代码，能读写Lua的变量，也能将C函数注册到Lua中以被Lua代码调用。通过对C函数的调用，Lua能够被配置而用于众多不同的领域，来创建共享语法框架的定制的编程语言。Lua的代码中包含一个名为"lua"的示例宿主程序，它使用Lua库来提供一个完整的独立的Lua解释器，可以用于交互或者批处理。

Lua是自由软件，如其许可证所述，不提供任何担保。你可以从Lua的官方网站（www.lua.org)找到本手册对应的实现。

与其它参考手册一样，本文档是极简洁的(dry in places)。你可以从我们的主页上查看相关的技术论文以了解Lua这样设计的原因和相关讨论。更详细的Lua编程指导见Roberto的书：Programming in Lua。

##2 – 基本概念

本章描述Lua的基本概念。

###2.1 – 值与类型

Lua是一门动态类型语言。这意味着只有值（value）有类型（type），而变量不具有类型。在语言中没有类型定义。所有的值都附带其类型。

所有的值都是第一等（first-class）值。这表明，任何值都可以被存储于变量，作为参数被传入函数中，及作为函数的返回值。

Lua包含8中类型，分别是*nil*、*boolean*、*number*、*string*、*function*、*userdata*、*thread* 和 *table*。*Nil*是*nil*的类型。*nil*区别于其它所有的值。它通常表示此处缺少一个有用的值。*Boolean*是value、false的类型。*nil*和*false*在条件语句中均为假，其它值均为真。*number*表示整数（integer）或浮点数（floating-point）。*string*表示不可变的字节（byte）序列。Lua是8-bit对齐的（8-bit clean），即字节串（string）可以包含任何8-bit的值，包括'\0'。Lua是编码无关的（encoding-agnostic），对字节串的内容不作任何限制。

number在实现内部使用了两个类型来表示，分别是integer和float。Lua具有一套明确的规则来决定究竟用哪个形式来表示一个number。它们之间在必要时会自动转化。因此，一般程序员不必关心Lua在内部是用integer还是float来存储某个Number值的，只有少数情况下要完全控制number的内部表示。Lua默认使用64bit的integer和float（双精度）。可以配置成使用32Bit（单精度），luaconf.h中找LUA_32BITS宏即可。

Lua可以使用Lua或者C实现的函数。这两种函数的类型都是*function*。

userdata代表一块raw内存，它可以让c数据存储在lua的变量中。userdata有两个类型，分别是1）full userdata，指一块由lua管理的内存。 2）light userdata，只是一个c指针。userdata除了assignment和identity test之外，没有其它预先定义的操作。码农可以通过metatables给full userdata定义oprations。userdata值不能够被Lua创建和修改，只能通过c API。这保证了host program数据的完整性。

thread类型表示一个执行线程，它是用来实现协程的。lua的thread与操作系统的线程没有半点关系。lua在所有系统上支持coroutine协程。

table类型实现了关联数组。这个关联数组既可以被除了nil和NaN（not a number，特殊的number，表示undefined或者unrepresentable的结果，比如0/0）之外所有的lua值所index。例如下面代码，用了function作为index key。table的值的限制是不能是nil，任何值为nil的pair将不再是table的成员。同时，不是table成员的key会返回的值为nil。

    local mytable = {}
    local key = function()begin print("hello world") end;
    mytable[key] = key
    mytable[key]()//hello world!

Table是lua中惟一的构建数据结构的方式。它可以被用来表示array、sequence、symbol table、set、record、graph、tree等。在表达records时，Lua使用field name作为table的index。在lua中，有个甜食（syntactic sugar）是a.name=a["name"]。其它还有一些方便的方式来创建和管理table。(@3.4.7)

Sequence不是array，它从1开始index到n，n是它的长度。（@3.4.7）

Table的值可以是任何类型，包括function。在table中的方法可以成为该table对象的method。

Table的索引按照raw equality来进行。只有i和j是raw equal时，a[i] ，a[j]才是同一个element。特别的对于number，类似2.0会被搞成纯integer为2。例如：a[2.0]和a[2]是同一个，但是a[2.1]和a[2]不是同一个。注意，a["2.0"] 和a[2.0]不一样。

Table，function，thread 和(full)userdata的值是objects，即，这些变量并不实际的包含value，只是reference，同时对assignment,parameter passing 和fucntion return也总是reference传递，而不是值拷贝。

库函数type()会返回value的类型描述。（@6.1)

###2.2 – 环境变量和全局环境变量

一个free name（即不被限制在任何的声明中）的变量var会被转换为_ENV.var。更具体的，任何的chunk都会在加载时注入一个名为_ENV的外在局部变量（external local variable），所以_ENV本身对于host整体来说不是free name。

尽管_ENV这个名字被用来表达一个外来的变量了，但_ENV本质上依旧是一个常规名称。我们依旧可以自己定义一个新的变量使用同样的变量名。任何时候，对某变量名的引用都遵循通用的变量可见性法则，_ENV也不例外。但通常只有没有必要覆盖_ENV变量。

加载时注入的_ENV是一个table，它表示环境变量。

Lua保持了一个特别的环境变量叫做全局环境变量。它的值保存在一个特殊的C registery中。在C中，全局变量_G也被初始化为此全局变量，但_G不在Lua的内部出现。

当Lua加载一个chunk（即代码段），_ENV这个upvalue的默认值就是那个全局变量。因此，默认的，free names都会引用到全局变量的entries（所以，这些free names也被称为全局变量）。标准库加载在全局环境变量中，同时一些函数可以操作这个全局环境变量，即标准库在_ENV中。你可以用load或者Loadfile来加载一个chunk，通过指明其环境变量来赋予其一个非全局环境变量的环境变量。（在C中，要指定某chunk的环境变量，需要在加载chunk后修改其首个upvalue。）

###2.3 – 错误处理

因为Lua是一个嵌入式扩展语言，所以Lua的执行都是从宿主程序某处C代码中调用一个Lua库函数开始的。在编译和执行一段chunk的时候，如果出现错误，Lua库将返回到宿主的C代码中，并告知错误，宿主可以处理这些错误。比如Lua standalone中，宿主发现Lua执行错误时的处理就是打印错误信息。

Lua代码可以通过调用error函数，显式地产生一个错误。如果需要在Lua代码中捕获错误，你可以使用pcall或者xpcall在保护模式下调用一个指定的函数。**TODO 什么是保护模式，pcall xpcall是怎么回事**

当错误发生了，一个error对象（也称为error消息）会携带错误信息返回到宿主中。Lua本身产生的error对象实际上只是一个string，里面包含一条描述错误的消息，而实际上Lua代码可以把任何值作为error对象。并且依赖于Lua程序或者宿主程序来处理这种特别的error对象。**TODO 实例**

当你使用xpcall或者lua_pcall时，你可以指定一个message handler。这个message handler在error出现时会被调用。这个message handler在调用时会传入原始的error对象，并且它应该返回一个新的error对象。它会在Lua展开调用栈之前被调用，因而它可以收集关于错误的更多的信息，比如收集函数调用关系（stack traceback)。这个message handler本身也是被proteceted call保护的。所以如果message handler函数自己出现了错误，会导致此message handler被再次调用。如果这导致了死循环，Lua会打破它并返回一条合适的消息。

###2.4 – 元表及元方法

Lua中的每个值都可以有一个元表。元表就是一个普通的Lua table。元表定义了原值在特定操作下的行为。你可以通过该表元表中的原方法来该表原值在特定操作时的行为。比如，当一个非Number类型的值被执行加法操作时，Lua会去检查其元表中的“__add”项，如果存在，则调用其所对应的元方法来完成此加法操作。

元表的键名是事件名，其所对应的值就是元方法。在前面的例子中，事件名为“add”，而元方法就是执行此加法的函数。

你可以通过getmetatable函数来获取某值的元表。

你可以通过setmetatable函数来设置table的元表。你不能在Lua中改变其它类型的元表，而只能在C代码中。

Table和full userdata对于每个对象都有独立的元表（虽然多个table和userdata可以共享同一个元表）。对于其它类型，各类型下的所有值都共享一个唯一的元表。在默认情况下，除了string类型外，其它类型的值是没有初始元表的。

元表控制着对象在数学操作、位操作、比较操作、连接操作、取长度操作、函数调用操作 和 indexing时的表现。同时，元表还可以定义一个在GC此对象时被调用的方法。

下面将会给出所有元表支持的操作名称。每个操作都有一个操作名。而元表的键名由两个下划线与操作名连接而成。比如“add”操作在元表中的键名是“__add”。注意，对元方法的引用永远是原始的（raw)，而不会调用其它的元方法。下面代码模拟了此过程：

     rawget(getmetatable(obj) or {}, "__" .. event_name)

对于一元操作符（取反、取长度和位非），元方法在被调用时会传入一个与首参数一致的第二个参数。这个多余的第二个参数只是为了Lua的实现方便。函数的实现代码中应该不能依赖于第二个参数，因为它可能在未来版本被移除。

"add": + 操作。只要两个操作数中，任何一个不是number类型的，Lua就会尝试调用此元方法。Lua会先检查第一个操作数是否有此元方法，如果没有，再检查第二个操作数的元方法，如果存在，Lua会以此2个操作数作为参数调用此元方法。如果均不存在此元方法，Lua会报错。
"sub": - 操作。与+类似。
"mul": * 操作。与+类似。
"div": / 操作。与+类似。
"mod": % 操作。与+类似。
"pow": ^(exponentiation 幂) 操作。与+类似。
"unm": - 取反(unary minus) 操作。与+类似。
"idiv": // (floor division) 操作。与+类似。
"band": & 按位与操作。表现与+类似。除了：当操作数不是number类型也不是一个可以强制转换为integer的值(coercible to integer @3.4.3)。//TODO
"bor": |　按位或操作，与＆类似。
"bxor": ～按位异或操作，与＆类似。
"bnot": ～按位取非操作(bitwise unary not)，与＆类似。
"shl": ＜＜按位左移操作，与＆类似。
"shr": ＞＞按位右移操作，与＆类似。
"concat":　．．连接操作。与＋类似。但是只有当Lua发现两个操作数都不是string或者number（它始终能被强制转化会string）才会尝试。 
"len": # (length) 取长度操作。当值不是一个string时，Lua会尝试此元方法。如果存在，Lua会调用此原方法并把该值作为第一个参数。如果不存在，那么如果该值是一个table，那么Lua会使用table的取长度方法（@3.4.7），否则报错。 
"eq": == 操作。与+类似。只有当两个操作数都是table或者都是full userdata并且都不是primitively equal时才会触发。结果总是被转换成boolean。 
"lt": <小于操作。与+类似。但是只有当两个操作数都不是number或者都不是string才会触发，结果会被转化成boolean。
"le": <=小于等于操作。 与其它操作都不同。小于等于操作有两个事件名。Lua会先在两个操作数中寻找“__le”元方法，如果找到，则与lt类似。如果不能找到，lua会尝试使用“__lt”，假设a <= b 与 not（b < a）是一样的。结果总是boolean。**todo**

"index": indexing access table[key]操作。当table不是table类型，或者key不在table中时触发。它的元方法可以是函数也可以是一个table。如果是函数，table 和key将作为它的参数。如果是一个table，那么结果将是对此元方法table的[key]操作的结果（而且此index是regular的，而不是raw，可能触发新的metamethod）。

"newindex": indexing assignment table[key] = value。当table变量不是一个table或者没有key时触发。与index类似，元方法既可以是函数也可以是一个table。如果是一个函数，那么table,key,value将作为参数传入。如果是一个table，那么其结果是对此元方法table的[key]=value的结果。

无论是否有“newindex”方法，Lua不会执行primitive assignment。（如果必要，可以在metamethod中调用rawset来完成）。**primitive assignment 什么鬼**

"call": call操作。当Lua尝试在非function类型的值上执行call操作时，Lua会检查此元方法。如果存在，则此元方法将被调用，并且此值将作为第一个参数传入此元方法，其它的参数将依次传入。**如果不存在，会报错**。
       myvar(args)
       getmetatable(myvar)["__call"](myvar, args)


###2.5 – 垃圾收集（GC）

Lua会自己管理好内存，所以你在创建对象和释放对象时不必担心内存的获取与释放。Lua通过一个垃圾回收器（GC）搜集死了的对象，并释放它们。所有lua使用的对象都会被GC管理。

Lua实现了一个增量的mark-and-sweep搜集器。它使用数字变量来控制垃圾回收循环：GC pause和GC step multiplier。它两都是0-100的整数。（percentage points as units）

GC pause控制GC运行的间隔时间。数值越大，那么GC就越懒惰。Pause小于100表示GC循环之间不会有停顿。如果是200，表示新循环在内存使用率为之前的2倍时才开始新的循环。

GC step multiplier控制着收集器运作速度相对于内存分配速度的倍率。 增大这个值不仅会让收集器更加积极，还会增加每个增量步骤的长度。 不要把这个值设得小于 100 ， 那样的话收集器就工作的太慢了以至于永远都干不完一个循环。 默认值是 200 ，这表示收集器以内存分配的“两倍”速工作。

如果你把step multiplier设为一个非常大的数字 （比你的程序可能用到的字节数还大 10% ）， 收集器的行为就像一个 stop-the-world 收集器。 接着你若把间歇率设为 200 ， 收集器的行为就和过去的 Lua 版本一样了： 每次 Lua 使用的内存翻倍时，就做一次完整的收集。

你可以通过在 C 中调用 lua_gc 或在 Lua 中调用 collectgarbage 来改变这俩数字。 这两个函数也可以用来直接控制收集器（例如停止它或重启它）。

####2.5.1 – 垃圾搜集元方法（cp cloudwu)

你可以为表设定垃圾收集的元方法， 对于完全用户数据（参见 §2.4）， 则需要使用 C API 。 该元方法被称为 终结器。 终结器允许你配合 Lua 的垃圾收集器做一些额外的资源管理工作 （例如关闭文件、网络或数据库连接，或是释放一些你自己的内存）。

如果要让一个对象（表或用户数据）在收集过程中进入终结流程， 你必须 标记 它需要触发终结器。 当你为一个对象设置元表时，若此刻这张元表中用一个以字符串 "__gc" 为索引的域，那么就标记了这个对象需要触发终结器。 注意：如果你给对象设置了一个没有 __gc 域的元表，之后才给元表加上这个域， 那么这个对象是没有被标记成需要触发终结器的。 然而，一旦对象被标记， 你还是可以自由的改变其元表中的 __gc 域的。

当一个被标记的对象成为了垃圾后， 垃圾收集器并不会立刻回收它。 取而代之的是，Lua 会将其置入一个链表。 在收集完成后，Lua 将遍历这个链表。 Lua 会检查每个链表中的对象的 __gc 元方法：如果是一个函数，那么就以对象为唯一参数调用它； 否则直接忽略它。

在每次垃圾收集循环的最后阶段， 本次循环中检测到的需要被回收之对象， 其终结器的触发次序按当初给对象作需要触发终结器的标记之次序的逆序进行； 这就是说，第一个被调用的终结器是程序中最后一个被标记的对象所携的那个。 每个终结器的运行可能发生在执行常规代码过程中的任意一刻。

由于被回收的对象还需要被终结器使用， 该对象（以及仅能通过它访问到的其它对象）一定会被 Lua 复活。 通常，复活是短暂的，对象所属内存会在下一个垃圾收集循环释放。 然后，若终结器又将对象保存去一些全局的地方 （例如：放在一个全局变量里），这次复活就持续生效了。 此外，如果在终结器中对一个正进入终结流程的对象再次做一次标记让它触发终结器， 只要这个对象在下个循环中依旧不可达，它的终结函数还会再调用一次。 无论是哪种情况， 对象所属内存仅在垃圾收集循环中该对象不可达且 没有被标记成需要触发终结器才会被释放。

当你关闭一个状态机（参见 lua_close）， Lua 将调用所有被标记了需要触发终结器对象的终结过程， 其次序为标记次序的逆序。 在这个过程中，任何终结器再次标记对象的行为都不会生效。

####2.5.2 – 弱表

一个弱表是一个所有元素都是弱引用的表。弱引用会被GC忽略。即，当对某对象的引用只有弱引用时，垃圾搜集器会搜集此对象。

一个弱表可以有弱的键、弱的值或者都有。一个具有弱键的表允许GC搜集它的键但不允许搜集其值。一个具有弱键和弱值的表允许GC搜集其键和表。在任何情况下，只要键值对中的一个被GC搜集了，那么这整个键值对都会从此表中被移出。一个表的弱特性由其元表的“__mode”键的值所控制。如果此键值包含'k'那么表中的键是弱的，同样的，如果包含'v'，则表的值是弱的。

一个具有弱键强值的表又被称为蜉蝣表（生命周期极短）。在一个蜉蝣表中，一个值只有当键是可达的时候才被认为是可达的。也就是说，当对key的唯一的引用来自其值时，此键值对将被移出。**注意可达性的概念**

任何对表的弱性的改变只会在下一个GC周期中生效。比如，你加强了弱性，Lua依旧会搜集一些弱的元素，直到下一次GC周期。

只有具有明确的构建行为的对象才会被GC从弱表中移除。值，比如number以及light C函数，都不是GC的处理对象，因而 它们不会被从弱表中移除，除非它们关联的键或值被搜集了。虽然string是GC的对象，但是由于它没有显式的构建过程，所以也不会被从弱表中移除。**TODO？？**

弱表针对复活的对象 （指那些正在走终结流程，仅能被终结器访问的对象） 有着特殊的行为。 弱值引用的对象，在运行它们的终结器前就被移除了， 而弱键引用的对象则要等到终结器运行完毕后，到下次收集当对象真的被释放时才被移除。 这个行为使得终结器运行时得以访问到由该对象在弱表中所关联的属性。

如果一张弱表在当次收集循环内的复活对象中， 那么在下个循环前这张表有可能未被正确地清理。

###2.6 – 协程

Lua支持协程，它也被称为协作式的多线程。Lua中的一个协程表示一个独立的执行序列。与多线程系统中的线程不同，协程只有当明确的调用yield函数时，该执行序列才会暂停。

你可以通过调用coroutine.create函数来创建一个协程。它的唯一的参数是一个函数，它将作为协程的函数体。这个创建函数只是创建了一个协程对象，但并没有运行此协程。

你可以通过coroutine.resume方法来执行某个协程。当你首次调用coroutine.resume时，第一个参数是由coroutine.create返回thread类型的值，其主函数将会从第一行开始执行，其它传入resume的参数，将作为主函数的参数。一个协程会运行，直到它结束或者调用yield才会停止。

一个协程可以通过2个方法结束它的执行。一般的，协程的主函数返回了。或者，异常的，一个不被保护的error出现了。在一般的结束时，coroutine.resume会返回true，和其它由协程主函数返回的值。在出错情况下，coroutine.resume会返回false，和一个error message。

一个协程可以调用coroutine.yield函数来让出。当一个协程让出时，对应的coroutine.resume调用会立即返回，即使yield发生在主函数直接或间接的调用的函数内。当yield时，coroutine.resume也会返回true，和coroutine.yield调用时传入的参数。当下次你resume这个协程时，它会从yield的地方继续执行，即在协程内部coroutine.yield返回了并且返回了在外部传入coroutine.resume的参数。

与coroutine.create一样，coroutien.wrap也能够创建coroutine，但它不会返回一个协程对象，而是返回一个函数对象，当它被调用，所创建的不具名的协程将被resume。此函数是对不具名的协程对象与coroutine.resume的包装，传入其的参数将作为resume的参数，resume返回的值将成为此函数的返回值。但是，此函数不会返回错误信息，即resume返回的第一个值。也就是说，此函数与coroutine.resume不同，它不会补货任何的错误，任何的错误将被扩散到它的caller。

下面是一个协程的示例：

     function foo (a)
       print("foo", a)
       return coroutine.yield(2*a)
     end
     
     co = coroutine.create(function (a,b)
           print("co-body", a, b)
           local r = foo(a+1)
           print("co-body", r)
           local r, s = coroutine.yield(a+b, a-b)
           print("co-body", r, s)
           return b, "end"
     end)
     
     print("main", coroutine.resume(co, 1, 10))
     print("main", coroutine.resume(co, "r"))
     print("main", coroutine.resume(co, "x", "y"))
     print("main", coroutine.resume(co, "x", "y"))
上面的代码运行后会输出如下内容：

     co-body 1       10
     foo     2
     main    true    4
     co-body r
     main    true    11      -9
     co-body x       y
     main    true    10      end
     main    false   cannot resume dead coroutine
你还可以通过C API来创建和操纵协程，参见：lua_newthread, lua_resume 和 lua_yield。

##3 – 语言定义

这一章描述了Lua的词法、语法和语义。

我们使用扩展的BNF范式来描述语法。例如{a}表示0或多个a，[a]表示0或1个a，非终结符以普通文本表述，关键词会加粗

本章介绍Lua的文本。

文本介绍时，我们会使用BNF范式来描述语言规则（见编译原理），例如：{a}表示0个或更多的a，[a]表示0个或1个a。 非终结符会这样写 non-terminal ， 关键字会写成这样 kword， 而其它终结符则写成这样 ‘=’ 。完整的语法见@9。

###3.1 – 语法约定

Lua是格式自由的，它忽略所有的white space和comments，只把它们作为names和keyword的分隔符。

Identifiers可有由下划线、字母和数字组成，但不能以数字开头。所有的name variable和table fields和label都是identifier。

下面这些关键词被语言保留：

     and       break     do        else      elseif    end
     false     for       function  goto      if        in
     local     nil       not       or        repeat    return
     then      true      until     while

Lua是大小写敏感的，所以and是一个保留关键字，但AND和And是合法的identifier。作为惯例，程序应该避免创建以_打头的大写字母序列作为name，比如_VERSION。

下面这些文本表示其他的一些tokens:

     +     -     *     /     %     ^     #
     &     ~     |     <<    >>    //
     ==    ~=    <=    >=    <     >     =
     (     )     {     }     [     ]     ::
     ;     :     ,     .     ..    ...

字节序列可以由单括号或者双括号来括起，同时可以包含\a，\b，\f，\n，\r，\t，\v，\\，\"，\'等。\(回车)表示一个newline。'\z'会跳过后续的white-space字符。

Lua的strings可以包含任何8-bit的值，包括\0。更普通的，我们可以用数字值来表达任何byte，可以使用\xXX或者\ddd（XX表十六进制的一个byte刚好，ddd最大到256你懂的）。注意\23是错误的，必须是\023。

UTF-8的unicode字符可以插入其中用，\u{XXX}来表示，其中XXX可以是1或多个十六进制数字。
	str = "c\u{2b}\u{2b}"
	print(str)//c++


the opening long bracket
[[string]]
[=[string]=]
[[               一个约定：这里的换行为了方便会省略
string]]

字面串中的每个不被上述规则影响的字节都呈现为本身。 然而，Lua 是用文本模式打开源文件解析的， 一些系统的文件操作函数对某些控制字符的处理可能有问题。 因此，对于非文本数据，用引号括起来并显式按转义符规则来表述更安全。

下面都是一样的：

     a = 'alo\n123"'
     a = "alo\n123\""
     a = '\97lo\10\04923"'
     a = [[alo
     123"]]
     a = [==[
     alo
     123"]==]

数字常量支持0x或者0X表示十六进制。同时e表示10的exponent，P表示二进制的exponent。

     3   345   0xff   0xBEBADA

     3.0     3.1416     314.16e-2     0.31416E1     34e1  
     0x0.1E  0xA23p-4   0X1.921FB54442D18P+1

	--short comment
	--[[ long
         comment
      ]]

###3.2 – 变量

变量是用来存放值的。Lua中有三种变量，分别是全局（global）、局部（local）和table fields。

一个单一的identifier可以表示一个局部或者全局的变量，而函数的参数，一种特殊的局部变量。

	var ::= Name

任何indentifier除非显式的指明是local，否则都是global。局部变量是限定作用范围的，局部变量只能够被定义在该scope中的function自由访问。

任何变量，在首次assignment之前的值是nil。

方括号用来index一个table。

	var ::= prefixexp ‘[’ exp ‘]’
这个过程的具体意义可以通过改变metatables来改变。

var.Name和var["Name']是一样的。

	var ::= prefixexp ‘.’ Name
对全局变量 x 的操作等价于操作 _ENV.x。 由于代码块编译的方式， _ENV 永远也不可能是一个全局名字。

###3.3 – 语句

Lua支持与pascal或者c相似的传统的语句。包括assignments，control structures, function calls和variable declarations.

####3.3.1 – 语句块(block)

一个block是一系列statement，它们顺序执行。

	block ::= {stat}
Lua有个空statements。你可以用;来分隔statements或者do ; end 或者;;.（主要就是为了让;在Lua中变得合法，而实际上他也就是为了让c程序员随便加个;也不会出错而已）

	stat ::= ‘;’

function calls和assignments都能够以（开始。这回导致一些ambiguity。如下这个例子：

     a = b + c
     (print or io.write)('done')
从语法上说，可能有如下两种解释：

     a = b + c(print or io.write)('done')
     
     a = b + c; (print or io.write)('done')
当前的解释器会采用第一种解释，即，把变量名后的小括号看成是函数调用。可以在以小括号开始的语句前面加“；”来避免这种歧义：

     ;(print or io.write)('done')
可以使用do end显式地为一个块定界：

	stat ::= do block end
通常用来控制局部变量的作用域。有时显式定块届也被用来在语句块的中间插入return，因为从语法上来讲return只能出现在一个block的尾部。

###3.3.2 – Chunk

Lua的编译单元被叫做chunk，从句法结构上讲，一个chunk也是一个block。

	chunk ::= block
Lua把chunk当做一个有参数的匿名function。所以，chunk可以像function一样，定义local variables，使用传入的参数，并且return values。此外，这种匿名的function在编译时还会为其作用域绑定入一个外部local变量_ENV。这个匿名函数总是会把_ENV作为它唯一的upvalue，即使此函数代码中没有使用_ENV，此upvalue也是存在的。

一个chunk可以被放在文件中，或者host pragram的某个string内。要执行一个chunk，你要让Lua先加载它，并将chunk的代码编译为虚拟机的机器码，然后让Lua的解释器来执行。

Chunk同样可以被编译成二进制形式，参见程序 luac 以及函数 string.dump 可获得更多细节。被编译成二进制形式的代码和原始代码是可以互相替换的。Lua能够自动的识别是编译过的还是原始代码，然后正确执行。

###3.3.3 – 赋值


Lua支持多重赋值，其语法定义为等号左边有一个变量列表，而右边有一个表达式列表：

	stat ::= varlist ‘=’ explist
	varlist ::= var {‘,’ var}
	explist ::= exp {‘,’ exp}
表达式将在@3.4中讨论。

在赋值之前，右边的值序列会被调整到与左边变量相同的个数。如果右边多了，那么多余的将被剔除。如果右边少了，那么缺少的将用nil顶替。如果右边的最后一项是函数调用，那么该函数调用将被执行，并且其所有的返回结果会被加入到右边序列中。如果function call在中间，则只取return的第一个值，如果没有return，则是nil。


	function a()
		return 11,13
    end
    function b()
    end

    x, y, z = a(),7
    print(x,y,z) //11,7,nil
    x,y,z = 7,a()
    print(x,y,z) //7,11,13
    x,y,z = b(),a()
    print(x,y,z) //nil,11,13

Assignment会先evaluate所有的表达式，之后在进行assign。
     i = 3
     i, a[i] = i+1, 20
     print(i, a[3]) // 4 20

     x, y = 12, 13
     x, y = y, x
     print(x, y) //13  12

     x, y, z = y, z, x


给全局变量和table field的assign操作可以通过修改metatables来改变语义。

对全局变量x=val的赋值，等价于_ENV.x = val；

###3.3.4 – 控制结构

逻辑控制结构包裹if,while,repeat。它们有着传统的语义:

	stat ::= while exp do block end
	stat ::= repeat block until exp
	stat ::= if exp then block {elseif exp then block} [else block] end

Lua还有2种形式的for语句。

控制结构中的条件表达式可以返回任何值。但只有false和nil是假的，其它的都是真，包括0和空string。

在repeat-until循环中，内部的Block直到Until的条件expression后才结束。也就是说condition表达式中可以使用循环block中的local variable。

Goto将代码跑到指定的label。就语法层面的原因，在lua中lebel也是一个statement:

	stat ::= goto Name
	stat ::= label
	label ::= ‘::’ Name ‘::’
一个label在整个所在定义的block内可见，包括nested block，除非nested block中定义了一样的名字。只要 goto 没有进入一个新的局部变量的作用域，它可以跳转到任意可见label。

label和空statements“；”被叫做void statements，他们不执行任何操作。

break有传统的语义，它被用来结束 while、 repeat、或 for 循环， 它将使程序跳到循环外之后的语句继续运行：

	stat ::= break
break 跳出最内层的循环。

return用来从function或者chunk（等价于匿名函数）返回values。函数可以返回多个值。
	stat ::= return [explist] [‘;’]

return只能写在一个block的最后一个语句。如果有必要在一个block的中间return回去，那么可以用nested block，比如do return xxx end等。

###3.3.5 – For 语句

for循环语句有两种不同的形式，分别是数值形式和通用形式的。

数值类型的for循环的语法：

	stat ::= for Name ‘=’ exp ‘,’ exp [‘,’ exp] do block end
就那样执行，比如：

     for v = e1, e2, e3 do block end
的意思是:

     do
       local var, limit, step = tonumber(e1), tonumber(e2), tonumber(e3)
       if not (var and limit and step) then error() end
       var = var - step
       while true do
         var = var + step
         if (step >= 0 and var > limit) or (step < 0 and var < limit) then
           break
         end
         local v = var
         block
       end
     end
注意一下几点：

3个控制表达式在循环开始前都会被计算，并且均只计算一次，而且其结果都必须是numebr。
如果numberic loop的第三个expression缺失了，那么默认的step就是1.
你可以使用break或者goto来退出一个for-loop。
loop变量v对于循环体来说是local variable。如果在循环结束后还需要它的值，那么在退出loop之前，把它付给外面变量的，否则将要丢失。
	
	for v = 1, 13, 3 do 
		print (v)
	end //1 4 7 10 13
**注意condition判断都是有>= 或者<=的。**

通用的for循环，能够工作在functions和called iterators上。

	stat ::= for namelist in explist do block end
	namelist ::= Name {‘,’ Name}
A for statement like

     for var_1, ···, var_n in explist do block end
记住下面这个语义即可：
     do
       local f, s, var = explist
       while true do
         local var_1, ···, var_n = f(s, var)
         if var_1 == nil then break end
         var = var_1
         block
       end
     end
注意以下几点：

- explist 只会被计算一次。 它返回三个值， 一个 迭代器 函数， 一个 状态， 一个 迭代器的初始值。
- f， s，与 var 都是不可见的变量。 这里给它们起的名字都只是为了解说方便。
- 你可以使用 break 来跳出 for 循环。
- 环变量 var_i 对于循环来说是一个局部变量；
- 你不可以在 for 循环结束后继续使用。
- 如果你需要保留这些值，那么就在循环跳出或结束前赋值到别的变量里去。

###3.3.6 – 函数调用语法

为了允许使用函数的副作用（Side effect），函数调用可以作为statement执行。

	stat ::= functioncall
在这个情况下，所有的返回values都会被丢弃。

###3.3.7 – 局部声明
局部变量可以再block的任何位置定义，并且可以附带一个初始的assignment。

	stat ::= local namelist [‘=’ explist]
这种用来初始化local variables的assignments和普通的multiple assignment具有一致的语义。local variable如果没有initial assignment那么它们会被初始化为nil。

chunk是block。所以local variables可以在chunk中定义。
local variables的可见性见@3.5.

##3.4 – 表达式

Lua有下面这些基本表达式：
	exp ::= prefixexp
	exp ::= nil | false | true
	exp ::= Numeral
	exp ::= LiteralString
	exp ::= functiondef
	exp ::= tableconstructor
	exp ::= ‘...’
	exp ::= exp binop exp
	exp ::= unop exp
	prefixexp ::= var | functioncall | ‘(’ exp ‘)’
数字和字面串在 §3.1 中解释； 变量在 §3.2 中解释； 函数定义在 §3.4.11 中解释； 函数调用在 §3.4.10 中解释； 表的构造在 §3.4.9 中解释。 可变参数的表达式写作三个点（'...'）， 它只能在有可变参数的函数中直接使用；这些在 §3.4.11 中解释。

二元操作符包含有数学运算操作符（参见 §3.4.1）， 位操作符（参见 §3.4.2）， 比较操作符（参见 §3.4.4）， 逻辑操作符（参见 §3.4.5）， 以及连接操作符（参见 §3.4.6）。 一元操作符包括负号（参见 §3.4.1）， 按位非（参见 §3.4.2）， 逻辑非（参见 §3.4.5）， 和取长度操作符（参见 §3.4.7）。

函数调用和可变参数表达式都可以放在多重返回值中。 如果函数调用被当作一条语句（参见 §3.3.6）， 其返回值列表被调整为零个元素，即抛弃所有的返回值。 如果表达式被用于表达式列表的最后（或是唯一的）一个元素， 那么不会做任何调整（除非表达式被括号括起来）。 在其它情况下， Lua 都会把结果调整为一个元素置入表达式列表中， 即保留第一个结果而忽略之后的所有值，或是在没有结果时， 补单个 nil。
一些多varlist的规则：

这里有一些例子：

     f()                -- 调整为0个结果
     g(f(), x)          -- f() 会被调整为1个结果
     g(x, f())          -- g 收到x与f()的所有返回值
     a,b,c = f(), x     -- f() 会被调整为1个结果（c将是nil)
     a,b = ...          -- a 收到可变参数列表的第一个参数，
                        -- b 收到第二个参数（如果可变参数列表中
                        -- 没有实际的参数，a 和 b 都会收到 nil）

     a,b,c = x, f()     -- f()的返回结果将被注入右边的序列中，右边的序列会被调整为3个结果；
     a,b,c = f()        -- f() 的返回结果会被调整为3个结果；
     return f()         -- 返回 f() 的所有返回结果
     return ...         -- 返回从可变参数列表中接收到的所有参数parameters
     return x,y,f()     -- 返回 x, y, 以及 f() 的所有返回值
     {f()}              -- 用 f() 的所有返回值创建一个列表
     {...}              -- 用可变参数中的所有值创建一个列表
     {f(), nil}         -- f() 被调整为一个结果
被括号括起来的表达式永远被当作一个值。 所以， (f(x,y,z)) 即使 f 返回多个值， 这个表达式永远是一个单一值。 （(f(x,y,z)) 的值是 f 返回的第一个值。 如果 f 不返回值的话，那么它的值就是 nil 。）

###3.4.1 – 数学运算操作符

Lua支持如下的数学运算符：

- +: 加法
- -: 减法
- *: 乘法
- /: 浮点除法
- //: 向下取整除法
- %: 取模
- ^: 幂
- -: 取负

如果两边都是integer，那么除了exponentiation和float division之外，结果都是integer。除此之外，如果两边都是number或者能够转化成number的string，那么它们都会先被转换成float，然后再进行计算，并且结果是float。
	print("3.3"/"3") //3.0

幂（^）和浮点数除法（/）总是把它们的操作数转换成float，并且结果也是float。exponentiations使用ISO C function pow，所以它也支持非integer的exponent。

//会先做浮点数除法，然后取底。

	print(11//3) //3
	print(-11//3) //-4

取模被定义成除法的余数，其商被圆整到靠近负无穷的一侧（向下取整的除法）。

对于整数数学运算的溢出问题， 这些操作采取的策略是按通常遵循的以 2 为补码的数学运算的 环绕 规则。 （换句话说，它们返回其运算的数学结果对 264 取模后的数字。）

###3.4.2 – 位操作符

lua支持如下的bitwise操作。
&: bitwise and
|: bitwise or
~: bitwise exclusive or
>>: right shift
<<: left shift
~: unary bitwise not
All bitwise operations convert its operands to integers (see §3.4.3), operate on all bits of those integers, and result in an integer.
所有的bitwise操作数都会将操作数转换为integer，作用在integer的所有Bit位上，并且结果也是一个integer。

对于右移和左移，均用零来填补空位。 移动的位数若为负，则向反方向位移； 若移动的位数的绝对值大于等于 整数本身的位数，其结果为零 （所有位都被移出）。

###3.4.3 – 强制转换

Lua对某些类型在运行时提供了一些自动的转换。位操作始终把float转换成integer。取幂和除法始终把操作数转换成float。所有的复合的操作数对，都会转换成float。同时string concatenation接受数字作为参数。

Lua也能够在预期是number的地方将字符串转换成numebr。

当把一个整数转换为浮点数时， 若整数值恰好可以表示为一个浮点数，那就取那个浮点数。 否则，转换会取最接近的较大值或较小值来表示这个数。 这种转换是不会失败的。**TODO？？**

从float到integer的转换，Lua会检查这个float是否能够转换成integer（1，是否有integer部分值 2，是否在integer的range内）。

从string到number的转化，1，string被转化成integer或者float，看具体的string内容。2，把integer或者float转化到合适的类型。

从number转化到string，使用了一个不明确的human-readable格式。如果需要严格控制number到字符串的表达，请使用format函数（string.format，见string library)。

###3.4.4 – 比较操作符
Lua支持如下的关系操作：

- ==: equality 等于
- ~=: inequality不等于
- <: less than 小于
- >: greater than 大雨
- <=: less or equal 小于等于
- >=: greater or equal 大于等于

关系操作的结果总是false或者true。
Equality（==）会先看两遍的type。如果type不同，则直接false。	
	这里注意lua对某些数值的处理比如：
	f = 2.0
	print(f==2)//true

table,userdata,以及thread以reference来做比较。两个object被认为equal只有当他们就是同一个object。每次创建的对象都是新的。具有相同reference的闭包也总是equal的。有任何差异的（包括behavior和definition）的闭包总是不同。

可以使用eq metamethod来改变lua对table userdata的比较处理。

equality比较不会将strings转变成number或者反过来。所以“0”==0为false，并且t[0]和t["0"]表示table的不同entry。

~=是就是==的取非。

大小比较操作以以下方式进行。 如果参数都是数字， 它们按二元操作的常规进行。 否则，如果两个参数都是字符串， 它们的值按当前的区域设置来比较。 再则，Lua 就试着调用 "lt" 或是 "le" 元方法 （参见 §2.4）。 a > b 的比较被转译为 b < a， a >= b 被转译为 b <= a。

###3.4.5 – 逻辑操作符

Lua有3个逻辑operator分别是and,or和not。和condition判断一样，logical operator把false 和 nil作为false其它的一切都是true。

取反操作 not 总是返回 false 或 true 中的一个。 与操作符 and 在第一个参数为 false 或 nil 时 返回这第一个参数； 否则，and 返回第二个参数。 或操作符 or 在第一个参数不为 nil 也不为 false 时， 返回这第一个参数，否则返回第二个参数。 and 和 or 都遵循短路规则； 也就是说，第二个操作数只在需要的时候去求值。 这里有一些例子：

     10 or 20            --> 10
     10 or error()       --> 10
     nil or "a"          --> "a"
     nil and 10          --> nil
     false and error()   --> false
     false and nil       --> false
     false or nil        --> nil
     10 and 20           --> 20
（在这本手册中， --> 指前面表达式的结果。）

###3.4.6 – 字节序连接

Lua的string连接操作符是“..”，如果两边都是String或者number，那么他们将先变成string，然后连接。其它情况下__concat metamethod被调用。

###3.4.7 – 取长度操作符

长度操作符是#。string的长度是byte的数目。
	a= "1234abcd"
	print(#a) //8
可以通过修改__len这个metamethod来改变#操作符的语义。
除非__len这个metamethod存在，否则table的长度只有当table是一个sequence时才存在，也就是说该table的所有正的整数key**刚好是一个{1..n}的set**。这种情况下n就是它的长度。

     {10, 20, nil, 40}
这个不是sequence，因为它有key4但没有key3. 只有Positive Integer key才会影响table的sequence与否。

###3.4.8 – 优先级

Lua 中操作符的优先级写在下表中，从低到高优先级排序：

     or
     and
     <     >     <=    >=    ~=    ==
     |
     ~
     &
     <<    >>
     ..
     +     -
     *     /     //    %
     unary operators (not   #     -     ~)
     ^
通常， 你可以用括号来改变运算次序。 **连接操作符 ('..') 和乘方操作 ('^') 是从右至左的。** 其它所有的操作都是从左至右。

###3.4.9 – 表的构建

表构造子是一个构造表的表达式。 每次构造子被执行，都会构造出一张新的表。 构造子可以被用来构造一张空表， 也可以用来构造一张表并初始化其中的一些域。 一般的构造子的语法如下

	tableconstructor ::= ‘{’ [fieldlist] ‘}’
	fieldlist ::= field {fieldsep field} [fieldsep]
	field ::= ‘[’ exp ‘]’ ‘=’ exp | Name ‘=’ exp | exp
	fieldsep ::= ‘,’ | ‘;’
每个形如 [exp1] = exp2 的域向表中增加新的一项， 其键为 exp1 而值为 exp2。 形如 name = exp 的域等价于 ["name"] = exp。 最后，形如 exp 的域等价于 [i] = exp ， 这里的 i 是一个从 1 开始不断增长的数字。 这这个格式中的其它域不会破坏其记数。 举个例子：

     a = { [f(1)] = g; "x", "y"; x = 1, f(x), [30] = 23; 45 }
等价于

     do
       local t = {}
       t[f(1)] = g
       t[1] = "x"         -- 1st exp
       t[2] = "y"         -- 2nd exp
       t.x = 1            -- t["x"] = 1
       t[3] = f(x)        -- 3rd exp
       t[30] = 23
       t[4] = 45          -- 4th exp
       a = t
     end
构造子中赋值的次序未定义。 （次序问题只会对那些键重复时的情况有影响。）

如果表单中最后一个域的形式是 exp ， 而且其表达式是一个函数调用或者是一个可变参数， 那么这个表达式所有的返回值将依次进入列表 （参见 §3.4.10）。

初始化域表可以在最后多一个分割符， 这样设计可以方便由机器生成代码。

####3.4.10 – 函数调用

function调用的语法:

	functioncall ::= prefixexp args
函数调用时， 第一步，prefixexp 和 args 先被求值。 如果 prefixexp 的值的类型是 function， 那么这个函数就被用给出的参数调用。 否则 prefixexp 的元方法 "call" 就被调用， 第一个参数是 prefixexp 的值， 接下来的是原来的调用参数 （参见 §2.4）。


有个语法糖，
	functioncall ::= prefixexp ‘:’ Name args
即：
	v:name(args)
    v.name(v,args)
两个是一样的。用它方便找“对象”。
这个形式被用来调用“对象”的成员函数（method）。


Arguments 的规则定义如下:

	args ::= ‘(’ [explist] ‘)’
	args ::= tableconstructor
	args ::= LiteralString
即：
当参数只是一个table时，可以用f{fields}来代替f({fields})。
当参数只是一个string时，可以用f'string'或者f"string"或者f[[string]]来代替f('string')


return functioncall 这样的调用形式将触发一次 尾调用。 Lua 实现了 完全尾调用（或称为 完全尾递归）： 在尾调用中， 被调用的函数重用调用它的函数的堆栈项。 因此，**对于程序执行的嵌套尾调用的层数是没有限制的。** 然而，尾调用将删除调用它的函数的任何调试信息。 注意，尾调用只发生在特定的语法下， 仅当 return 只有单一函数调用作为参数时才发生尾调用； 这种语法使得调用函数的所有结果可以完整地返回。 因此，下面这些例子都不是尾调用：

     return (f(x))        -- 返回值被调整为一个
     return 2 * f(x)
     return x, f(x)       -- 追加若干返回值
     f(x); return         -- 返回值全部被舍弃
     return x or f(x)     -- 返回值被调整为一个
####3.4.11 – function定义

Lua 中的函数调用的语法如下：

	functioncall ::= prefixexp args
函数调用时， 第一步，prefixexp 和 args 先被求值。 如果 prefixexp 的值的类型是 function， 那么这个函数就被用给出的参数调用。 否则 prefixexp 的元方法 "call" 就被调用， 第一个参数是 prefixexp 的值， 接下来的是原来的调用参数 （参见 §2.4）。

这样的形式

	functioncall ::= prefixexp ‘:’ Name args
可以用来调用 "方法"。 这是 Lua 支持的一种语法糖。 像 v:name(args) 这个样子， 被解释成 v.name(v,args)， 这里的 v 只会被求值一次。

参数的语法如下：

	args ::= ‘(’ [explist] ‘)’
	args ::= tableconstructor
	args ::= LiteralString
所有参数的表达式求值都在函数调用之前。 这样的调用形式 f{fields} 是一种语法糖用于表示 f({fields})； 这里指参数列表是一个新创建出来的列表。 而这样的形式 f'string' （或是 f"string" 亦或是 f[[string]]） 也是一种语法糖，用于表示 f('string')； 此时的参数列表是一个单独的字符串。

return functioncall 这样的调用形式将触发一次 尾调用。 Lua 实现了 完全尾调用（或称为 完全尾递归）： 在尾调用中， 被调用的函数重用调用它的函数的堆栈项。 因此，对于程序执行的嵌套尾调用的层数是没有限制的。 然而，尾调用将删除调用它的函数的任何调试信息。 注意，尾调用只发生在特定的语法下， 仅当 return 只有单一函数调用作为参数时才发生尾调用； 这种语法使得调用函数的所有结果可以完整地返回。 因此，下面这些例子都不是尾调用：

     return (f(x))        -- 返回值被调整为一个
     return 2 * f(x)
     return x, f(x)       -- 追加若干返回值
     f(x); return         -- 返回值全部被舍弃
     return x or f(x)     -- 返回值被调整为一个
####3.4.11 – 函数定义

函数定义的语法如下：

	functiondef ::= function funcbody
	funcbody ::= ‘(’ [parlist] ‘)’ block end
另外定义了一些语法糖简化函数定义的写法：

	stat ::= function funcname funcbody
	stat ::= local function Name funcbody
	funcname ::= Name {‘.’ Name} [‘:’ Name]
该语句

     function f () body end
被转译成

     f = function () body end
该语句

     function t.a.b.c.f () body end
被转译成

     t.a.b.c.f = function () body end
该语句

     local function f () body end
被转译成

     local f; f = function () body end
而不是

     local f = function () body end
（这个差别只在函数体内需要引用 f 时才有。）

一个函数定义是一个可执行的表达式， 执行结果是一个类型为 function 的值。 当 Lua 预编译一个代码块时， 代码块作为一个函数，整个函数体也就被预编译了。 那么，无论何时 Lua 执行了函数定义， 这个函数本身就进行了 实例化（或者说是 关闭了）。 这个函数的实例（或者说是 闭包）是表达式的最终值。

形参被看作是一些局部变量， 它们将由实参的值来初始化：

	parlist ::= namelist [‘,’ ‘...’] | ‘...’
当一个函数被调用， 如果函数并非一个 可变参数函数， 即在形参列表的末尾注明三个点 ('...')， 那么实参列表就会被调整到形参列表的长度。 变长参数函数不会调整实参列表； 取而代之的是，它将把所有额外的参数放在一起通过 变长参数表达式传递给函数， 其写法依旧是三个点。 这个表达式的值是一串实参值的列表， 看起来就跟一个可以返回多个结果的函数一样。 如果一个变长参数表达式放在另一个表达式中使用， 或是放在另一串表达式的中间， 那么它的返回值就会被调整为单个值。 若这个表达式放在了一系列表达式的最后一个， 就不会做调整了 （除非这最后一个参数被括号给括了起来）。

我们先做如下定义，然后再来看一个例子：

     function f(a, b) end
     function g(a, b, ...) end
     function r() return 1,2,3 end
下面看看实参到形参数以及可变长参数的映射关系：

     CALL            PARAMETERS
     
     f(3)             a=3, b=nil
     f(3, 4)          a=3, b=4
     f(3, 4, 5)       a=3, b=4
     f(r(), 10)       a=1, b=10
     f(r())           a=1, b=2
     
     g(3)             a=3, b=nil, ... -->  (nothing)
     g(3, 4)          a=3, b=4,   ... -->  (nothing)
     g(3, 4, 5, 8)    a=3, b=4,   ... -->  5  8
     g(5, r())        a=5, b=1,   ... -->  2  3
结果由 return 来返回（参见 §3.3.4）。 如果执行到函数末尾依旧没有遇到任何 return 语句， 函数就不会返回任何结果。

关于函数可返回值的数量限制和系统有关。 这个限制一定大于 1000 。

冒号 语法可以用来定义 方法， 就是说，函数可以有一个隐式的形参 self。 因此，如下语句

     function t.a.b.c:f (params) body end
是这样一种写法的语法糖

     t.a.b.c.f = function (self, params) body end
###3.5 – 变量可见性规则
除了定义为local的变量，其它变量都是全局的。
lua遵循文本层面的可见性规则。
lua的局部变量的作用域从首次申明到其所在的最内层block结束为止。


     x = 10                -- global variable
     do                    -- new block
       local x = x         -- new 'x', with value 10
       print(x)            --> 10
       x = x+1
       do                  -- another block
         local x = x+1     -- another 'x'
         print(x)          --> 12
       end
       print(x)            --> 11
     end
     print(x)              --> 10  (the global one)

注意，类似local x = x的申明，右侧的x指外部的variable而不是新的local x。


因为lua遵循lexical scoping 规则，所以local variables可以被处在该variable可见域中的function使用。一个被inner function使用的local variable称为upvalue或者external local variable。


注意闭包的特性。每次执行时，对于被function引用的upvalue都是会被重新创建的，而不是同一个。

     a = {}
     local x = 20
     for i=1,10 do
       local y = 0
       a[i] = function () y=y+1; return x+y end
     end
上面代码创建了10个闭包（closure）（即，10个匿名function)。每个闭包使用了一个不同彼此的y变量，而它们都共享同一个x变量。


##4 – 编程接口

这章描述Lua的C API。宿主程序可以通过这些C API与Lua通讯。所有的API 函数及相关的类型与常量都在lua.h中声明。

虽然我们使用“函数”来称呼这些API，但是部分特性实际上是通过宏来提供的。除非特别指出的，所有这些宏仅使用其参数一次（除了第一个Lua state参数外），所以它们不会产生任何的副作用。

与常见的C函数库一样，Lua API函数不会检查其参数的有效性和一致性。但是，你可以通过定义LUA_USE_APICHECK打开参数检查。

4.1 – 栈

Lua使用一个虚拟栈来与C互传值。这个栈中的所有元素都是Lua值（包括nil,number,string等）。

无论何时，当Lua调用C时，被调用的函数都会获得一个新的栈。这个栈与之前获得过的栈，或仍旧在活动的栈均保持独立。这个传入C函数的栈包含着所有来自Lua的参数，并且C函数会把要返回的结果放入栈中来返回给调用者（见lua_CFunction)。

为了方便，API中的大部分查询操作并不严格遵循通常的栈操作。而是，它们可以通过索引来引用任何栈中的值。一个正的索引表示栈中的一个绝对位置（从1开始）。一个负的索引表示一个与栈顶相对的位置。更具体的，如果栈中有n个元素，那么索引1和-n都表示第一个元素（位于栈底的元素），而索引n和-1则表示最后一个元素（位于栈顶的元素）。

4.2 – 栈的大小

当你使用Lua API时，你有义务保证其一致性，包括对栈溢出的处理。你可以通过函数lua_checkstack来保证栈有足够的空间存放更多的元素。

当Lua调用一个C函数时，它会保证栈中有至少LUA_MINSTACK的可用位置。LUA_MINSTACK被定义为20，所以一般而言我们不需要担心栈溢出，除非你的代码会循环的填充栈（有循环往往意味着可能有大量元素）。

当你调用一个 Lua 函数却没有指定要接收多少个返回值时 （见 lua_call）， Lua 可以保证栈一定有足够的空间来接收所有的返回值， 但不保证此外留有额外的空间。 因此，在做了一次这样的调用后，如果你需要继续压栈， 则需要使用 lua_checkstack。


4.3 – 有效索引与可接受索引

API中接受索引的函数均只接受有效索引或者可接受索引。

有效索引能够引用栈中的一个实际位置。它位于1和栈顶之间（即：1<=abs(index)<=top）。通常，函数可以修改有效索引指向的元素。

除非特别指出，否则任何接受有效索引的函数也接受伪索引。伪索引指向能够被C代码访问但又不在栈中的值。伪索引被用来访问注册表和C函数的上值（见@4.4）。

如果函数不需要一个栈中的位置，而只需要一个栈中的元素（比如，所有查询函数），那么它就可以使用可接受索引。有效索引和伪索引都是可接受索引，但可接受索引还包括指向在栈分配空间内栈顶上方的正索引，即在栈大小内的索引。（注意，0不是一个可接受索引。）除非明确指出，否者API函数均接受可接受索引。

可接受索引避免了在查询栈元素时对栈顶的额外检查。比如，一个C函数可以查询其第三个参数但不需要事先检查它是否存在，即，不需要检查3是否是一个有效索引。

凡是接受可接受索引的函数，一个对“无效”索引的查询会返回一个虚拟的类型LUA_TNONE，它的行为和nil值相似。

4.4 – C闭包

在创建一个C函数时，我们可以额外得绑定一些值给它。我们把这样的C函数叫做C闭包（见 lua_pushcclosure)。这些被绑定的值叫做上值，它们可以在任何时候被此函数访问。

当一个C函数被调用时，它的上值会被置放在特定的伪索引中。这些伪索引可以由lua_upvalueindex产生。例如，第一个被绑定到此函数的上值位于索引lua_upvalueindex(1)。当n大于当前函数上值数量时，任何对lua_upvalueindex(n)的访问都会产生一个“可接受的无效”索引。


4.5 – 注册表

Lua提供了一个注册表。它是一个被预先定义的表，C代码可以存放任何Lua值在其中。注册表永远都位于伪索引LUA_REGISTRYINDEX，并且是一个有效索引。任何C函数库都可以向其中存放数据，但是，为了防止冲突，它需要取一个与已存在的不同的键名。通常，你应该使用一个包含库名的字节串，或者一个包含要存储的C对象地址的light-userdata，或者一个由代码生成的Lua对象。Lua保留以下划线开头跟着2个大写字母的字符串键名。

注册表中Integer类型的键被用来处理reference机制（见luaL_ref）和其它预定义值。所以，不要把它用于其它目的。

当创建一个新的Lua State时，它的注册表中就会有一些预定义的值。这些预定义的值通过integer类型的常量来引用，它们定义在lua.h中。它们是：
- LUA_RIDX_MAINTHREAD：指向state的主thread。（一个主thread与state同时被创建）。**TODO 无法理解**
- LUA_RIDX_GLOBALS：指向global environment。

4.6 – C中的错误处理

在内部，Lua使用C的longjmp来处理errors。（如果把Lua按C++编译，Lua会使用异常机制。见LUAI_THROW。）当Lua遇到一个错误（比如内存分配错误，类型错误，语法错误，以及运行时错误），它会产生一个error，即它会执行一个long jump。一个保护环境会使用setjmp来设置一个恢复点（recover point），所有error都会跳转到最近的恢复点。

如果error在保护环境之外发生，那么Lua会调用一个奔溃函数（panic function @lua_atpanic）并调用abort，从而推出宿主程序。你的奔溃函数可以不返回而拒绝退出程序（比如执行一个long jump到位于Lua外的恢复点）。

奔溃函数类似一个message handler（见2.3）。特别的是，error message位于栈顶。然而栈的空间没有任何保障。要放入到栈中，奔溃函数必须先检查栈的空间。（见4.2）

大部分API函数会引发error，比如由于内存分配错误等。每个函数的文档都标注了它们可能的错误。

在C函数中，我们可以调用lua_error来故意引发一个error。

4.7 – 在C中让出

**十分抽象**引用自cloudwu

Lua 内部使用 C 的 longjmp 机制让出一个协程。 因此，如果一个 C 函数 foo 调用了一个 API 函数， 而这个 API 函数让出了（直接或间接调用了让出函数）。 由于 longjmp 会移除 C 栈的栈帧， Lua 就无法返回到 foo 里了。

为了回避这类问题， 碰到 API 调用中调用让出时，除了那些抛出错误的 API 外，还提供了三个函数： lua_yieldk， lua_callk，和 lua_pcallk 。 它们在让出发生时，可以从传入的 延续函数 （名为 k 的参数）继续运行。

我们需要预设一些术语来解释延续点。 对于从 Lua 中调用的 C 函数，我们称之为 原函数。 从这个原函数中调用的上面所述的三个 C API 函数我们称之为 被调函数。 被调函数可以使当前线程让出。 （让出发生在被调函数是 lua_yieldk， 或传入 lua_callk 或 lua_pcallk 的函数调用了让出时。）

假设正在运行的线程在执行被调函数时让出。 当再次延续这条线程，它希望继续被调函数的运行。 然而，被调函数不可能返回到原函数中。 这是因为之前的让出操作破坏了 C 栈的栈帧。 作为替代品，Lua 调用那个作为被调函数参数给出的 延续函数 。 正如其名，延续函数将延续原函数的任务。

下面的函数会做一个说明：

     int original_function (lua_State *L) {
       ...     /* code 1 */
       status = lua_pcall(L, n, m, h);  /* calls Lua */
       ...     /* code 2 */
     }
现在我们想允许被 lua_pcall 运行的 Lua 代码让出。 首先，我们把函数改写成这个样子：

     int k (lua_State *L, int status, lua_KContext ctx) {
       ...  /* code 2 */
     }
     
     int original_function (lua_State *L) {
       ...     /* code 1 */
       return k(L, lua_pcall(L, n, m, h), ctx);
     }
上面的代码中，新函数 k 就是一个 延续函数 （函数类型为 lua_KFunction）。 它的工作就是原函数中调用 lua_pcall 之后做的那些事情。 现在我们必须通知 Lua 说，你必须在被 lua_pcall 执行的 Lua 代码发生过中断（错误或让出）后， 还得继续调用 k 。 所以我们还得继续改写这段代码，把 lua_pcall 替换成 lua_pcallk：

     int original_function (lua_State *L) {
       ...     /* code 1 */
       return k(L, lua_pcallk(L, n, m, h, ctx2, k), ctx1);
     }
注意这里那个额外的显式的对延续函数的调用： Lua 仅在需要时，这可能是由错误导致的也可能是发生了让出而需要继续运行，才会调用延续函数。 如果没有发生过任何让出，调用的函数正常返回， 那么 lua_pcallk （以及 lua_callk）也会正常返回。 （当然，这个例子中你也可以不在之后调用延续函数， 而是在原函数的调用后直接写上需要做的工作。）

除了 Lua 状态，延续函数还有两个参数： 一个是调用最后的状态码，另一个一开始由 lua_pcallk 传入的上下文 （ctx）。 （Lua 本身不使用这个值；它仅仅从原函数转发这个值给延续函数。） 对于 lua_pcallk 而言， 状态码和 lua_pcallk 本应返回值相同，区别仅在于发生过让出后才执行完时，状态码为 LUA_YIELD（而不是 LUA_OK）。 对于 lua_yieldk 和 lua_callk 而言， 调用延续函数传入的状态码一定是 LUA_YIELD。 （对这两个函数，Lua 不会因任何错误而调用延续函数。 因为它们并不处理错误。） 同样，当你使用 lua_callk 时， 你应该用 LUA_OK 作为状态码来调用延续函数。 （对于 lua_yieldk， 几乎没有什么地方需要直接调用延续函数， 因为 lua_yieldk 本身并不会返回。）

Lua 会把延续函数看作原函数。 延续函数将接收到和原函数相同的 Lua 栈，其接收到的 lua 状态也和 被调函数若返回后应该有的状态一致。 （例如， lua_callk 调用之后， 栈中之前压入的函数和调用参数都被调用产生的返回值所替代。） 这时也有相同的上值。 等到它返回的时候，Lua 会将其看待成原函数的返回去操作。

4.8 – API函数和类型
**以下C API及标准库 不再翻译**

Here we list all functions and types from the C API in alphabetical order. Each function has an indicator like this: [-o, +p, x]

The first field, o, is how many elements the function pops from the stack. The second field, p, is how many elements the function pushes onto the stack. (Any function always pushes its results after popping its arguments.) A field in the form x|y means the function can push (or pop) x or y elements, depending on the situation; an interrogation mark '?' means that we cannot know how many elements the function pops/pushes by looking only at its arguments (e.g., they may depend on what is on the stack). The third field, x, tells whether the function may raise errors: '-' means the function never raises any error; 'e' means the function may raise errors; 'v' means the function may raise an error on purpose.

lua_absindex

[-0, +0, –]
int lua_absindex (lua_State *L, int idx);
Converts the acceptable index idx into an absolute index (that is, one that does not depend on the stack top).

lua_Alloc

typedef void * (*lua_Alloc) (void *ud,
                             void *ptr,
                             size_t osize,
                             size_t nsize);
The type of the memory-allocation function used by Lua states. The allocator function must provide a functionality similar to realloc, but not exactly the same. Its arguments are ud, an opaque pointer passed to lua_newstate; ptr, a pointer to the block being allocated/reallocated/freed; osize, the original size of the block or some code about what is being allocated; and nsize, the new size of the block.

When ptr is not NULL, osize is the size of the block pointed by ptr, that is, the size given when it was allocated or reallocated.

When ptr is NULL, osize encodes the kind of object that Lua is allocating. osize is any of LUA_TSTRING, LUA_TTABLE, LUA_TFUNCTION, LUA_TUSERDATA, or LUA_TTHREAD when (and only when) Lua is creating a new object of that type. When osize is some other value, Lua is allocating memory for something else.

Lua assumes the following behavior from the allocator function:

When nsize is zero, the allocator must behave like free and return NULL.

When nsize is not zero, the allocator must behave like realloc. The allocator returns NULL if and only if it cannot fulfill the request. Lua assumes that the allocator never fails when osize >= nsize.

Here is a simple implementation for the allocator function. It is used in the auxiliary library by luaL_newstate.

     static void *l_alloc (void *ud, void *ptr, size_t osize,
                                                size_t nsize) {
       (void)ud;  (void)osize;  /* not used */
       if (nsize == 0) {
         free(ptr);
         return NULL;
       }
       else
         return realloc(ptr, nsize);
     }
Note that Standard C ensures that free(NULL) has no effect and that realloc(NULL,size) is equivalent to malloc(size). This code assumes that realloc does not fail when shrinking a block. (Although Standard C does not ensure this behavior, it seems to be a safe assumption.)

lua_arith

[-(2|1), +1, e]
void lua_arith (lua_State *L, int op);
Performs an arithmetic or bitwise operation over the two values (or one, in the case of negations) at the top of the stack, with the value at the top being the second operand, pops these values, and pushes the result of the operation. The function follows the semantics of the corresponding Lua operator (that is, it may call metamethods).

The value of op must be one of the following constants:

LUA_OPADD: performs addition (+)
LUA_OPSUB: performs subtraction (-)
LUA_OPMUL: performs multiplication (*)
LUA_OPDIV: performs float division (/)
LUA_OPIDIV: performs floor division (//)
LUA_OPMOD: performs modulo (%)
LUA_OPPOW: performs exponentiation (^)
LUA_OPUNM: performs mathematical negation (unary -)
LUA_OPBNOT: performs bitwise negation (~)
LUA_OPBAND: performs bitwise and (&)
LUA_OPBOR: performs bitwise or (|)
LUA_OPBXOR: performs bitwise exclusive or (~)
LUA_OPSHL: performs left shift (<<)
LUA_OPSHR: performs right shift (>>)
lua_atpanic

[-0, +0, –]
lua_CFunction lua_atpanic (lua_State *L, lua_CFunction panicf);
Sets a new panic function and returns the old one (see §4.6).

lua_call

[-(nargs+1), +nresults, e]
void lua_call (lua_State *L, int nargs, int nresults);
Calls a function.

To call a function you must use the following protocol: first, the function to be called is pushed onto the stack; then, the arguments to the function are pushed in direct order; that is, the first argument is pushed first. Finally you call lua_call; nargs is the number of arguments that you pushed onto the stack. All arguments and the function value are popped from the stack when the function is called. The function results are pushed onto the stack when the function returns. The number of results is adjusted to nresults, unless nresults is LUA_MULTRET. In this case, all results from the function are pushed. Lua takes care that the returned values fit into the stack space. The function results are pushed onto the stack in direct order (the first result is pushed first), so that after the call the last result is on the top of the stack.

Any error inside the called function is propagated upwards (with a longjmp).

The following example shows how the host program can do the equivalent to this Lua code:

     a = f("how", t.x, 14)
Here it is in C:

     lua_getglobal(L, "f");                  /* function to be called */
     lua_pushliteral(L, "how");                       /* 1st argument */
     lua_getglobal(L, "t");                    /* table to be indexed */
     lua_getfield(L, -1, "x");        /* push result of t.x (2nd arg) */
     lua_remove(L, -2);                  /* remove 't' from the stack */
     lua_pushinteger(L, 14);                          /* 3rd argument */
     lua_call(L, 3, 1);     /* call 'f' with 3 arguments and 1 result */
     lua_setglobal(L, "a");                         /* set global 'a' */
Note that the code above is balanced: at its end, the stack is back to its original configuration. This is considered good programming practice.

lua_callk

[-(nargs + 1), +nresults, e]
void lua_callk (lua_State *L,
                int nargs,
                int nresults,
                lua_KContext ctx,
                lua_KFunction k);
This function behaves exactly like lua_call, but allows the called function to yield (see §4.7).

lua_CFunction

typedef int (*lua_CFunction) (lua_State *L);
Type for C functions.

In order to communicate properly with Lua, a C function must use the following protocol, which defines the way parameters and results are passed: a C function receives its arguments from Lua in its stack in direct order (the first argument is pushed first). So, when the function starts, lua_gettop(L) returns the number of arguments received by the function. The first argument (if any) is at index 1 and its last argument is at index lua_gettop(L). To return values to Lua, a C function just pushes them onto the stack, in direct order (the first result is pushed first), and returns the number of results. Any other value in the stack below the results will be properly discarded by Lua. Like a Lua function, a C function called by Lua can also return many results.

As an example, the following function receives a variable number of numerical arguments and returns their average and their sum:

     static int foo (lua_State *L) {
       int n = lua_gettop(L);    /* number of arguments */
       lua_Number sum = 0.0;
       int i;
       for (i = 1; i <= n; i++) {
         if (!lua_isnumber(L, i)) {
           lua_pushliteral(L, "incorrect argument");
           lua_error(L);
         }
         sum += lua_tonumber(L, i);
       }
       lua_pushnumber(L, sum/n);        /* first result */
       lua_pushnumber(L, sum);         /* second result */
       return 2;                   /* number of results */
     }
lua_checkstack

[-0, +0, –]
int lua_checkstack (lua_State *L, int n);
Ensures that the stack has space for at least n extra slots. It returns false if it cannot fulfill the request, either because it would cause the stack to be larger than a fixed maximum size (typically at least several thousand elements) or because it cannot allocate memory for the extra space. This function never shrinks the stack; if the stack is already larger than the new size, it is left unchanged.

lua_close

[-0, +0, –]
void lua_close (lua_State *L);
Destroys all objects in the given Lua state (calling the corresponding garbage-collection metamethods, if any) and frees all dynamic memory used by this state. On several platforms, you may not need to call this function, because all resources are naturally released when the host program ends. On the other hand, long-running programs that create multiple states, such as daemons or web servers, will probably need to close states as soon as they are not needed.

lua_compare

[-0, +0, e]
int lua_compare (lua_State *L, int index1, int index2, int op);
Compares two Lua values. Returns 1 if the value at index index1 satisfies op when compared with the value at index index2, following the semantics of the corresponding Lua operator (that is, it may call metamethods). Otherwise returns 0. Also returns 0 if any of the indices is not valid.

The value of op must be one of the following constants:

LUA_OPEQ: compares for equality (==)
LUA_OPLT: compares for less than (<)
LUA_OPLE: compares for less or equal (<=)
lua_concat

[-n, +1, e]
void lua_concat (lua_State *L, int n);
Concatenates the n values at the top of the stack, pops them, and leaves the result at the top. If n is 1, the result is the single value on the stack (that is, the function does nothing); if n is 0, the result is the empty string. Concatenation is performed following the usual semantics of Lua (see §3.4.6).

lua_copy

[-0, +0, –]
void lua_copy (lua_State *L, int fromidx, int toidx);
Copies the element at index fromidx into the valid index toidx, replacing the value at that position. Values at other positions are not affected.

lua_createtable

[-0, +1, e]
void lua_createtable (lua_State *L, int narr, int nrec);
Creates a new empty table and pushes it onto the stack. Parameter narr is a hint for how many elements the table will have as a sequence; parameter nrec is a hint for how many other elements the table will have. Lua may use these hints to preallocate memory for the new table. This pre-allocation is useful for performance when you know in advance how many elements the table will have. Otherwise you can use the function lua_newtable.

lua_dump

[-0, +0, e]
int lua_dump (lua_State *L,
                        lua_Writer writer,
                        void *data,
                        int strip);
Dumps a function as a binary chunk. Receives a Lua function on the top of the stack and produces a binary chunk that, if loaded again, results in a function equivalent to the one dumped. As it produces parts of the chunk, lua_dump calls function writer (see lua_Writer) with the given data to write them.

If strip is true, the binary representation is created without debug information about the function.

The value returned is the error code returned by the last call to the writer; 0 means no errors.

This function does not pop the Lua function from the stack.

lua_error

[-1, +0, v]
int lua_error (lua_State *L);
Generates a Lua error, using the value at the top of the stack as the error object. This function does a long jump, and therefore never returns (see luaL_error).

lua_gc

[-0, +0, e]
int lua_gc (lua_State *L, int what, int data);
Controls the garbage collector.

This function performs several tasks, according to the value of the parameter what:

LUA_GCSTOP: stops the garbage collector.
LUA_GCRESTART: restarts the garbage collector.
LUA_GCCOLLECT: performs a full garbage-collection cycle.
LUA_GCCOUNT: returns the current amount of memory (in Kbytes) in use by Lua.
LUA_GCCOUNTB: returns the remainder of dividing the current amount of bytes of memory in use by Lua by 1024.
LUA_GCSTEP: performs an incremental step of garbage collection.
LUA_GCSETPAUSE: sets data as the new value for the pause of the collector (see §2.5) and returns the previous value of the pause.
LUA_GCSETSTEPMUL: sets data as the new value for the step multiplier of the collector (see §2.5) and returns the previous value of the step multiplier.
LUA_GCISRUNNING: returns a boolean that tells whether the collector is running (i.e., not stopped).
For more details about these options, see collectgarbage.

lua_getallocf

[-0, +0, –]
lua_Alloc lua_getallocf (lua_State *L, void **ud);
Returns the memory-allocation function of a given state. If ud is not NULL, Lua stores in *ud the opaque pointer given when the memory-allocator function was set.

lua_getfield

[-0, +1, e]
int lua_getfield (lua_State *L, int index, const char *k);
Pushes onto the stack the value t[k], where t is the value at the given index. As in Lua, this function may trigger a metamethod for the "index" event (see §2.4).

Returns the type of the pushed value.

lua_getextraspace

[-0, +0, –]
void *lua_getextraspace (lua_State *L);
Returns a pointer to a raw memory area associated with the given Lua state. The application can use this area for any purpose; Lua does not use it for anything.

Each new thread has this area initialized with a copy of the area of the main thread.

By default, this area has the size of a pointer to void, but you can recompile Lua with a different size for this area. (See LUA_EXTRASPACE in luaconf.h.)

lua_getglobal

[-0, +1, e]
int lua_getglobal (lua_State *L, const char *name);
Pushes onto the stack the value of the global name. Returns the type of that value.

lua_geti

[-0, +1, e]
int lua_geti (lua_State *L, int index, lua_Integer i);
Pushes onto the stack the value t[i], where t is the value at the given index. As in Lua, this function may trigger a metamethod for the "index" event (see §2.4).

Returns the type of the pushed value.

lua_getmetatable

[-0, +(0|1), –]
int lua_getmetatable (lua_State *L, int index);
If the value at the given index has a metatable, the function pushes that metatable onto the stack and returns 1. Otherwise, the function returns 0 and pushes nothing on the stack.

lua_gettable

[-1, +1, e]
int lua_gettable (lua_State *L, int index);
Pushes onto the stack the value t[k], where t is the value at the given index and k is the value at the top of the stack.

This function pops the key from the stack, pushing the resulting value in its place. As in Lua, this function may trigger a metamethod for the "index" event (see §2.4).

Returns the type of the pushed value.

lua_gettop

[-0, +0, –]
int lua_gettop (lua_State *L);
Returns the index of the top element in the stack. Because indices start at 1, this result is equal to the number of elements in the stack; in particular, 0 means an empty stack.

lua_getuservalue

[-0, +1, –]
int lua_getuservalue (lua_State *L, int index);
Pushes onto the stack the Lua value associated with the userdata at the given index.

Returns the type of the pushed value.

lua_insert

[-1, +1, –]
void lua_insert (lua_State *L, int index);
Moves the top element into the given valid index, shifting up the elements above this index to open space. This function cannot be called with a pseudo-index, because a pseudo-index is not an actual stack position.

lua_Integer

typedef ... lua_Integer;
The type of integers in Lua.

By default this type is long long, (usually a 64-bit two-complement integer), but that can be changed to long or int (usually a 32-bit two-complement integer). (See LUA_INT in luaconf.h.)

Lua also defines the constants LUA_MININTEGER and LUA_MAXINTEGER, with the minimum and the maximum values that fit in this type.

lua_isboolean

[-0, +0, –]
int lua_isboolean (lua_State *L, int index);
Returns 1 if the value at the given index is a boolean, and 0 otherwise.

lua_iscfunction

[-0, +0, –]
int lua_iscfunction (lua_State *L, int index);
Returns 1 if the value at the given index is a C function, and 0 otherwise.

lua_isfunction

[-0, +0, –]
int lua_isfunction (lua_State *L, int index);
Returns 1 if the value at the given index is a function (either C or Lua), and 0 otherwise.

lua_isinteger

[-0, +0, –]
int lua_isinteger (lua_State *L, int index);
Returns 1 if the value at the given index is an integer (that is, the value is a number and is represented as an integer), and 0 otherwise.

lua_islightuserdata

[-0, +0, –]
int lua_islightuserdata (lua_State *L, int index);
Returns 1 if the value at the given index is a light userdata, and 0 otherwise.

lua_isnil

[-0, +0, –]
int lua_isnil (lua_State *L, int index);
Returns 1 if the value at the given index is nil, and 0 otherwise.

lua_isnone

[-0, +0, –]
int lua_isnone (lua_State *L, int index);
Returns 1 if the given index is not valid, and 0 otherwise.

lua_isnoneornil

[-0, +0, –]
int lua_isnoneornil (lua_State *L, int index);
Returns 1 if the given index is not valid or if the value at this index is nil, and 0 otherwise.

lua_isnumber

[-0, +0, –]
int lua_isnumber (lua_State *L, int index);
Returns 1 if the value at the given index is a number or a string convertible to a number, and 0 otherwise.

lua_isstring

[-0, +0, –]
int lua_isstring (lua_State *L, int index);
Returns 1 if the value at the given index is a string or a number (which is always convertible to a string), and 0 otherwise.

lua_istable

[-0, +0, –]
int lua_istable (lua_State *L, int index);
Returns 1 if the value at the given index is a table, and 0 otherwise.

lua_isthread

[-0, +0, –]
int lua_isthread (lua_State *L, int index);
Returns 1 if the value at the given index is a thread, and 0 otherwise.

lua_isuserdata

[-0, +0, –]
int lua_isuserdata (lua_State *L, int index);
Returns 1 if the value at the given index is a userdata (either full or light), and 0 otherwise.

lua_isyieldable

[-0, +0, –]
int lua_isyieldable (lua_State *L);
Returns 1 if the given coroutine can yield, and 0 otherwise.

lua_KContext

typedef ... lua_KContext;
The type for continuation-function contexts. It must be a numerical type. This type is defined as intptr_t when intptr_t is available, so that it can store pointers too. Otherwise, it is defined as ptrdiff_t.

lua_KFunction

typedef int (*lua_KFunction) (lua_State *L, int status, lua_KContext ctx);
Type for continuation functions (see §4.7).

lua_len

[-0, +1, e]
void lua_len (lua_State *L, int index);
Returns the length of the value at the given index. It is equivalent to the '#' operator in Lua (see §3.4.7) and may trigger a metamethod for the "length" event (see §2.4). The result is pushed on the stack.

lua_load

[-0, +1, –]
int lua_load (lua_State *L,
              lua_Reader reader,
              void *data,
              const char *chunkname,
              const char *mode);
Loads a Lua chunk without running it. If there are no errors, lua_load pushes the compiled chunk as a Lua function on top of the stack. Otherwise, it pushes an error message.

The return values of lua_load are:

LUA_OK: no errors;
LUA_ERRSYNTAX: syntax error during precompilation;
LUA_ERRMEM: memory allocation error;
LUA_ERRGCMM: error while running a __gc metamethod. (This error has no relation with the chunk being loaded. It is generated by the garbage collector.)
The lua_load function uses a user-supplied reader function to read the chunk (see lua_Reader). The data argument is an opaque value passed to the reader function.

The chunkname argument gives a name to the chunk, which is used for error messages and in debug information (see §4.9).

lua_load automatically detects whether the chunk is text or binary and loads it accordingly (see program luac). The string mode works as in function load, with the addition that a NULL value is equivalent to the string "bt".

lua_load uses the stack internally, so the reader function must always leave the stack unmodified when returning.

If the resulting function has upvalues, its first upvalue is set to the value of the global environment stored at index LUA_RIDX_GLOBALS in the registry (see §4.5). When loading main chunks, this upvalue will be the _ENV variable (see §2.2). Other upvalues are initialized with nil.

lua_newstate

[-0, +0, –]
lua_State *lua_newstate (lua_Alloc f, void *ud);
Creates a new thread running in a new, independent state. Returns NULL if it cannot create the thread or the state (due to lack of memory). The argument f is the allocator function; Lua does all memory allocation for this state through this function. The second argument, ud, is an opaque pointer that Lua passes to the allocator in every call.

lua_newtable

[-0, +1, e]
void lua_newtable (lua_State *L);
Creates a new empty table and pushes it onto the stack. It is equivalent to lua_createtable(L, 0, 0).

lua_newthread

[-0, +1, e]
lua_State *lua_newthread (lua_State *L);
Creates a new thread, pushes it on the stack, and returns a pointer to a lua_State that represents this new thread. The new thread returned by this function shares with the original thread its global environment, but has an independent execution stack.

There is no explicit function to close or to destroy a thread. Threads are subject to garbage collection, like any Lua object.

lua_newuserdata

[-0, +1, e]
void *lua_newuserdata (lua_State *L, size_t size);
This function allocates a new block of memory with the given size, pushes onto the stack a new full userdata with the block address, and returns this address. The host program can freely use this memory.

lua_next

[-1, +(2|0), e]
int lua_next (lua_State *L, int index);
Pops a key from the stack, and pushes a key–value pair from the table at the given index (the "next" pair after the given key). If there are no more elements in the table, then lua_next returns 0 (and pushes nothing).

A typical traversal looks like this:

     /* table is in the stack at index 't' */
     lua_pushnil(L);  /* first key */
     while (lua_next(L, t) != 0) {
       /* uses 'key' (at index -2) and 'value' (at index -1) */
       printf("%s - %s\n",
              lua_typename(L, lua_type(L, -2)),
              lua_typename(L, lua_type(L, -1)));
       /* removes 'value'; keeps 'key' for next iteration */
       lua_pop(L, 1);
     }
While traversing a table, do not call lua_tolstring directly on a key, unless you know that the key is actually a string. Recall that lua_tolstring may change the value at the given index; this confuses the next call to lua_next.

See function next for the caveats of modifying the table during its traversal.

lua_Number

typedef double lua_Number;
The type of floats in Lua.

By default this type is double, but that can be changed to a single float. (See LUA_REAL in luaconf.h.)

lua_numbertointeger

int lua_numbertointeger (lua_Number n, lua_Integer *p);
Converts a Lua float to a Lua integer. This macro assumes that n has an integral value. If that value is within the range of Lua integers, it is converted to an integer and assigned to *p. The macro results in a boolean indicating whether the conversion was successful. (Note that this range test can be tricky to do correctly without this macro, due to roundings.)

This macro may evaluate its arguments more than once.

lua_pcall

[-(nargs + 1), +(nresults|1), –]
int lua_pcall (lua_State *L, int nargs, int nresults, int msgh);
Calls a function in protected mode.

Both nargs and nresults have the same meaning as in lua_call. If there are no errors during the call, lua_pcall behaves exactly like lua_call. However, if there is any error, lua_pcall catches it, pushes a single value on the stack (the error message), and returns an error code. Like lua_call, lua_pcall always removes the function and its arguments from the stack.

If msgh is 0, then the error message returned on the stack is exactly the original error message. Otherwise, msgh is the stack index of a message handler. (In the current implementation, this index cannot be a pseudo-index.) In case of runtime errors, this function will be called with the error message and its return value will be the message returned on the stack by lua_pcall.

Typically, the message handler is used to add more debug information to the error message, such as a stack traceback. Such information cannot be gathered after the return of lua_pcall, since by then the stack has unwound.

The lua_pcall function returns one of the following constants (defined in lua.h):

LUA_OK (0): success.
LUA_ERRRUN: a runtime error.
LUA_ERRMEM: memory allocation error. For such errors, Lua does not call the message handler.
LUA_ERRERR: error while running the message handler.
LUA_ERRGCMM: error while running a __gc metamethod. (This error typically has no relation with the function being called.)
lua_pcallk

[-(nargs + 1), +(nresults|1), –]
int lua_pcallk (lua_State *L,
                int nargs,
                int nresults,
                int msgh,
                lua_KContext ctx,
                lua_KFunction k);
This function behaves exactly like lua_pcall, but allows the called function to yield (see §4.7).

lua_pop

[-n, +0, –]
void lua_pop (lua_State *L, int n);
Pops n elements from the stack.

lua_pushboolean

[-0, +1, –]
void lua_pushboolean (lua_State *L, int b);
Pushes a boolean value with value b onto the stack.

lua_pushcclosure

[-n, +1, e]
void lua_pushcclosure (lua_State *L, lua_CFunction fn, int n);
Pushes a new C closure onto the stack.

When a C function is created, it is possible to associate some values with it, thus creating a C closure (see §4.4); these values are then accessible to the function whenever it is called. To associate values with a C function, first these values must be pushed onto the stack (when there are multiple values, the first value is pushed first). Then lua_pushcclosure is called to create and push the C function onto the stack, with the argument n telling how many values will be associated with the function. lua_pushcclosure also pops these values from the stack.

The maximum value for n is 255.

When n is zero, this function creates a light C function, which is just a pointer to the C function. In that case, it never raises a memory error.

lua_pushcfunction

[-0, +1, –]
void lua_pushcfunction (lua_State *L, lua_CFunction f);
Pushes a C function onto the stack. This function receives a pointer to a C function and pushes onto the stack a Lua value of type function that, when called, invokes the corresponding C function.

Any function to be registered in Lua must follow the correct protocol to receive its parameters and return its results (see lua_CFunction).

lua_pushcfunction is defined as a macro:

     #define lua_pushcfunction(L,f)  lua_pushcclosure(L,f,0)
Note that f is used twice.

lua_pushfstring

[-0, +1, e]
const char *lua_pushfstring (lua_State *L, const char *fmt, ...);
Pushes onto the stack a formatted string and returns a pointer to this string. It is similar to the ISO C function sprintf, but has some important differences:

You do not have to allocate space for the result: the result is a Lua string and Lua takes care of memory allocation (and deallocation, through garbage collection).
The conversion specifiers are quite restricted. There are no flags, widths, or precisions. The conversion specifiers can only be '%%' (inserts the character '%'), '%s' (inserts a zero-terminated string, with no size restrictions), '%f' (inserts a lua_Number), '%L' (inserts a lua_Integer), '%p' (inserts a pointer as a hexadecimal numeral), '%d' (inserts an int), '%c' (inserts an int as a one-byte character), and '%U' (inserts a long int as a UTF-8 byte sequence).
lua_pushglobaltable

[-0, +1, –]
void lua_pushglobaltable (lua_State *L);
Pushes the global environment onto the stack.

lua_pushinteger

[-0, +1, –]
void lua_pushinteger (lua_State *L, lua_Integer n);
Pushes an integer with value n onto the stack.

lua_pushlightuserdata

[-0, +1, –]
void lua_pushlightuserdata (lua_State *L, void *p);
Pushes a light userdata onto the stack.

Userdata represent C values in Lua. A light userdata represents a pointer, a void*. It is a value (like a number): you do not create it, it has no individual metatable, and it is not collected (as it was never created). A light userdata is equal to "any" light userdata with the same C address.

lua_pushliteral

[-0, +1, e]
const char *lua_pushliteral (lua_State *L, const char *s);
This macro is equivalent to lua_pushlstring, but can be used only when s is a literal string. It automatically provides the string length.

lua_pushlstring

[-0, +1, e]
const char *lua_pushlstring (lua_State *L, const char *s, size_t len);
Pushes the string pointed to by s with size len onto the stack. Lua makes (or reuses) an internal copy of the given string, so the memory at s can be freed or reused immediately after the function returns. The string can contain any binary data, including embedded zeros.

Returns a pointer to the internal copy of the string.

lua_pushnil

[-0, +1, –]
void lua_pushnil (lua_State *L);
Pushes a nil value onto the stack.

lua_pushnumber

[-0, +1, –]
void lua_pushnumber (lua_State *L, lua_Number n);
Pushes a float with value n onto the stack.

lua_pushstring

[-0, +1, e]
const char *lua_pushstring (lua_State *L, const char *s);
Pushes the zero-terminated string pointed to by s onto the stack. Lua makes (or reuses) an internal copy of the given string, so the memory at s can be freed or reused immediately after the function returns.

Returns a pointer to the internal copy of the string.

If s is NULL, pushes nil and returns NULL.

lua_pushthread

[-0, +1, –]
int lua_pushthread (lua_State *L);
Pushes the thread represented by L onto the stack. Returns 1 if this thread is the main thread of its state.

lua_pushvalue

[-0, +1, –]
void lua_pushvalue (lua_State *L, int index);
Pushes a copy of the element at the given index onto the stack.

lua_pushvfstring

[-0, +1, e]
const char *lua_pushvfstring (lua_State *L,
                              const char *fmt,
                              va_list argp);
Equivalent to lua_pushfstring, except that it receives a va_list instead of a variable number of arguments.

lua_rawequal

[-0, +0, –]
int lua_rawequal (lua_State *L, int index1, int index2);
Returns 1 if the two values in indices index1 and index2 are primitively equal (that is, without calling metamethods). Otherwise returns 0. Also returns 0 if any of the indices are not valid.

lua_rawget

[-1, +1, –]
int lua_rawget (lua_State *L, int index);
Similar to lua_gettable, but does a raw access (i.e., without metamethods).

lua_rawgeti

[-0, +1, –]
int lua_rawgeti (lua_State *L, int index, lua_Integer n);
Pushes onto the stack the value t[n], where t is the table at the given index. The access is raw; that is, it does not invoke metamethods.

Returns the type of the pushed value.

lua_rawgetp

[-0, +1, –]
int lua_rawgetp (lua_State *L, int index, const void *p);
Pushes onto the stack the value t[k], where t is the table at the given index and k is the pointer p represented as a light userdata. The access is raw; that is, it does not invoke metamethods.

Returns the type of the pushed value.

lua_rawlen

[-0, +0, –]
size_t lua_rawlen (lua_State *L, int index);
Returns the raw "length" of the value at the given index: for strings, this is the string length; for tables, this is the result of the length operator ('#') with no metamethods; for userdata, this is the size of the block of memory allocated for the userdata; for other values, it is 0.

lua_rawset

[-2, +0, e]
void lua_rawset (lua_State *L, int index);
Similar to lua_settable, but does a raw assignment (i.e., without metamethods).

lua_rawseti

[-1, +0, e]
void lua_rawseti (lua_State *L, int index, lua_Integer i);
Does the equivalent of t[i] = v, where t is the table at the given index and v is the value at the top of the stack.

This function pops the value from the stack. The assignment is raw; that is, it does not invoke metamethods.

lua_rawsetp

[-1, +0, e]
void lua_rawsetp (lua_State *L, int index, const void *p);
Does the equivalent of t[k] = v, where t is the table at the given index, k is the pointer p represented as a light userdata, and v is the value at the top of the stack.

This function pops the value from the stack. The assignment is raw; that is, it does not invoke metamethods.

lua_Reader

typedef const char * (*lua_Reader) (lua_State *L,
                                    void *data,
                                    size_t *size);
The reader function used by lua_load. Every time it needs another piece of the chunk, lua_load calls the reader, passing along its data parameter. The reader must return a pointer to a block of memory with a new piece of the chunk and set size to the block size. The block must exist until the reader function is called again. To signal the end of the chunk, the reader must return NULL or set size to zero. The reader function may return pieces of any size greater than zero.

lua_register

[-0, +0, e]
void lua_register (lua_State *L, const char *name, lua_CFunction f);
Sets the C function f as the new value of global name. It is defined as a macro:

     #define lua_register(L,n,f) \
            (lua_pushcfunction(L, f), lua_setglobal(L, n))
lua_remove

[-1, +0, –]
void lua_remove (lua_State *L, int index);
Removes the element at the given valid index, shifting down the elements above this index to fill the gap. This function cannot be called with a pseudo-index, because a pseudo-index is not an actual stack position.

lua_replace

[-1, +0, –]
void lua_replace (lua_State *L, int index);
Moves the top element into the given valid index without shifting any element (therefore replacing the value at the given index), and then pops the top element.

lua_resume

[-?, +?, –]
int lua_resume (lua_State *L, lua_State *from, int nargs);
Starts and resumes a coroutine in a given thread.

To start a coroutine, you push onto the thread stack the main function plus any arguments; then you call lua_resume, with nargs being the number of arguments. This call returns when the coroutine suspends or finishes its execution. When it returns, the stack contains all values passed to lua_yield, or all values returned by the body function. lua_resume returns LUA_YIELD if the coroutine yields, LUA_OK if the coroutine finishes its execution without errors, or an error code in case of errors (see lua_pcall).

In case of errors, the stack is not unwound, so you can use the debug API over it. The error message is on the top of the stack.

To resume a coroutine, you remove any results from the last lua_yield, put on its stack only the values to be passed as results from yield, and then call lua_resume.

The parameter from represents the coroutine that is resuming L. If there is no such coroutine, this parameter can be NULL.

lua_rotate

[-0, +0, –]
void lua_rotate (lua_State *L, int idx, int n);
Rotates the stack elements from idx to the top n positions in the direction of the top, for a positive n, or -n positions in the direction of the bottom, for a negative n. The absolute value of n must not be greater than the size of the slice being rotated.

lua_setallocf

[-0, +0, –]
void lua_setallocf (lua_State *L, lua_Alloc f, void *ud);
Changes the allocator function of a given state to f with user data ud.

lua_setfield

[-1, +0, e]
void lua_setfield (lua_State *L, int index, const char *k);
Does the equivalent to t[k] = v, where t is the value at the given index and v is the value at the top of the stack.

This function pops the value from the stack. As in Lua, this function may trigger a metamethod for the "newindex" event (see §2.4).

lua_setglobal

[-1, +0, e]
void lua_setglobal (lua_State *L, const char *name);
Pops a value from the stack and sets it as the new value of global name.

lua_seti

[-1, +0, e]
void lua_seti (lua_State *L, int index, lua_Integer n);
Does the equivalent to t[n] = v, where t is the value at the given index and v is the value at the top of the stack.

This function pops the value from the stack. As in Lua, this function may trigger a metamethod for the "newindex" event (see §2.4).

lua_setmetatable

[-1, +0, –]
void lua_setmetatable (lua_State *L, int index);
Pops a table from the stack and sets it as the new metatable for the value at the given index.

lua_settable

[-2, +0, e]
void lua_settable (lua_State *L, int index);
Does the equivalent to t[k] = v, where t is the value at the given index, v is the value at the top of the stack, and k is the value just below the top.

This function pops both the key and the value from the stack. As in Lua, this function may trigger a metamethod for the "newindex" event (see §2.4).

lua_settop

[-?, +?, –]
void lua_settop (lua_State *L, int index);
Accepts any index, or 0, and sets the stack top to this index. If the new top is larger than the old one, then the new elements are filled with nil. If index is 0, then all stack elements are removed.

lua_setuservalue

[-1, +0, –]
void lua_setuservalue (lua_State *L, int index);
Pops a value from the stack and sets it as the new value associated to the userdata at the given index.

lua_State

typedef struct lua_State lua_State;
An opaque structure that points to a thread and indirectly (through the thread) to the whole state of a Lua interpreter. The Lua library is fully reentrant: it has no global variables. All information about a state is accessible through this structure.

A pointer to this structure must be passed as the first argument to every function in the library, except to lua_newstate, which creates a Lua state from scratch.

lua_status

[-0, +0, –]
int lua_status (lua_State *L);
Returns the status of the thread L.

The status can be 0 (LUA_OK) for a normal thread, an error code if the thread finished the execution of a lua_resume with an error, or LUA_YIELD if the thread is suspended.

You can only call functions in threads with status LUA_OK. You can resume threads with status LUA_OK (to start a new coroutine) or LUA_YIELD (to resume a coroutine).

lua_stringtonumber

[-0, +1, –]
size_t lua_stringtonumber (lua_State *L, const char *s);
Converts the zero-terminated string s to a number, pushes that number into the stack, and returns the total size of the string, that is, its length plus one. The conversion can result in an integer or a float, according to the lexical conventions of Lua (see §3.1). The string may have leading and trailing spaces and a sign. If the string is not a valid numeral, returns 0 and pushes nothing. (Note that the result can be used as a boolean, true if the conversion succeeds.)

lua_toboolean

[-0, +0, –]
int lua_toboolean (lua_State *L, int index);
Converts the Lua value at the given index to a C boolean value (0 or 1). Like all tests in Lua, lua_toboolean returns true for any Lua value different from false and nil; otherwise it returns false. (If you want to accept only actual boolean values, use lua_isboolean to test the value's type.)

lua_tocfunction

[-0, +0, –]
lua_CFunction lua_tocfunction (lua_State *L, int index);
Converts a value at the given index to a C function. That value must be a C function; otherwise, returns NULL.

lua_tointeger

[-0, +0, –]
lua_Integer lua_tointeger (lua_State *L, int index);
Equivalent to lua_tointegerx with isnum equal to NULL.

lua_tointegerx

[-0, +0, –]
lua_Integer lua_tointegerx (lua_State *L, int index, int *isnum);
Converts the Lua value at the given index to the signed integral type lua_Integer. The Lua value must be an integer, or a number or string convertible to an integer (see §3.4.3); otherwise, lua_tointegerx returns 0.

If isnum is not NULL, its referent is assigned a boolean value that indicates whether the operation succeeded.

lua_tolstring

[-0, +0, e]
const char *lua_tolstring (lua_State *L, int index, size_t *len);
Converts the Lua value at the given index to a C string. If len is not NULL, it also sets *len with the string length. The Lua value must be a string or a number; otherwise, the function returns NULL. If the value is a number, then lua_tolstring also changes the actual value in the stack to a string. (This change confuses lua_next when lua_tolstring is applied to keys during a table traversal.)

lua_tolstring returns a fully aligned pointer to a string inside the Lua state. This string always has a zero ('\0') after its last character (as in C), but can contain other zeros in its body.

Because Lua has garbage collection, there is no guarantee that the pointer returned by lua_tolstring will be valid after the corresponding Lua value is removed from the stack.

lua_tonumber

[-0, +0, –]
lua_Number lua_tonumber (lua_State *L, int index);
Equivalent to lua_tonumberx with isnum equal to NULL.

lua_tonumberx

[-0, +0, –]
lua_Number lua_tonumberx (lua_State *L, int index, int *isnum);
Converts the Lua value at the given index to the C type lua_Number (see lua_Number). The Lua value must be a number or a string convertible to a number (see §3.4.3); otherwise, lua_tonumberx returns 0.

If isnum is not NULL, its referent is assigned a boolean value that indicates whether the operation succeeded.

lua_topointer

[-0, +0, –]
const void *lua_topointer (lua_State *L, int index);
Converts the value at the given index to a generic C pointer (void*). The value can be a userdata, a table, a thread, or a function; otherwise, lua_topointer returns NULL. Different objects will give different pointers. There is no way to convert the pointer back to its original value.

Typically this function is used only for debug information.

lua_tostring

[-0, +0, e]
const char *lua_tostring (lua_State *L, int index);
Equivalent to lua_tolstring with len equal to NULL.

lua_tothread

[-0, +0, –]
lua_State *lua_tothread (lua_State *L, int index);
Converts the value at the given index to a Lua thread (represented as lua_State*). This value must be a thread; otherwise, the function returns NULL.

lua_touserdata

[-0, +0, –]
void *lua_touserdata (lua_State *L, int index);
If the value at the given index is a full userdata, returns its block address. If the value is a light userdata, returns its pointer. Otherwise, returns NULL.

lua_type

[-0, +0, –]
int lua_type (lua_State *L, int index);
Returns the type of the value in the given valid index, or LUA_TNONE for a non-valid (but acceptable) index. The types returned by lua_type are coded by the following constants defined in lua.h: LUA_TNIL, LUA_TNUMBER, LUA_TBOOLEAN, LUA_TSTRING, LUA_TTABLE, LUA_TFUNCTION, LUA_TUSERDATA, LUA_TTHREAD, and LUA_TLIGHTUSERDATA.

lua_typename

[-0, +0, –]
const char *lua_typename (lua_State *L, int tp);
Returns the name of the type encoded by the value tp, which must be one the values returned by lua_type.

lua_Unsigned

typedef ... lua_Unsigned;
The unsigned version of lua_Integer.

lua_upvalueindex

[-0, +0, –]
int lua_upvalueindex (int i);
Returns the pseudo-index that represents the i-th upvalue of the running function (see §4.4).

lua_version

[-0, +0, v]
const lua_Number *lua_version (lua_State *L);
Returns the address of the version number stored in the Lua core. When called with a valid lua_State, returns the address of the version used to create that state. When called with NULL, returns the address of the version running the call.

lua_Writer

typedef int (*lua_Writer) (lua_State *L,
                           const void* p,
                           size_t sz,
                           void* ud);
The type of the writer function used by lua_dump. Every time it produces another piece of chunk, lua_dump calls the writer, passing along the buffer to be written (p), its size (sz), and the data parameter supplied to lua_dump.

The writer returns an error code: 0 means no errors; any other value means an error and stops lua_dump from calling the writer again.

lua_xmove

[-?, +?, –]
void lua_xmove (lua_State *from, lua_State *to, int n);
Exchange values between different threads of the same state.

This function pops n values from the stack from, and pushes them onto the stack to.

lua_yield

[-?, +?, e]
int lua_yield (lua_State *L, int nresults);
This function is equivalent to lua_yieldk, but it has no continuation (see §4.7). Therefore, when the thread resumes, it continues the function that called the function calling lua_yield.

lua_yieldk

[-?, +?, e]
int lua_yieldk (lua_State *L,
                int nresults,
                lua_KContext ctx,
                lua_KFunction k);
Yields a coroutine (thread).

When a C function calls lua_yieldk, the running coroutine suspends its execution, and the call to lua_resume that started this coroutine returns. The parameter nresults is the number of values from the stack that will be passed as results to lua_resume.

When the coroutine is resumed again, Lua calls the given continuation function k to continue the execution of the C function that yielded (see §4.7). This continuation function receives the same stack from the previous function, with the n results removed and replaced by the arguments passed to lua_resume. Moreover, the continuation function receives the value ctx that was passed to lua_yieldk.

Usually, this function does not return; when the coroutine eventually resumes, it continues executing the continuation function. However, there is one special case, which is when this function is called from inside a line hook (see §4.9). In that case, lua_yieldk should be called with no continuation (probably in the form of lua_yield), and the hook should return immediately after the call. Lua will yield and, when the coroutine resumes again, it will continue the normal execution of the (Lua) function that triggered the hook.

This function can raise an error if it is called from a thread with a pending C call with no continuation function, or it is called from a thread that is not running inside a resume (e.g., the main thread).

4.9 – The Debug Interface

Lua has no built-in debugging facilities. Instead, it offers a special interface by means of functions and hooks. This interface allows the construction of different kinds of debuggers, profilers, and other tools that need "inside information" from the interpreter.

lua_Debug

typedef struct lua_Debug {
  int event;
  const char *name;           /* (n) */
  const char *namewhat;       /* (n) */
  const char *what;           /* (S) */
  const char *source;         /* (S) */
  int currentline;            /* (l) */
  int linedefined;            /* (S) */
  int lastlinedefined;        /* (S) */
  unsigned char nups;         /* (u) number of upvalues */
  unsigned char nparams;      /* (u) number of parameters */
  char isvararg;              /* (u) */
  char istailcall;            /* (t) */
  char short_src[LUA_IDSIZE]; /* (S) */
  /* private part */
  other fields
} lua_Debug;
A structure used to carry different pieces of information about a function or an activation record. lua_getstack fills only the private part of this structure, for later use. To fill the other fields of lua_Debug with useful information, call lua_getinfo.

The fields of lua_Debug have the following meaning:

source: the name of the chunk that created the function. If source starts with a '@', it means that the function was defined in a file where the file name follows the '@'. If source starts with a '=', the remainder of its contents describe the source in a user-dependent manner. Otherwise, the function was defined in a string where source is that string.
short_src: a "printable" version of source, to be used in error messages.
linedefined: the line number where the definition of the function starts.
lastlinedefined: the line number where the definition of the function ends.
what: the string "Lua" if the function is a Lua function, "C" if it is a C function, "main" if it is the main part of a chunk.
currentline: the current line where the given function is executing. When no line information is available, currentline is set to -1.
name: a reasonable name for the given function. Because functions in Lua are first-class values, they do not have a fixed name: some functions can be the value of multiple global variables, while others can be stored only in a table field. The lua_getinfo function checks how the function was called to find a suitable name. If it cannot find a name, then name is set to NULL.
namewhat: explains the name field. The value of namewhat can be "global", "local", "method", "field", "upvalue", or "" (the empty string), according to how the function was called. (Lua uses the empty string when no other option seems to apply.)
istailcall: true if this function invocation was called by a tail call. In this case, the caller of this level is not in the stack.
nups: the number of upvalues of the function.
nparams: the number of fixed parameters of the function (always 0 for C functions).
isvararg: true if the function is a vararg function (always true for C functions).
lua_gethook

[-0, +0, –]
lua_Hook lua_gethook (lua_State *L);
Returns the current hook function.

lua_gethookcount

[-0, +0, –]
int lua_gethookcount (lua_State *L);
Returns the current hook count.

lua_gethookmask

[-0, +0, –]
int lua_gethookmask (lua_State *L);
Returns the current hook mask.

lua_getinfo

[-(0|1), +(0|1|2), e]
int lua_getinfo (lua_State *L, const char *what, lua_Debug *ar);
Gets information about a specific function or function invocation.

To get information about a function invocation, the parameter ar must be a valid activation record that was filled by a previous call to lua_getstack or given as argument to a hook (see lua_Hook).

To get information about a function you push it onto the stack and start the what string with the character '>'. (In that case, lua_getinfo pops the function from the top of the stack.) For instance, to know in which line a function f was defined, you can write the following code:

     lua_Debug ar;
     lua_getglobal(L, "f");  /* get global 'f' */
     lua_getinfo(L, ">S", &ar);
     printf("%d\n", ar.linedefined);
Each character in the string what selects some fields of the structure ar to be filled or a value to be pushed on the stack:

'n': fills in the field name and namewhat;
'S': fills in the fields source, short_src, linedefined, lastlinedefined, and what;
'l': fills in the field currentline;
't': fills in the field istailcall;
'u': fills in the fields nups, nparams, and isvararg;
'f': pushes onto the stack the function that is running at the given level;
'L': pushes onto the stack a table whose indices are the numbers of the lines that are valid on the function. (A valid line is a line with some associated code, that is, a line where you can put a break point. Non-valid lines include empty lines and comments.)
If this option is given together with option 'f', its table is pushed after the function.

This function returns 0 on error (for instance, an invalid option in what).

lua_getlocal

[-0, +(0|1), –]
const char *lua_getlocal (lua_State *L, const lua_Debug *ar, int n);
Gets information about a local variable of a given activation record or a given function.

In the first case, the parameter ar must be a valid activation record that was filled by a previous call to lua_getstack or given as argument to a hook (see lua_Hook). The index n selects which local variable to inspect; see debug.getlocal for details about variable indices and names.

lua_getlocal pushes the variable's value onto the stack and returns its name.

In the second case, ar must be NULL and the function to be inspected must be at the top of the stack. In this case, only parameters of Lua functions are visible (as there is no information about what variables are active) and no values are pushed onto the stack.

Returns NULL (and pushes nothing) when the index is greater than the number of active local variables.

lua_getstack

[-0, +0, –]
int lua_getstack (lua_State *L, int level, lua_Debug *ar);
Gets information about the interpreter runtime stack.

This function fills parts of a lua_Debug structure with an identification of the activation record of the function executing at a given level. Level 0 is the current running function, whereas level n+1 is the function that has called level n (except for tail calls, which do not count on the stack). When there are no errors, lua_getstack returns 1; when called with a level greater than the stack depth, it returns 0.

lua_getupvalue

[-0, +(0|1), –]
const char *lua_getupvalue (lua_State *L, int funcindex, int n);
Gets information about a closure's upvalue. (For Lua functions, upvalues are the external local variables that the function uses, and that are consequently included in its closure.) lua_getupvalue gets the index n of an upvalue, pushes the upvalue's value onto the stack, and returns its name. funcindex points to the closure in the stack. (Upvalues have no particular order, as they are active through the whole function. So, they are numbered in an arbitrary order.)

Returns NULL (and pushes nothing) when the index is greater than the number of upvalues. For C functions, this function uses the empty string "" as a name for all upvalues.

lua_Hook

typedef void (*lua_Hook) (lua_State *L, lua_Debug *ar);
Type for debugging hook functions.

Whenever a hook is called, its ar argument has its field event set to the specific event that triggered the hook. Lua identifies these events with the following constants: LUA_HOOKCALL, LUA_HOOKRET, LUA_HOOKTAILCALL, LUA_HOOKLINE, and LUA_HOOKCOUNT. Moreover, for line events, the field currentline is also set. To get the value of any other field in ar, the hook must call lua_getinfo.

For call events, event can be LUA_HOOKCALL, the normal value, or LUA_HOOKTAILCALL, for a tail call; in this case, there will be no corresponding return event.

While Lua is running a hook, it disables other calls to hooks. Therefore, if a hook calls back Lua to execute a function or a chunk, this execution occurs without any calls to hooks.

Hook functions cannot have continuations, that is, they cannot call lua_yieldk, lua_pcallk, or lua_callk with a non-null k.

Hook functions can yield under the following conditions: Only count and line events can yield and they cannot yield any value; to yield a hook function must finish its execution calling lua_yield with nresults equal to zero.

lua_sethook

[-0, +0, –]
void lua_sethook (lua_State *L, lua_Hook f, int mask, int count);
Sets the debugging hook function.

Argument f is the hook function. mask specifies on which events the hook will be called: it is formed by a bitwise or of the constants LUA_MASKCALL, LUA_MASKRET, LUA_MASKLINE, and LUA_MASKCOUNT. The count argument is only meaningful when the mask includes LUA_MASKCOUNT. For each event, the hook is called as explained below:

The call hook: is called when the interpreter calls a function. The hook is called just after Lua enters the new function, before the function gets its arguments.
The return hook: is called when the interpreter returns from a function. The hook is called just before Lua leaves the function. There is no standard way to access the values to be returned by the function.
The line hook: is called when the interpreter is about to start the execution of a new line of code, or when it jumps back in the code (even to the same line). (This event only happens while Lua is executing a Lua function.)
The count hook: is called after the interpreter executes every count instructions. (This event only happens while Lua is executing a Lua function.)
A hook is disabled by setting mask to zero.

lua_setlocal

[-(0|1), +0, –]
const char *lua_setlocal (lua_State *L, const lua_Debug *ar, int n);
Sets the value of a local variable of a given activation record. Parameters ar and n are as in lua_getlocal (see lua_getlocal). lua_setlocal assigns the value at the top of the stack to the variable and returns its name. It also pops the value from the stack.

Returns NULL (and pops nothing) when the index is greater than the number of active local variables.

lua_setupvalue

[-(0|1), +0, –]
const char *lua_setupvalue (lua_State *L, int funcindex, int n);
Sets the value of a closure's upvalue. It assigns the value at the top of the stack to the upvalue and returns its name. It also pops the value from the stack. Parameters funcindex and n are as in the lua_getupvalue (see lua_getupvalue).

Returns NULL (and pops nothing) when the index is greater than the number of upvalues.

lua_upvalueid

[-0, +0, –]
void *lua_upvalueid (lua_State *L, int funcindex, int n);
Returns a unique identifier for the upvalue numbered n from the closure at index funcindex. Parameters funcindex and n are as in the lua_getupvalue (see lua_getupvalue) (but n cannot be greater than the number of upvalues).

These unique identifiers allow a program to check whether different closures share upvalues. Lua closures that share an upvalue (that is, that access a same external local variable) will return identical ids for those upvalue indices.

lua_upvaluejoin

[-0, +0, –]
void lua_upvaluejoin (lua_State *L, int funcindex1, int n1,
                                    int funcindex2, int n2);
Make the n1-th upvalue of the Lua closure at index funcindex1 refer to the n2-th upvalue of the Lua closure at index funcindex2.

#5 – The Auxiliary Library

The auxiliary library provides several convenient functions to interface C with Lua. While the basic API provides the primitive functions for all interactions between C and Lua, the auxiliary library provides higher-level functions for some common tasks.

All functions and types from the auxiliary library are defined in header file lauxlib.h and have a prefix luaL_.

All functions in the auxiliary library are built on top of the basic API, and so they provide nothing that cannot be done with that API. Nevertheless, the use of the auxiliary library ensures more consistency to your code.

Several functions in the auxiliary library use internally some extra stack slots. When a function in the auxiliary library uses less than five slots, it does not check the stack size; it simply assumes that there are enough slots.

Several functions in the auxiliary library are used to check C function arguments. Because the error message is formatted for arguments (e.g., "bad argument #1"), you should not use these functions for other stack values.

Functions called luaL_check* always raise an error if the check is not satisfied.

5.1 – Functions and Types

Here we list all functions and types from the auxiliary library in alphabetical order.

luaL_addchar

[-?, +?, e]
void luaL_addchar (luaL_Buffer *B, char c);
Adds the byte c to the buffer B (see luaL_Buffer).

luaL_addlstring

[-?, +?, e]
void luaL_addlstring (luaL_Buffer *B, const char *s, size_t l);
Adds the string pointed to by s with length l to the buffer B (see luaL_Buffer). The string can contain embedded zeros.

luaL_addsize

[-?, +?, e]
void luaL_addsize (luaL_Buffer *B, size_t n);
Adds to the buffer B (see luaL_Buffer) a string of length n previously copied to the buffer area (see luaL_prepbuffer).

luaL_addstring

[-?, +?, e]
void luaL_addstring (luaL_Buffer *B, const char *s);
Adds the zero-terminated string pointed to by s to the buffer B (see luaL_Buffer).

luaL_addvalue

[-1, +?, e]
void luaL_addvalue (luaL_Buffer *B);
Adds the value at the top of the stack to the buffer B (see luaL_Buffer). Pops the value.

This is the only function on string buffers that can (and must) be called with an extra element on the stack, which is the value to be added to the buffer.

luaL_argcheck

[-0, +0, v]
void luaL_argcheck (lua_State *L,
                    int cond,
                    int arg,
                    const char *extramsg);
Checks whether cond is true. If it is not, raises an error with a standard message (see luaL_argerror).

luaL_argerror

[-0, +0, v]
int luaL_argerror (lua_State *L, int arg, const char *extramsg);
Raises an error reporting a problem with argument arg of the C function that called it, using a standard message that includes extramsg as a comment:

     bad argument #arg to 'funcname' (extramsg)
This function never returns.

luaL_Buffer

typedef struct luaL_Buffer luaL_Buffer;
Type for a string buffer.

A string buffer allows C code to build Lua strings piecemeal. Its pattern of use is as follows:

First declare a variable b of type luaL_Buffer.
Then initialize it with a call luaL_buffinit(L, &b).
Then add string pieces to the buffer calling any of the luaL_add* functions.
Finish by calling luaL_pushresult(&b). This call leaves the final string on the top of the stack.
If you know beforehand the total size of the resulting string, you can use the buffer like this:

First declare a variable b of type luaL_Buffer.
Then initialize it and preallocate a space of size sz with a call luaL_buffinitsize(L, &b, sz).
Then copy the string into that space.
Finish by calling luaL_pushresultsize(&b, sz), where sz is the total size of the resulting string copied into that space.
During its normal operation, a string buffer uses a variable number of stack slots. So, while using a buffer, you cannot assume that you know where the top of the stack is. You can use the stack between successive calls to buffer operations as long as that use is balanced; that is, when you call a buffer operation, the stack is at the same level it was immediately after the previous buffer operation. (The only exception to this rule is luaL_addvalue.) After calling luaL_pushresult the stack is back to its level when the buffer was initialized, plus the final string on its top.

luaL_buffinit

[-0, +0, –]
void luaL_buffinit (lua_State *L, luaL_Buffer *B);
Initializes a buffer B. This function does not allocate any space; the buffer must be declared as a variable (see luaL_Buffer).

luaL_buffinitsize

[-?, +?, e]
char *luaL_buffinitsize (lua_State *L, luaL_Buffer *B, size_t sz);
Equivalent to the sequence luaL_buffinit, luaL_prepbuffsize.

luaL_callmeta

[-0, +(0|1), e]
int luaL_callmeta (lua_State *L, int obj, const char *e);
Calls a metamethod.

If the object at index obj has a metatable and this metatable has a field e, this function calls this field passing the object as its only argument. In this case this function returns true and pushes onto the stack the value returned by the call. If there is no metatable or no metamethod, this function returns false (without pushing any value on the stack).

luaL_checkany

[-0, +0, v]
void luaL_checkany (lua_State *L, int arg);
Checks whether the function has an argument of any type (including nil) at position arg.

luaL_checkinteger

[-0, +0, v]
lua_Integer luaL_checkinteger (lua_State *L, int arg);
Checks whether the function argument arg is an integer (or can be converted to an integer) and returns this integer cast to a lua_Integer.

luaL_checklstring

[-0, +0, v]
const char *luaL_checklstring (lua_State *L, int arg, size_t *l);
Checks whether the function argument arg is a string and returns this string; if l is not NULL fills *l with the string's length.

This function uses lua_tolstring to get its result, so all conversions and caveats of that function apply here.

luaL_checknumber

[-0, +0, v]
lua_Number luaL_checknumber (lua_State *L, int arg);
Checks whether the function argument arg is a number and returns this number.

luaL_checkoption

[-0, +0, v]
int luaL_checkoption (lua_State *L,
                      int arg,
                      const char *def,
                      const char *const lst[]);
Checks whether the function argument arg is a string and searches for this string in the array lst (which must be NULL-terminated). Returns the index in the array where the string was found. Raises an error if the argument is not a string or if the string cannot be found.

If def is not NULL, the function uses def as a default value when there is no argument arg or when this argument is nil.

This is a useful function for mapping strings to C enums. (The usual convention in Lua libraries is to use strings instead of numbers to select options.)

luaL_checkstack

[-0, +0, v]
void luaL_checkstack (lua_State *L, int sz, const char *msg);
Grows the stack size to top + sz elements, raising an error if the stack cannot grow to that size. msg is an additional text to go into the error message (or NULL for no additional text).

luaL_checkstring

[-0, +0, v]
const char *luaL_checkstring (lua_State *L, int arg);
Checks whether the function argument arg is a string and returns this string.

This function uses lua_tolstring to get its result, so all conversions and caveats of that function apply here.

luaL_checktype

[-0, +0, v]
void luaL_checktype (lua_State *L, int arg, int t);
Checks whether the function argument arg has type t. See lua_type for the encoding of types for t.

luaL_checkudata

[-0, +0, v]
void *luaL_checkudata (lua_State *L, int arg, const char *tname);
Checks whether the function argument arg is a userdata of the type tname (see luaL_newmetatable) and returns the userdata address (see lua_touserdata).

luaL_checkversion

[-0, +0, –]
void luaL_checkversion (lua_State *L);
Checks whether the core running the call, the core that created the Lua state, and the code making the call are all using the same version of Lua. Also checks whether the core running the call and the core that created the Lua state are using the same address space.

luaL_dofile

[-0, +?, e]
int luaL_dofile (lua_State *L, const char *filename);
Loads and runs the given file. It is defined as the following macro:

     (luaL_loadfile(L, filename) || lua_pcall(L, 0, LUA_MULTRET, 0))
It returns false if there are no errors or true in case of errors.

luaL_dostring

[-0, +?, –]
int luaL_dostring (lua_State *L, const char *str);
Loads and runs the given string. It is defined as the following macro:

     (luaL_loadstring(L, str) || lua_pcall(L, 0, LUA_MULTRET, 0))
It returns false if there are no errors or true in case of errors.

luaL_error

[-0, +0, v]
int luaL_error (lua_State *L, const char *fmt, ...);
Raises an error. The error message format is given by fmt plus any extra arguments, following the same rules of lua_pushfstring. It also adds at the beginning of the message the file name and the line number where the error occurred, if this information is available.

This function never returns, but it is an idiom to use it in C functions as return luaL_error(args).

luaL_execresult

[-0, +3, e]
int luaL_execresult (lua_State *L, int stat);
This function produces the return values for process-related functions in the standard library (os.execute and io.close).

luaL_fileresult

[-0, +(1|3), e]
int luaL_fileresult (lua_State *L, int stat, const char *fname);
This function produces the return values for file-related functions in the standard library (io.open, os.rename, file:seek, etc.).

luaL_getmetafield

[-0, +(0|1), e]
int luaL_getmetafield (lua_State *L, int obj, const char *e);
Pushes onto the stack the field e from the metatable of the object at index obj and returns the type of pushed value. If the object does not have a metatable, or if the metatable does not have this field, pushes nothing and returns LUA_TNIL.

luaL_getmetatable

[-0, +1, –]
int luaL_getmetatable (lua_State *L, const char *tname);
Pushes onto the stack the metatable associated with name tname in the registry (see luaL_newmetatable). If there is no metatable associated with tname, returns false and pushes nil.

luaL_getsubtable

[-0, +1, e]
int luaL_getsubtable (lua_State *L, int idx, const char *fname);
Ensures that the value t[fname], where t is the value at index idx, is a table, and pushes that table onto the stack. Returns true if it finds a previous table there and false if it creates a new table.

luaL_gsub

[-0, +1, e]
const char *luaL_gsub (lua_State *L,
                       const char *s,
                       const char *p,
                       const char *r);
Creates a copy of string s by replacing any occurrence of the string p with the string r. Pushes the resulting string on the stack and returns it.

luaL_len

[-0, +0, e]
lua_Integer luaL_len (lua_State *L, int index);
Returns the "length" of the value at the given index as a number; it is equivalent to the '#' operator in Lua (see §3.4.7). Raises an error if the result of the operation is not an integer. (This case only can happen through metamethods.)

luaL_loadbuffer

[-0, +1, –]
int luaL_loadbuffer (lua_State *L,
                     const char *buff,
                     size_t sz,
                     const char *name);
Equivalent to luaL_loadbufferx with mode equal to NULL.

luaL_loadbufferx

[-0, +1, –]
int luaL_loadbufferx (lua_State *L,
                      const char *buff,
                      size_t sz,
                      const char *name,
                      const char *mode);
Loads a buffer as a Lua chunk. This function uses lua_load to load the chunk in the buffer pointed to by buff with size sz.

This function returns the same results as lua_load. name is the chunk name, used for debug information and error messages. The string mode works as in function lua_load.

luaL_loadfile

[-0, +1, e]
int luaL_loadfile (lua_State *L, const char *filename);
Equivalent to luaL_loadfilex with mode equal to NULL.

luaL_loadfilex

[-0, +1, e]
int luaL_loadfilex (lua_State *L, const char *filename,
                                            const char *mode);
Loads a file as a Lua chunk. This function uses lua_load to load the chunk in the file named filename. If filename is NULL, then it loads from the standard input. The first line in the file is ignored if it starts with a #.

The string mode works as in function lua_load.

This function returns the same results as lua_load, but it has an extra error code LUA_ERRFILE if it cannot open/read the file or the file has a wrong mode.

As lua_load, this function only loads the chunk; it does not run it.

luaL_loadstring

[-0, +1, –]
int luaL_loadstring (lua_State *L, const char *s);
Loads a string as a Lua chunk. This function uses lua_load to load the chunk in the zero-terminated string s.

This function returns the same results as lua_load.

Also as lua_load, this function only loads the chunk; it does not run it.

luaL_newlib

[-0, +1, e]
void luaL_newlib (lua_State *L, const luaL_Reg l[]);
Creates a new table and registers there the functions in list l.

It is implemented as the following macro:

     (luaL_newlibtable(L,l), luaL_setfuncs(L,l,0))
The array l must be the actual array, not a pointer to it.

luaL_newlibtable

[-0, +1, e]
void luaL_newlibtable (lua_State *L, const luaL_Reg l[]);
Creates a new table with a size optimized to store all entries in the array l (but does not actually store them). It is intended to be used in conjunction with luaL_setfuncs (see luaL_newlib).

It is implemented as a macro. The array l must be the actual array, not a pointer to it.

luaL_newmetatable

[-0, +1, e]
int luaL_newmetatable (lua_State *L, const char *tname);
If the registry already has the key tname, returns 0. Otherwise, creates a new table to be used as a metatable for userdata, adds to this new table the pair __name = tname, adds to the registry the pair [tname] = new table, and returns 1. (The entry __name is used by some error-reporting functions.)

In both cases pushes onto the stack the final value associated with tname in the registry.

luaL_newstate

[-0, +0, –]
lua_State *luaL_newstate (void);
Creates a new Lua state. It calls lua_newstate with an allocator based on the standard C realloc function and then sets a panic function (see §4.6) that prints an error message to the standard error output in case of fatal errors.

Returns the new state, or NULL if there is a memory allocation error.

luaL_openlibs

[-0, +0, e]
void luaL_openlibs (lua_State *L);
Opens all standard Lua libraries into the given state.

luaL_optinteger

[-0, +0, v]
lua_Integer luaL_optinteger (lua_State *L,
                             int arg,
                             lua_Integer d);
If the function argument arg is an integer (or convertible to an integer), returns this integer. If this argument is absent or is nil, returns d. Otherwise, raises an error.

luaL_optlstring

[-0, +0, v]
const char *luaL_optlstring (lua_State *L,
                             int arg,
                             const char *d,
                             size_t *l);
If the function argument arg is a string, returns this string. If this argument is absent or is nil, returns d. Otherwise, raises an error.

If l is not NULL, fills the position *l with the result's length.

luaL_optnumber

[-0, +0, v]
lua_Number luaL_optnumber (lua_State *L, int arg, lua_Number d);
If the function argument arg is a number, returns this number. If this argument is absent or is nil, returns d. Otherwise, raises an error.

luaL_optstring

[-0, +0, v]
const char *luaL_optstring (lua_State *L,
                            int arg,
                            const char *d);
If the function argument arg is a string, returns this string. If this argument is absent or is nil, returns d. Otherwise, raises an error.

luaL_prepbuffer

[-?, +?, e]
char *luaL_prepbuffer (luaL_Buffer *B);
Equivalent to luaL_prepbuffsize with the predefined size LUAL_BUFFERSIZE.

luaL_prepbuffsize

[-?, +?, e]
char *luaL_prepbuffsize (luaL_Buffer *B, size_t sz);
Returns an address to a space of size sz where you can copy a string to be added to buffer B (see luaL_Buffer). After copying the string into this space you must call luaL_addsize with the size of the string to actually add it to the buffer.

luaL_pushresult

[-?, +1, e]
void luaL_pushresult (luaL_Buffer *B);
Finishes the use of buffer B leaving the final string on the top of the stack.

luaL_pushresultsize

[-?, +1, e]
void luaL_pushresultsize (luaL_Buffer *B, size_t sz);
Equivalent to the sequence luaL_addsize, luaL_pushresult.

luaL_ref

[-1, +0, e]
int luaL_ref (lua_State *L, int t);
Creates and returns a reference, in the table at index t, for the object at the top of the stack (and pops the object).

A reference is a unique integer key. As long as you do not manually add integer keys into table t, luaL_ref ensures the uniqueness of the key it returns. You can retrieve an object referred by reference r by calling lua_rawgeti(L, t, r). Function luaL_unref frees a reference and its associated object.

If the object at the top of the stack is nil, luaL_ref returns the constant LUA_REFNIL. The constant LUA_NOREF is guaranteed to be different from any reference returned by luaL_ref.

luaL_Reg

typedef struct luaL_Reg {
  const char *name;
  lua_CFunction func;
} luaL_Reg;
Type for arrays of functions to be registered by luaL_setfuncs. name is the function name and func is a pointer to the function. Any array of luaL_Reg must end with a sentinel entry in which both name and func are NULL.

luaL_requiref

[-0, +1, e]
void luaL_requiref (lua_State *L, const char *modname,
                    lua_CFunction openf, int glb);
If modname is not already present in package.loaded, calls function openf with string modname as an argument and sets the call result in package.loaded[modname], as if that function has been called through require.

If glb is true, also stores the module into global modname.

Leaves a copy of the module on the stack.

luaL_setfuncs

[-nup, +0, e]
void luaL_setfuncs (lua_State *L, const luaL_Reg *l, int nup);
Registers all functions in the array l (see luaL_Reg) into the table on the top of the stack (below optional upvalues, see next).

When nup is not zero, all functions are created sharing nup upvalues, which must be previously pushed on the stack on top of the library table. These values are popped from the stack after the registration.

luaL_setmetatable

[-0, +0, –]
void luaL_setmetatable (lua_State *L, const char *tname);
Sets the metatable of the object at the top of the stack as the metatable associated with name tname in the registry (see luaL_newmetatable).

luaL_Stream

typedef struct luaL_Stream {
  FILE *f;
  lua_CFunction closef;
} luaL_Stream;
The standard representation for file handles, which is used by the standard I/O library.

A file handle is implemented as a full userdata, with a metatable called LUA_FILEHANDLE (where LUA_FILEHANDLE is a macro with the actual metatable's name). The metatable is created by the I/O library (see luaL_newmetatable).

This userdata must start with the structure luaL_Stream; it can contain other data after this initial structure. Field f points to the corresponding C stream (or it can be NULL to indicate an incompletely created handle). Field closef points to a Lua function that will be called to close the stream when the handle is closed or collected; this function receives the file handle as its sole argument and must return either true (in case of success) or nil plus an error message (in case of error). Once Lua calls this field, the field value is changed to NULL to signal that the handle is closed.

luaL_testudata

[-0, +0, e]
void *luaL_testudata (lua_State *L, int arg, const char *tname);
This function works like luaL_checkudata, except that, when the test fails, it returns NULL instead of raising an error.

luaL_tolstring

[-0, +1, e]
const char *luaL_tolstring (lua_State *L, int idx, size_t *len);
Converts any Lua value at the given index to a C string in a reasonable format. The resulting string is pushed onto the stack and also returned by the function. If len is not NULL, the function also sets *len with the string length.

If the value has a metatable with a "__tostring" field, then luaL_tolstring calls the corresponding metamethod with the value as argument, and uses the result of the call as its result.

luaL_traceback

[-0, +1, e]
void luaL_traceback (lua_State *L, lua_State *L1, const char *msg,
                     int level);
Creates and pushes a traceback of the stack L1. If msg is not NULL it is appended at the beginning of the traceback. The level parameter tells at which level to start the traceback.

luaL_typename

[-0, +0, –]
const char *luaL_typename (lua_State *L, int index);
Returns the name of the type of the value at the given index.

luaL_unref

[-0, +0, –]
void luaL_unref (lua_State *L, int t, int ref);
Releases reference ref from the table at index t (see luaL_ref). The entry is removed from the table, so that the referred object can be collected. The reference ref is also freed to be used again.

If ref is LUA_NOREF or LUA_REFNIL, luaL_unref does nothing.

luaL_where

[-0, +1, e]
void luaL_where (lua_State *L, int lvl);
Pushes onto the stack a string identifying the current position of the control at level lvl in the call stack. Typically this string has the following format:

     chunkname:currentline:
Level 0 is the running function, level 1 is the function that called the running function, etc.

This function is used to build a prefix for error messages.

#6 – Standard Libraries

The standard Lua libraries provide useful functions that are implemented directly through the C API. Some of these functions provide essential services to the language (e.g., type and getmetatable); others provide access to "outside" services (e.g., I/O); and others could be implemented in Lua itself, but are quite useful or have critical performance requirements that deserve an implementation in C (e.g., table.sort).

All libraries are implemented through the official C API and are provided as separate C modules. Currently, Lua has the following standard libraries:

basic library (§6.1);
coroutine library (§6.2);
package library (§6.3);
string manipulation (§6.4);
basic UTF-8 support (§6.5);
table manipulation (§6.6);
mathematical functions (§6.7) (sin, log, etc.);
input and output (§6.8);
operating system facilities (§6.9);
debug facilities (§6.10).
Except for the basic and the package libraries, each library provides all its functions as fields of a global table or as methods of its objects.

To have access to these libraries, the C host program should call the luaL_openlibs function, which opens all standard libraries. Alternatively, the host program can open them individually by using luaL_requiref to call luaopen_base (for the basic library), luaopen_package (for the package library), luaopen_coroutine (for the coroutine library), luaopen_string (for the string library), luaopen_utf8 (for the UTF8 library), luaopen_table (for the table library), luaopen_math (for the mathematical library), luaopen_io (for the I/O library), luaopen_os (for the operating system library), and luaopen_debug (for the debug library). These functions are declared in lualib.h.

6.1 – Basic Functions

The basic library provides core functions to Lua. If you do not include this library in your application, you should check carefully whether you need to provide implementations for some of its facilities.

assert (v [, message])

Calls error if the value of its argument v is false (i.e., nil or false); otherwise, returns all its arguments. In case of error, message is the error object; when absent, it defaults to "assertion failed!"

collectgarbage ([opt [, arg]])

This function is a generic interface to the garbage collector. It performs different functions according to its first argument, opt:

"collect": performs a full garbage-collection cycle. This is the default option.
"stop": stops automatic execution of the garbage collector. The collector will run only when explicitly invoked, until a call to restart it.
"restart": restarts automatic execution of the garbage collector.
"count": returns the total memory in use by Lua in Kbytes. The value has a fractional part, so that it multiplied by 1024 gives the exact number of bytes in use by Lua (except for overflows).
"step": performs a garbage-collection step. The step "size" is controlled by arg. With a zero value, the collector will perform one basic (indivisible) step. For non-zero values, the collector will perform as if that amount of memory (in KBytes) had been allocated by Lua. Returns true if the step finished a collection cycle.
"setpause": sets arg as the new value for the pause of the collector (see §2.5). Returns the previous value for pause.
"setstepmul": sets arg as the new value for the step multiplier of the collector (see §2.5). Returns the previous value for step.
"isrunning": returns a boolean that tells whether the collector is running (i.e., not stopped).
dofile ([filename])

Opens the named file and executes its contents as a Lua chunk. When called without arguments, dofile executes the contents of the standard input (stdin). Returns all values returned by the chunk. In case of errors, dofile propagates the error to its caller (that is, dofile does not run in protected mode).
error (message [, level])

Terminates the last protected function called and returns message as the error object. Function error never returns.
Usually, error adds some information about the error position at the beginning of the message, if the message is a string. The level argument specifies how to get the error position. With level 1 (the default), the error position is where the error function was called. Level 2 points the error to where the function that called error was called; and so on. Passing a level 0 avoids the addition of error position information to the message.

_G

A global variable (not a function) that holds the global environment (see §2.2). Lua itself does not use this variable; changing its value does not affect any environment, nor vice versa.
getmetatable (object)

If object does not have a metatable, returns nil. Otherwise, if the object's metatable has a "__metatable" field, returns the associated value. Otherwise, returns the metatable of the given object.

ipairs (t)

Returns three values (an iterator function, the table t, and 0) so that the construction

     for i,v in ipairs(t) do body end
will iterate over the key–value pairs (1,t[1]), (2,t[2]), ..., up to the first nil value.

load (chunk [, chunkname [, mode [, env]]])

Loads a chunk.

If chunk is a string, the chunk is this string. If chunk is a function, load calls it repeatedly to get the chunk pieces. Each call to chunk must return a string that concatenates with previous results. A return of an empty string, nil, or no value signals the end of the chunk.

If there are no syntactic errors, returns the compiled chunk as a function; otherwise, returns nil plus the error message.

If the resulting function has upvalues, the first upvalue is set to the value of env, if that parameter is given, or to the value of the global environment. Other upvalues are initialized with nil. (When you load a main chunk, the resulting function will always have exactly one upvalue, the _ENV variable (see §2.2). However, when you load a binary chunk created from a function (see string.dump), the resulting function can have an arbitrary number of upvalues.) All upvalues are fresh, that is, they are not shared with any other function.

chunkname is used as the name of the chunk for error messages and debug information (see §4.9). When absent, it defaults to chunk, if chunk is a string, or to "=(load)" otherwise.

The string mode controls whether the chunk can be text or binary (that is, a precompiled chunk). It may be the string "b" (only binary chunks), "t" (only text chunks), or "bt" (both binary and text). The default is "bt".

Lua does not check the consistency of binary chunks. Maliciously crafted binary chunks can crash the interpreter.

loadfile ([filename [, mode [, env]]])

Similar to load, but gets the chunk from file filename or from the standard input, if no file name is given.

next (table [, index])

Allows a program to traverse all fields of a table. Its first argument is a table and its second argument is an index in this table. next returns the next index of the table and its associated value. When called with nil as its second argument, next returns an initial index and its associated value. When called with the last index, or with nil in an empty table, next returns nil. If the second argument is absent, then it is interpreted as nil. In particular, you can use next(t) to check whether a table is empty.

The order in which the indices are enumerated is not specified, even for numeric indices. (To traverse a table in numeric order, use a numerical for.)

The behavior of next is undefined if, during the traversal, you assign any value to a non-existent field in the table. You may however modify existing fields. In particular, you may clear existing fields.

pairs (t)

If t has a metamethod __pairs, calls it with t as argument and returns the first three results from the call.

Otherwise, returns three values: the next function, the table t, and nil, so that the construction

     for k,v in pairs(t) do body end
will iterate over all key–value pairs of table t.

See function next for the caveats of modifying the table during its traversal.

pcall (f [, arg1, ···])

Calls function f with the given arguments in protected mode. This means that any error inside f is not propagated; instead, pcall catches the error and returns a status code. Its first result is the status code (a boolean), which is true if the call succeeds without errors. In such case, pcall also returns all results from the call, after this first result. In case of any error, pcall returns false plus the error message.

print (···)

Receives any number of arguments and prints their values to stdout, using the tostring function to convert each argument to a string. print is not intended for formatted output, but only as a quick way to show a value, for instance for debugging. For complete control over the output, use string.format and io.write.
rawequal (v1, v2)

Checks whether v1 is equal to v2, without invoking any metamethod. Returns a boolean.
rawget (table, index)

Gets the real value of table[index], without invoking any metamethod. table must be a table; index may be any value.
rawlen (v)

Returns the length of the object v, which must be a table or a string, without invoking any metamethod. Returns an integer.
rawset (table, index, value)

Sets the real value of table[index] to value, without invoking any metamethod. table must be a table, index any value different from nil and NaN, and value any Lua value.
This function returns table.

select (index, ···)

If index is a number, returns all arguments after argument number index; a negative number indexes from the end (-1 is the last argument). Otherwise, index must be the string "#", and select returns the total number of extra arguments it received.

setmetatable (table, metatable)

Sets the metatable for the given table. (You cannot change the metatable of other types from Lua, only from C.) If metatable is nil, removes the metatable of the given table. If the original metatable has a "__metatable" field, raises an error.

This function returns table.

tonumber (e [, base])

When called with no base, tonumber tries to convert its argument to a number. If the argument is already a number or a string convertible to a number, then tonumber returns this number; otherwise, it returns nil.

The conversion of strings can result in integers or floats, according to the lexical conventions of Lua (see §3.1). (The string may have leading and trailing spaces and a sign.)

When called with base, then e must be a string to be interpreted as an integer numeral in that base. The base may be any integer between 2 and 36, inclusive. In bases above 10, the letter 'A' (in either upper or lower case) represents 10, 'B' represents 11, and so forth, with 'Z' representing 35. If the string e is not a valid numeral in the given base, the function returns nil.

tostring (v)

Receives a value of any type and converts it to a string in a human-readable format. Floats always produce strings with some floating-point indication (either a decimal dot or an exponent). (For complete control of how numbers are converted, use string.format.)
If the metatable of v has a "__tostring" field, then tostring calls the corresponding value with v as argument, and uses the result of the call as its result.

type (v)

Returns the type of its only argument, coded as a string. The possible results of this function are "nil" (a string, not the value nil), "number", "string", "boolean", "table", "function", "thread", and "userdata".
_VERSION

A global variable (not a function) that holds a string containing the current interpreter version. The current value of this variable is "Lua 5.3".
xpcall (f, msgh [, arg1, ···])

This function is similar to pcall, except that it sets a new message handler msgh.

6.2 – Coroutine Manipulation

The operations related to coroutines comprise a sub-library of the basic library and come inside the table coroutine. See §2.6 for a general description of coroutines.

coroutine.create (f)

Creates a new coroutine, with body f. f must be a Lua function. Returns this new coroutine, an object with type "thread".

coroutine.isyieldable ()

Returns true when the running coroutine can yield.

A running coroutine is yieldable if it is not the main thread and it is not inside a non-yieldable C function.

coroutine.resume (co [, val1, ···])

Starts or continues the execution of coroutine co. The first time you resume a coroutine, it starts running its body. The values val1, ... are passed as the arguments to the body function. If the coroutine has yielded, resume restarts it; the values val1, ... are passed as the results from the yield.

If the coroutine runs without any errors, resume returns true plus any values passed to yield (when the coroutine yields) or any values returned by the body function (when the coroutine terminates). If there is any error, resume returns false plus the error message.

coroutine.running ()

Returns the running coroutine plus a boolean, true when the running coroutine is the main one.

coroutine.status (co)

Returns the status of coroutine co, as a string: "running", if the coroutine is running (that is, it called status); "suspended", if the coroutine is suspended in a call to yield, or if it has not started running yet; "normal" if the coroutine is active but not running (that is, it has resumed another coroutine); and "dead" if the coroutine has finished its body function, or if it has stopped with an error.

coroutine.wrap (f)

Creates a new coroutine, with body f. f must be a Lua function. Returns a function that resumes the coroutine each time it is called. Any arguments passed to the function behave as the extra arguments to resume. Returns the same values returned by resume, except the first boolean. In case of error, propagates the error.

coroutine.yield (···)

Suspends the execution of the calling coroutine. Any arguments to yield are passed as extra results to resume.

6.3 – Modules

The package library provides basic facilities for loading modules in Lua. It exports one function directly in the global environment: require. Everything else is exported in a table package.

require (modname)

Loads the given module. The function starts by looking into the package.loaded table to determine whether modname is already loaded. If it is, then require returns the value stored at package.loaded[modname]. Otherwise, it tries to find a loader for the module.

To find a loader, require is guided by the package.searchers sequence. By changing this sequence, we can change how require looks for a module. The following explanation is based on the default configuration for package.searchers.

First require queries package.preload[modname]. If it has a value, this value (which must be a function) is the loader. Otherwise require searches for a Lua loader using the path stored in package.path. If that also fails, it searches for a C loader using the path stored in package.cpath. If that also fails, it tries an all-in-one loader (see package.searchers).

Once a loader is found, require calls the loader with two arguments: modname and an extra value dependent on how it got the loader. (If the loader came from a file, this extra value is the file name.) If the loader returns any non-nil value, require assigns the returned value to package.loaded[modname]. If the loader does not return a non-nil value and has not assigned any value to package.loaded[modname], then require assigns true to this entry. In any case, require returns the final value of package.loaded[modname].

If there is any error loading or running the module, or if it cannot find any loader for the module, then require raises an error.

package.config

A string describing some compile-time configurations for packages. This string is a sequence of lines:

The first line is the directory separator string. Default is '\' for Windows and '/' for all other systems.
The second line is the character that separates templates in a path. Default is ';'.
The third line is the string that marks the substitution points in a template. Default is '?'.
The fourth line is a string that, in a path in Windows, is replaced by the executable's directory. Default is '!'.
The fifth line is a mark to ignore all text after it when building the luaopen_ function name. Default is '-'.
package.cpath

The path used by require to search for a C loader.

Lua initializes the C path package.cpath in the same way it initializes the Lua path package.path, using the environment variable LUA_CPATH_5_3 or the environment variable LUA_CPATH or a default path defined in luaconf.h.

package.loaded

A table used by require to control which modules are already loaded. When you require a module modname and package.loaded[modname] is not false, require simply returns the value stored there.

This variable is only a reference to the real table; assignments to this variable do not change the table used by require.

package.loadlib (libname, funcname)

Dynamically links the host program with the C library libname.

If funcname is "*", then it only links with the library, making the symbols exported by the library available to other dynamically linked libraries. Otherwise, it looks for a function funcname inside the library and returns this function as a C function. So, funcname must follow the lua_CFunction prototype (see lua_CFunction).

This is a low-level function. It completely bypasses the package and module system. Unlike require, it does not perform any path searching and does not automatically adds extensions. libname must be the complete file name of the C library, including if necessary a path and an extension. funcname must be the exact name exported by the C library (which may depend on the C compiler and linker used).

This function is not supported by Standard C. As such, it is only available on some platforms (Windows, Linux, Mac OS X, Solaris, BSD, plus other Unix systems that support the dlfcn standard).

package.path

The path used by require to search for a Lua loader.

At start-up, Lua initializes this variable with the value of the environment variable LUA_PATH_5_3 or the environment variable LUA_PATH or with a default path defined in luaconf.h, if those environment variables are not defined. Any ";;" in the value of the environment variable is replaced by the default path.

package.preload

A table to store loaders for specific modules (see require).

This variable is only a reference to the real table; assignments to this variable do not change the table used by require.

package.searchers

A table used by require to control how to load modules.

Each entry in this table is a searcher function. When looking for a module, require calls each of these searchers in ascending order, with the module name (the argument given to require) as its sole parameter. The function can return another function (the module loader) plus an extra value that will be passed to that loader, or a string explaining why it did not find that module (or nil if it has nothing to say).

Lua initializes this table with four searcher functions.

The first searcher simply looks for a loader in the package.preload table.

The second searcher looks for a loader as a Lua library, using the path stored at package.path. The search is done as described in function package.searchpath.

The third searcher looks for a loader as a C library, using the path given by the variable package.cpath. Again, the search is done as described in function package.searchpath. For instance, if the C path is the string

     "./?.so;./?.dll;/usr/local/?/init.so"
the searcher for module foo will try to open the files ./foo.so, ./foo.dll, and /usr/local/foo/init.so, in that order. Once it finds a C library, this searcher first uses a dynamic link facility to link the application with the library. Then it tries to find a C function inside the library to be used as the loader. The name of this C function is the string "luaopen_" concatenated with a copy of the module name where each dot is replaced by an underscore. Moreover, if the module name has a hyphen, its suffix after (and including) the first hyphen is removed. For instance, if the module name is a.b.c-v2.1, the function name will be luaopen_a_b_c.

The fourth searcher tries an all-in-one loader. It searches the C path for a library for the root name of the given module. For instance, when requiring a.b.c, it will search for a C library for a. If found, it looks into it for an open function for the submodule; in our example, that would be luaopen_a_b_c. With this facility, a package can pack several C submodules into one single library, with each submodule keeping its original open function.

All searchers except the first one (preload) return as the extra value the file name where the module was found, as returned by package.searchpath. The first searcher returns no extra value.

package.searchpath (name, path [, sep [, rep]])

Searches for the given name in the given path.

A path is a string containing a sequence of templates separated by semicolons. For each template, the function replaces each interrogation mark (if any) in the template with a copy of name wherein all occurrences of sep (a dot, by default) were replaced by rep (the system's directory separator, by default), and then tries to open the resulting file name.

For instance, if the path is the string

     "./?.lua;./?.lc;/usr/local/?/init.lua"
the search for the name foo.a will try to open the files ./foo/a.lua, ./foo/a.lc, and /usr/local/foo/a/init.lua, in that order.

Returns the resulting name of the first file that it can open in read mode (after closing the file), or nil plus an error message if none succeeds. (This error message lists all file names it tried to open.)

6.4 – String Manipulation

This library provides generic functions for string manipulation, such as finding and extracting substrings, and pattern matching. When indexing a string in Lua, the first character is at position 1 (not at 0, as in C). Indices are allowed to be negative and are interpreted as indexing backwards, from the end of the string. Thus, the last character is at position -1, and so on.

The string library provides all its functions inside the table string. It also sets a metatable for strings where the __index field points to the string table. Therefore, you can use the string functions in object-oriented style. For instance, string.byte(s,i) can be written as s:byte(i).

The string library assumes one-byte character encodings.

string.byte (s [, i [, j]])

Returns the internal numerical codes of the characters s[i], s[i+1], ..., s[j]. The default value for i is 1; the default value for j is i. These indices are corrected following the same rules of function string.sub.
Numerical codes are not necessarily portable across platforms.

string.char (···)

Receives zero or more integers. Returns a string with length equal to the number of arguments, in which each character has the internal numerical code equal to its corresponding argument.
Numerical codes are not necessarily portable across platforms.

string.dump (function [, strip])

Returns a string containing a binary representation (a binary chunk) of the given function, so that a later load on this string returns a copy of the function (but with new upvalues). If strip is a true value, the binary representation is created without debug information about the function (local variable names, lines, etc.).

Functions with upvalues have only their number of upvalues saved. When (re)loaded, those upvalues receive fresh instances containing nil. (You can use the debug library to serialize and reload the upvalues of a function in a way adequate to your needs.)

string.find (s, pattern [, init [, plain]])

Looks for the first match of pattern (see §6.4.1) in the string s. If it finds a match, then find returns the indices of s where this occurrence starts and ends; otherwise, it returns nil. A third, optional numerical argument init specifies where to start the search; its default value is 1 and can be negative. A value of true as a fourth, optional argument plain turns off the pattern matching facilities, so the function does a plain "find substring" operation, with no characters in pattern being considered magic. Note that if plain is given, then init must be given as well.

If the pattern has captures, then in a successful match the captured values are also returned, after the two indices.

string.format (formatstring, ···)

Returns a formatted version of its variable number of arguments following the description given in its first argument (which must be a string). The format string follows the same rules as the ISO C function sprintf. The only differences are that the options/modifiers *, h, L, l, n, and p are not supported and that there is an extra option, q. The q option formats a string between double quotes, using escape sequences when necessary to ensure that it can safely be read back by the Lua interpreter. For instance, the call

     string.format('%q', 'a string with "quotes" and \n new line')
may produce the string:

     "a string with \"quotes\" and \
      new line"
Options A and a (when available), E, e, f, G, and g all expect a number as argument. Options c, d, i, o, u, X, and x expect an integer. Option q expects a string; option s expects a string without embedded zeros. If the argument to option s is not a string, it is converted to one following the same rules of tostring.

string.gmatch (s, pattern)

Returns an iterator function that, each time it is called, returns the next captures from pattern (see §6.4.1) over the string s. If pattern specifies no captures, then the whole match is produced in each call.
As an example, the following loop will iterate over all the words from string s, printing one per line:

     s = "hello world from Lua"
     for w in string.gmatch(s, "%a+") do
       print(w)
     end
The next example collects all pairs key=value from the given string into a table:

     t = {}
     s = "from=world, to=Lua"
     for k, v in string.gmatch(s, "(%w+)=(%w+)") do
       t[k] = v
     end
For this function, a caret '^' at the start of a pattern does not work as an anchor, as this would prevent the iteration.

string.gsub (s, pattern, repl [, n])

Returns a copy of s in which all (or the first n, if given) occurrences of the pattern (see §6.4.1) have been replaced by a replacement string specified by repl, which can be a string, a table, or a function. gsub also returns, as its second value, the total number of matches that occurred. The name gsub comes from Global SUBstitution.
If repl is a string, then its value is used for replacement. The character % works as an escape character: any sequence in repl of the form %d, with d between 1 and 9, stands for the value of the d-th captured substring. The sequence %0 stands for the whole match. The sequence %% stands for a single %.

If repl is a table, then the table is queried for every match, using the first capture as the key.

If repl is a function, then this function is called every time a match occurs, with all captured substrings passed as arguments, in order.

In any case, if the pattern specifies no captures, then it behaves as if the whole pattern was inside a capture.

If the value returned by the table query or by the function call is a string or a number, then it is used as the replacement string; otherwise, if it is false or nil, then there is no replacement (that is, the original match is kept in the string).

Here are some examples:

     x = string.gsub("hello world", "(%w+)", "%1 %1")
     --> x="hello hello world world"
     
     x = string.gsub("hello world", "%w+", "%0 %0", 1)
     --> x="hello hello world"
     
     x = string.gsub("hello world from Lua", "(%w+)%s*(%w+)", "%2 %1")
     --> x="world hello Lua from"
     
     x = string.gsub("home = $HOME, user = $USER", "%$(%w+)", os.getenv)
     --> x="home = /home/roberto, user = roberto"
     
     x = string.gsub("4+5 = $return 4+5$", "%$(.-)%$", function (s)
           return load(s)()
         end)
     --> x="4+5 = 9"
     
     local t = {name="lua", version="5.3"}
     x = string.gsub("$name-$version.tar.gz", "%$(%w+)", t)
     --> x="lua-5.3.tar.gz"
string.len (s)

Receives a string and returns its length. The empty string "" has length 0. Embedded zeros are counted, so "a\000bc\000" has length 5.
string.lower (s)

Receives a string and returns a copy of this string with all uppercase letters changed to lowercase. All other characters are left unchanged. The definition of what an uppercase letter is depends on the current locale.
string.match (s, pattern [, init])

Looks for the first match of pattern (see §6.4.1) in the string s. If it finds one, then match returns the captures from the pattern; otherwise it returns nil. If pattern specifies no captures, then the whole match is returned. A third, optional numerical argument init specifies where to start the search; its default value is 1 and can be negative.
string.pack (fmt, v1, v2, ···)

Returns a binary string containing the values v1, v2, etc. packed (that is, serialized in binary form) according to the format string fmt (see §6.4.2).

string.packsize (fmt)

Returns the size of a string resulting from string.pack with the given format. The format string cannot have the variable-length options 's' or 'z' (see §6.4.2).

string.rep (s, n [, sep])

Returns a string that is the concatenation of n copies of the string s separated by the string sep. The default value for sep is the empty string (that is, no separator). Returns the empty string if n is not positive.
string.reverse (s)

Returns a string that is the string s reversed.
string.sub (s, i [, j])

Returns the substring of s that starts at i and continues until j; i and j can be negative. If j is absent, then it is assumed to be equal to -1 (which is the same as the string length). In particular, the call string.sub(s,1,j) returns a prefix of s with length j, and string.sub(s, -i) returns a suffix of s with length i.
If, after the translation of negative indices, i is less than 1, it is corrected to 1. If j is greater than the string length, it is corrected to that length. If, after these corrections, i is greater than j, the function returns the empty string.

string.unpack (fmt, s [, pos])

Returns the values packed in string s (see string.pack) according to the format string fmt (see §6.4.2). An optional pos marks where to start reading in s (default is 1). After the read values, this function also returns the index of the first unread byte in s.

string.upper (s)

Receives a string and returns a copy of this string with all lowercase letters changed to uppercase. All other characters are left unchanged. The definition of what a lowercase letter is depends on the current locale.
6.4.1 – Patterns

Patterns in Lua are described by regular strings, which are interpreted as patterns by the pattern-matching functions string.find, string.gmatch, string.gsub, and string.match. This section describes the syntax and the meaning (that is, what they match) of these strings.

Character Class:

A character class is used to represent a set of characters. The following combinations are allowed in describing a character class:

x: (where x is not one of the magic characters ^$()%.[]*+-?) represents the character x itself.
.: (a dot) represents all characters.
%a: represents all letters.
%c: represents all control characters.
%d: represents all digits.
%g: represents all printable characters except space.
%l: represents all lowercase letters.
%p: represents all punctuation characters.
%s: represents all space characters.
%u: represents all uppercase letters.
%w: represents all alphanumeric characters.
%x: represents all hexadecimal digits.
%x: (where x is any non-alphanumeric character) represents the character x. This is the standard way to escape the magic characters. Any non-alphanumeric character (including all punctuations, even the non-magical) can be preceded by a '%' when used to represent itself in a pattern.
[set]: represents the class which is the union of all characters in set. A range of characters can be specified by separating the end characters of the range, in ascending order, with a '-'. All classes %x described above can also be used as components in set. All other characters in set represent themselves. For example, [%w_] (or [_%w]) represents all alphanumeric characters plus the underscore, [0-7] represents the octal digits, and [0-7%l%-] represents the octal digits plus the lowercase letters plus the '-' character.
The interaction between ranges and classes is not defined. Therefore, patterns like [%a-z] or [a-%%] have no meaning.

[^set]: represents the complement of set, where set is interpreted as above.
For all classes represented by single letters (%a, %c, etc.), the corresponding uppercase letter represents the complement of the class. For instance, %S represents all non-space characters.

The definitions of letter, space, and other character groups depend on the current locale. In particular, the class [a-z] may not be equivalent to %l.

Pattern Item:

A pattern item can be

a single character class, which matches any single character in the class;
a single character class followed by '*', which matches zero or more repetitions of characters in the class. These repetition items will always match the longest possible sequence;
a single character class followed by '+', which matches one or more repetitions of characters in the class. These repetition items will always match the longest possible sequence;
a single character class followed by '-', which also matches zero or more repetitions of characters in the class. Unlike '*', these repetition items will always match the shortest possible sequence;
a single character class followed by '?', which matches zero or one occurrence of a character in the class. It always matches one occurrence if possible;
%n, for n between 1 and 9; such item matches a substring equal to the n-th captured string (see below);
%bxy, where x and y are two distinct characters; such item matches strings that start with x, end with y, and where the x and y are balanced. This means that, if one reads the string from left to right, counting +1 for an x and -1 for a y, the ending y is the first y where the count reaches 0. For instance, the item %b() matches expressions with balanced parentheses.
%f[set], a frontier pattern; such item matches an empty string at any position such that the next character belongs to set and the previous character does not belong to set. The set set is interpreted as previously described. The beginning and the end of the subject are handled as if they were the character '\0'.
Pattern:

A pattern is a sequence of pattern items. A caret '^' at the beginning of a pattern anchors the match at the beginning of the subject string. A '$' at the end of a pattern anchors the match at the end of the subject string. At other positions, '^' and '$' have no special meaning and represent themselves.

Captures:

A pattern can contain sub-patterns enclosed in parentheses; they describe captures. When a match succeeds, the substrings of the subject string that match captures are stored (captured) for future use. Captures are numbered according to their left parentheses. For instance, in the pattern "(a*(.)%w(%s*))", the part of the string matching "a*(.)%w(%s*)" is stored as the first capture (and therefore has number 1); the character matching "." is captured with number 2, and the part matching "%s*" has number 3.

As a special case, the empty capture () captures the current string position (a number). For instance, if we apply the pattern "()aa()" on the string "flaaap", there will be two captures: 3 and 5.

6.4.2 – Format Strings for Pack and Unpack

The first argument to string.pack, string.packsize, and string.unpack is a format string, which describes the layout of the structure being created or read.

A format string is a sequence of conversion options. The conversion options are as follows:

<: sets little endian
>: sets big endian
=: sets native endian
![n]: sets maximum alignment to n (default is native alignment)
b: a signed byte (char)
B: an unsigned byte (char)
h: a signed short (native size)
H: an unsigned short (native size)
l: a signed long (native size)
L: an unsigned long (native size)
j: a lua_Integer
J: a lua_Unsigned
T: a size_t (native size)
i[n]: a signed int with n bytes (default is native size)
I[n]: an unsigned int with n bytes (default is native size)
f: a float (native size)
d: a double (native size)
n: a lua_Number
cn: a fixed-sized string with n bytes
z: a zero-terminated string
s[n]: a string preceded by its length coded as an unsigned integer with n bytes (default is a size_t)
x: one byte of padding
Xop: an empty item that aligns according to option op (which is otherwise ignored)
' ': (empty space) ignored
(A "[n]" means an optional integral numeral.) Except for padding, spaces, and configurations (options "xX <=>!"), each option corresponds to an argument (in string.pack) or a result (in string.unpack).

For options "!n", "sn", "in", and "In", n can be any integer between 1 and 16. All integral options check overflows; string.pack checks whether the given value fits in the given size; string.unpack checks whether the read value fits in a Lua integer.

Any format string starts as if prefixed by "!1=", that is, with maximum alignment of 1 (no alignment) and native endianness.

Alignment works as follows: For each option, the format gets extra padding until the data starts at an offset that is a multiple of the minimum between the option size and the maximum alignment; this minimum must be a power of 2. Options "c" and "z" are not aligned; option "s" follows the alignment of its starting integer.

All padding is filled with zeros by string.pack (and ignored by string.unpack).

6.5 – UTF-8 Support

This library provides basic support for UTF-8 encoding. It provides all its functions inside the table utf8. This library does not provide any support for Unicode other than the handling of the encoding. Any operation that needs the meaning of a character, such as character classification, is outside its scope.

Unless stated otherwise, all functions that expect a byte position as a parameter assume that the given position is either the start of a byte sequence or one plus the length of the subject string. As in the string library, negative indices count from the end of the string.

utf8.char (···)

Receives zero or more integers, converts each one to its corresponding UTF-8 byte sequence and returns a string with the concatenation of all these sequences.
utf8.charpattern

The pattern (a string, not a function) "[\0-\x7F\xC2-\xF4][\x80-\xBF]*" (see §6.4.1), which matches exactly one UTF-8 byte sequence, assuming that the subject is a valid UTF-8 string.
utf8.codes (s)

Returns values so that the construction

     for p, c in utf8.codes(s) do body end
will iterate over all characters in string s, with p being the position (in bytes) and c the code point of each character. It raises an error if it meets any invalid byte sequence.

utf8.codepoint (s [, i [, j]])

Returns the codepoints (as integers) from all characters in s that start between byte position i and j (both included). The default for i is 1 and for j is i. It raises an error if it meets any invalid byte sequence.
utf8.len (s [, i [, j]])

Returns the number of UTF-8 characters in string s that start between positions i and j (both inclusive). The default for i is 1 and for j is -1. If it finds any invalid byte sequence, returns a false value plus the position of the first invalid byte.
utf8.offset (s, n [, i])

Returns the position (in bytes) where the encoding of the n-th character of s (counting from position i) starts. A negative n gets characters before position i. The default for i is 1 when n is non-negative and #s + 1 otherwise, so that utf8.offset(s, -n) gets the offset of the n-th character from the end of the string. If the specified character is neither in the subject nor right after its end, the function returns nil.
As a special case, when n is 0 the function returns the start of the encoding of the character that contains the i-th byte of s.

This function assumes that s is a valid UTF-8 string.

6.6 – Table Manipulation

This library provides generic functions for table manipulation. It provides all its functions inside the table table.

Remember that, whenever an operation needs the length of a table, the table must be a proper sequence or have a __len metamethod (see §3.4.7). All functions ignore non-numeric keys in the tables given as arguments.

table.concat (list [, sep [, i [, j]]])

Given a list where all elements are strings or numbers, returns the string list[i]..sep..list[i+1] ··· sep..list[j]. The default value for sep is the empty string, the default for i is 1, and the default for j is #list. If i is greater than j, returns the empty string.

table.insert (list, [pos,] value)

Inserts element value at position pos in list, shifting up the elements list[pos], list[pos+1], ···, list[#list]. The default value for pos is #list+1, so that a call table.insert(t,x) inserts x at the end of list t.

table.move (a1, f, e, t [,a2])

Moves elements from table a1 to table a2. This function performs the equivalent to the following multiple assignment: a2[t],··· = a1[f],···,a1[e]. The default for a2 is a1. The destination range can overlap with the source range. Index f must be positive.

table.pack (···)

Returns a new table with all parameters stored into keys 1, 2, etc. and with a field "n" with the total number of parameters. Note that the resulting table may not be a sequence.

table.remove (list [, pos])

Removes from list the element at position pos, returning the value of the removed element. When pos is an integer between 1 and #list, it shifts down the elements list[pos+1], list[pos+2], ···, list[#list] and erases element list[#list]; The index pos can also be 0 when #list is 0, or #list + 1; in those cases, the function erases the element list[pos].

The default value for pos is #list, so that a call table.remove(l) removes the last element of list l.

table.sort (list [, comp])

Sorts list elements in a given order, in-place, from list[1] to list[#list]. If comp is given, then it must be a function that receives two list elements and returns true when the first element must come before the second in the final order (so that not comp(list[i+1],list[i]) will be true after the sort). If comp is not given, then the standard Lua operator < is used instead.

The sort algorithm is not stable; that is, elements considered equal by the given order may have their relative positions changed by the sort.

table.unpack (list [, i [, j]])

Returns the elements from the given list. This function is equivalent to

     return list[i], list[i+1], ···, list[j]
By default, i is 1 and j is #list.

6.7 – Mathematical Functions

This library provides basic mathematical functions. It provides all its functions and constants inside the table math. Functions with the annotation "integer/float" give integer results for integer arguments and float results for float (or mixed) arguments. Rounding functions (math.ceil, math.floor, and math.modf) return an integer when the result fits in the range of an integer, or a float otherwise.

math.abs (x)

Returns the absolute value of x. (integer/float)

math.acos (x)

Returns the arc cosine of x (in radians).

math.asin (x)

Returns the arc sine of x (in radians).

math.atan (y [, x])

Returns the arc tangent of y/x (in radians), but uses the signs of both parameters to find the quadrant of the result. (It also handles correctly the case of x being zero.)

The default value for x is 1, so that the call math.atan(y) returns the arc tangent of y.

math.ceil (x)

Returns the smallest integral value larger than or equal to x.

math.cos (x)

Returns the cosine of x (assumed to be in radians).

math.deg (x)

Converts the angle x from radians to degrees.

math.exp (x)

Returns the value ex (where e is the base of natural logarithms).

math.floor (x)

Returns the largest integral value smaller than or equal to x.

math.fmod (x, y)

Returns the remainder of the division of x by y that rounds the quotient towards zero. (integer/float)

math.huge

The float value HUGE_VAL, a value larger than any other numerical value.

math.log (x [, base])

Returns the logarithm of x in the given base. The default for base is e (so that the function returns the natural logarithm of x).

math.max (x, ···)

Returns the argument with the maximum value, according to the Lua operator <. (integer/float)

math.maxinteger

An integer with the maximum value for an integer.
math.min (x, ···)

Returns the argument with the minimum value, according to the Lua operator <. (integer/float)

math.mininteger

An integer with the minimum value for an integer.
math.modf (x)

Returns the integral part of x and the fractional part of x. Its second result is always a float.

math.pi

The value of π.

math.rad (x)

Converts the angle x from degrees to radians.

math.random ([m [, n]])

When called without arguments, returns a pseudo-random float with uniform distribution in the range [0,1). When called with two integers m and n, math.random returns a pseudo-random integer with uniform distribution in the range [m, n]. (The value m-n cannot be negative and must fit in a Lua integer.) The call math.random(n) is equivalent to math.random(1,n).

This function is an interface to the underling pseudo-random generator function provided by C. No guarantees can be given for its statistical properties.

math.randomseed (x)

Sets x as the "seed" for the pseudo-random generator: equal seeds produce equal sequences of numbers.

math.sin (x)

Returns the sine of x (assumed to be in radians).

math.sqrt (x)

Returns the square root of x. (You can also use the expression x^0.5 to compute this value.)

math.tan (x)

Returns the tangent of x (assumed to be in radians).

math.tointeger (x)

If the value x is convertible to an integer, returns that integer. Otherwise, returns nil.

math.type (x)

Returns "integer" if x is an integer, "float" if it is a float, or nil if x is not a number.

math.ult (m, n)

Returns a boolean, true if integer m is below integer n when they are compared as unsigned integers.

6.8 – Input and Output Facilities

The I/O library provides two different styles for file manipulation. The first one uses implicit file handles; that is, there are operations to set a default input file and a default output file, and all input/output operations are over these default files. The second style uses explicit file handles.

When using implicit file handles, all operations are supplied by table io. When using explicit file handles, the operation io.open returns a file handle and then all operations are supplied as methods of the file handle.

The table io also provides three predefined file handles with their usual meanings from C: io.stdin, io.stdout, and io.stderr. The I/O library never closes these files.

Unless otherwise stated, all I/O functions return nil on failure (plus an error message as a second result and a system-dependent error code as a third result) and some value different from nil on success. On non-POSIX systems, the computation of the error message and error code in case of errors may be not thread safe, because they rely on the global C variable errno.

io.close ([file])

Equivalent to file:close(). Without a file, closes the default output file.

io.flush ()

Equivalent to io.output():flush().

io.input ([file])

When called with a file name, it opens the named file (in text mode), and sets its handle as the default input file. When called with a file handle, it simply sets this file handle as the default input file. When called without parameters, it returns the current default input file.

In case of errors this function raises the error, instead of returning an error code.

io.lines ([filename ···])

Opens the given file name in read mode and returns an iterator function that works like file:lines(···) over the opened file. When the iterator function detects the end of file, it returns no values (to finish the loop) and automatically closes the file.

The call io.lines() (with no file name) is equivalent to io.input():lines("*l"); that is, it iterates over the lines of the default input file. In this case it does not close the file when the loop ends.

In case of errors this function raises the error, instead of returning an error code.

io.open (filename [, mode])

This function opens a file, in the mode specified in the string mode. It returns a new file handle, or, in case of errors, nil plus an error message.

The mode string can be any of the following:

"r": read mode (the default);
"w": write mode;
"a": append mode;
"r+": update mode, all previous data is preserved;
"w+": update mode, all previous data is erased;
"a+": append update mode, previous data is preserved, writing is only allowed at the end of file.
The mode string can also have a 'b' at the end, which is needed in some systems to open the file in binary mode.

io.output ([file])

Similar to io.input, but operates over the default output file.

io.popen (prog [, mode])

This function is system dependent and is not available on all platforms.

Starts program prog in a separated process and returns a file handle that you can use to read data from this program (if mode is "r", the default) or to write data to this program (if mode is "w").

io.read (···)

Equivalent to io.input():read(···).

io.tmpfile ()

Returns a handle for a temporary file. This file is opened in update mode and it is automatically removed when the program ends.

io.type (obj)

Checks whether obj is a valid file handle. Returns the string "file" if obj is an open file handle, "closed file" if obj is a closed file handle, or nil if obj is not a file handle.

io.write (···)

Equivalent to io.output():write(···).

file:close ()

Closes file. Note that files are automatically closed when their handles are garbage collected, but that takes an unpredictable amount of time to happen.

When closing a file handle created with io.popen, file:close returns the same values returned by os.execute.

file:flush ()

Saves any written data to file.

file:lines (···)

Returns an iterator function that, each time it is called, reads the file according to the given formats. When no format is given, uses "l" as a default. As an example, the construction

     for c in file:lines(1) do body end
will iterate over all characters of the file, starting at the current position. Unlike io.lines, this function does not close the file when the loop ends.

In case of errors this function raises the error, instead of returning an error code.

file:read (···)

Reads the file file, according to the given formats, which specify what to read. For each format, the function returns a string or a number with the characters read, or nil if it cannot read data with the specified format. (In this latter case, the function does not read subsequent formats.) When called without formats, it uses a default format that reads the next line (see below).

The available formats are

"n": reads a numeral and returns it as a float or an integer, following the lexical conventions of Lua. (The numeral may have leading spaces and a sign.) This format always reads the longest input sequence that is a valid prefix for a number; if that prefix does not form a valid number (e.g., an empty string, "0x", or "3.4e-"), it is discarded and the function returns nil.
"i": reads an integral number and returns it as an integer.
"a": reads the whole file, starting at the current position. On end of file, it returns the empty string.
"l": reads the next line skipping the end of line, returning nil on end of file. This is the default format.
"L": reads the next line keeping the end-of-line character (if present), returning nil on end of file.
number: reads a string with up to this number of bytes, returning nil on end of file. If number is zero, it reads nothing and returns an empty string, or nil on end of file.
The formats "l" and "L" should be used only for text files.

file:seek ([whence [, offset]])

Sets and gets the file position, measured from the beginning of the file, to the position given by offset plus a base specified by the string whence, as follows:

"set": base is position 0 (beginning of the file);
"cur": base is current position;
"end": base is end of file;
In case of success, seek returns the final file position, measured in bytes from the beginning of the file. If seek fails, it returns nil, plus a string describing the error.

The default value for whence is "cur", and for offset is 0. Therefore, the call file:seek() returns the current file position, without changing it; the call file:seek("set") sets the position to the beginning of the file (and returns 0); and the call file:seek("end") sets the position to the end of the file, and returns its size.

file:setvbuf (mode [, size])

Sets the buffering mode for an output file. There are three available modes:

"no": no buffering; the result of any output operation appears immediately.
"full": full buffering; output operation is performed only when the buffer is full or when you explicitly flush the file (see io.flush).
"line": line buffering; output is buffered until a newline is output or there is any input from some special files (such as a terminal device).
For the last two cases, size specifies the size of the buffer, in bytes. The default is an appropriate size.

file:write (···)

Writes the value of each of its arguments to file. The arguments must be strings or numbers.

In case of success, this function returns file. Otherwise it returns nil plus a string describing the error.

6.9 – Operating System Facilities

This library is implemented through table os.

os.clock ()

Returns an approximation of the amount in seconds of CPU time used by the program.

os.date ([format [, time]])

Returns a string or a table containing date and time, formatted according to the given string format.

If the time argument is present, this is the time to be formatted (see the os.time function for a description of this value). Otherwise, date formats the current time.

If format starts with '!', then the date is formatted in Coordinated Universal Time. After this optional character, if format is the string "*t", then date returns a table with the following fields: year (four digits), month (1–12), day (1–31), hour (0–23), min (0–59), sec (0–61), wday (weekday, Sunday is 1), yday (day of the year), and isdst (daylight saving flag, a boolean). This last field may be absent if the information is not available.

If format is not "*t", then date returns the date as a string, formatted according to the same rules as the ISO C function strftime.

When called without arguments, date returns a reasonable date and time representation that depends on the host system and on the current locale (that is, os.date() is equivalent to os.date("%c")).

On non-POSIX systems, this function may be not thread safe because of its reliance on C function gmtime and C function localtime.

os.difftime (t2, t1)

Returns the difference, in seconds, from time t1 to time t2 (where the times are values returned by os.time). In POSIX, Windows, and some other systems, this value is exactly t2-t1.

os.execute ([command])

This function is equivalent to the ISO C function system. It passes command to be executed by an operating system shell. Its first result is true if the command terminated successfully, or nil otherwise. After this first result the function returns a string plus a number, as follows:

"exit": the command terminated normally; the following number is the exit status of the command.
"signal": the command was terminated by a signal; the following number is the signal that terminated the command.
When called without a command, os.execute returns a boolean that is true if a shell is available.

os.exit ([code [, close]])

Calls the ISO C function exit to terminate the host program. If code is true, the returned status is EXIT_SUCCESS; if code is false, the returned status is EXIT_FAILURE; if code is a number, the returned status is this number. The default value for code is true.

If the optional second argument close is true, closes the Lua state before exiting.

os.getenv (varname)

Returns the value of the process environment variable varname, or nil if the variable is not defined.

os.remove (filename)

Deletes the file (or empty directory, on POSIX systems) with the given name. If this function fails, it returns nil, plus a string describing the error and the error code.

os.rename (oldname, newname)

Renames file or directory named oldname to newname. If this function fails, it returns nil, plus a string describing the error and the error code.

os.setlocale (locale [, category])

Sets the current locale of the program. locale is a system-dependent string specifying a locale; category is an optional string describing which category to change: "all", "collate", "ctype", "monetary", "numeric", or "time"; the default category is "all". The function returns the name of the new locale, or nil if the request cannot be honored.

If locale is the empty string, the current locale is set to an implementation-defined native locale. If locale is the string "C", the current locale is set to the standard C locale.

When called with nil as the first argument, this function only returns the name of the current locale for the given category.

This function may be not thread safe because of its reliance on C function setlocale.

os.time ([table])

Returns the current time when called without arguments, or a time representing the date and time specified by the given table. This table must have fields year, month, and day, and may have fields hour (default is 12), min (default is 0), sec (default is 0), and isdst (default is nil). For a description of these fields, see the os.date function.

The returned value is a number, whose meaning depends on your system. In POSIX, Windows, and some other systems, this number counts the number of seconds since some given start time (the "epoch"). In other systems, the meaning is not specified, and the number returned by time can be used only as an argument to os.date and os.difftime.

os.tmpname ()

Returns a string with a file name that can be used for a temporary file. The file must be explicitly opened before its use and explicitly removed when no longer needed.

On POSIX systems, this function also creates a file with that name, to avoid security risks. (Someone else might create the file with wrong permissions in the time between getting the name and creating the file.) You still have to open the file to use it and to remove it (even if you do not use it).

When possible, you may prefer to use io.tmpfile, which automatically removes the file when the program ends.

6.10 – The Debug Library

This library provides the functionality of the debug interface (§4.9) to Lua programs. You should exert care when using this library. Several of its functions violate basic assumptions about Lua code (e.g., that variables local to a function cannot be accessed from outside; that userdata metatables cannot be changed by Lua code; that Lua programs do not crash) and therefore can compromise otherwise secure code. Moreover, some functions in this library may be slow.

All functions in this library are provided inside the debug table. All functions that operate over a thread have an optional first argument which is the thread to operate over. The default is always the current thread.

debug.debug ()

Enters an interactive mode with the user, running each string that the user enters. Using simple commands and other debug facilities, the user can inspect global and local variables, change their values, evaluate expressions, and so on. A line containing only the word cont finishes this function, so that the caller continues its execution.

Note that commands for debug.debug are not lexically nested within any function and so have no direct access to local variables.

debug.gethook ([thread])

Returns the current hook settings of the thread, as three values: the current hook function, the current hook mask, and the current hook count (as set by the debug.sethook function).

debug.getinfo ([thread,] f [, what])

Returns a table with information about a function. You can give the function directly or you can give a number as the value of f, which means the function running at level f of the call stack of the given thread: level 0 is the current function (getinfo itself); level 1 is the function that called getinfo (except for tail calls, which do not count on the stack); and so on. If f is a number larger than the number of active functions, then getinfo returns nil.

The returned table can contain all the fields returned by lua_getinfo, with the string what describing which fields to fill in. The default for what is to get all information available, except the table of valid lines. If present, the option 'f' adds a field named func with the function itself. If present, the option 'L' adds a field named activelines with the table of valid lines.

For instance, the expression debug.getinfo(1,"n").name returns a table with a name for the current function, if a reasonable name can be found, and the expression debug.getinfo(print) returns a table with all available information about the print function.

debug.getlocal ([thread,] f, local)

This function returns the name and the value of the local variable with index local of the function at level f of the stack. This function accesses not only explicit local variables, but also parameters, temporaries, etc.

The first parameter or local variable has index 1, and so on, following the order that they are declared in the code, counting only the variables that are active in the current scope of the function. Negative indices refer to vararg parameters; -1 is the first vararg parameter. The function returns nil if there is no variable with the given index, and raises an error when called with a level out of range. (You can call debug.getinfo to check whether the level is valid.)

Variable names starting with '(' (open parenthesis) represent variables with no known names (internal variables such as loop control variables, and variables from chunks saved without debug information).

The parameter f may also be a function. In that case, getlocal returns only the name of function parameters.

debug.getmetatable (value)

Returns the metatable of the given value or nil if it does not have a metatable.

debug.getregistry ()

Returns the registry table (see §4.5).

debug.getupvalue (f, up)

This function returns the name and the value of the upvalue with index up of the function f. The function returns nil if there is no upvalue with the given index.

Variable names starting with '(' (open parenthesis) represent variables with no known names (variables from chunks saved without debug information).

debug.getuservalue (u)

Returns the Lua value associated to u. If u is not a userdata, returns nil.

debug.sethook ([thread,] hook, mask [, count])

Sets the given function as a hook. The string mask and the number count describe when the hook will be called. The string mask may have any combination of the following characters, with the given meaning:

'c': the hook is called every time Lua calls a function;
'r': the hook is called every time Lua returns from a function;
'l': the hook is called every time Lua enters a new line of code.
Moreover, with a count different from zero, the hook is called also after every count instructions.

When called without arguments, debug.sethook turns off the hook.

When the hook is called, its first parameter is a string describing the event that has triggered its call: "call" (or "tail call"), "return", "line", and "count". For line events, the hook also gets the new line number as its second parameter. Inside a hook, you can call getinfo with level 2 to get more information about the running function (level 0 is the getinfo function, and level 1 is the hook function).

debug.setlocal ([thread,] level, local, value)

This function assigns the value value to the local variable with index local of the function at level level of the stack. The function returns nil if there is no local variable with the given index, and raises an error when called with a level out of range. (You can call getinfo to check whether the level is valid.) Otherwise, it returns the name of the local variable.

See debug.getlocal for more information about variable indices and names.

debug.setmetatable (value, table)

Sets the metatable for the given value to the given table (which can be nil). Returns value.

debug.setupvalue (f, up, value)

This function assigns the value value to the upvalue with index up of the function f. The function returns nil if there is no upvalue with the given index. Otherwise, it returns the name of the upvalue.

debug.setuservalue (udata, value)

Sets the given value as the Lua value associated to the given udata. udata must be a full userdata.

Returns udata.

debug.traceback ([thread,] [message [, level]])

If message is present but is neither a string nor nil, this function returns message without further processing. Otherwise, it returns a string with a traceback of the call stack. The optional message string is appended at the beginning of the traceback. An optional level number tells at which level to start the traceback (default is 1, the function calling traceback).

debug.upvalueid (f, n)

Returns a unique identifier (as a light userdata) for the upvalue numbered n from the given function.

These unique identifiers allow a program to check whether different closures share upvalues. Lua closures that share an upvalue (that is, that access a same external local variable) will return identical ids for those upvalue indices.

debug.upvaluejoin (f1, n1, f2, n2)

Make the n1-th upvalue of the Lua closure f1 refer to the n2-th upvalue of the Lua closure f2.

#7 – Lua Standalone

Although Lua has been designed as an extension language, to be embedded in a host C program, it is also frequently used as a standalone language. An interpreter for Lua as a standalone language, called simply lua, is provided with the standard distribution. The standalone interpreter includes all standard libraries, including the debug library. Its usage is:

     lua [options] [script [args]]
The options are:

-e stat: executes string stat;
-l mod: "requires" mod;
-i: enters interactive mode after running script;
-v: prints version information;
-E: ignores environment variables;
--: stops handling options;
-: executes stdin as a file and stops handling options.
After handling its options, lua runs the given script. When called without arguments, lua behaves as lua -v -i when the standard input (stdin) is a terminal, and as lua - otherwise.

When called without option -E, the interpreter checks for an environment variable LUA_INIT_5_3 (or LUA_INIT if the versioned name is not defined) before running any argument. If the variable content has the format @filename, then lua executes the file. Otherwise, lua executes the string itself.

When called with option -E, besides ignoring LUA_INIT, Lua also ignores the values of LUA_PATH and LUA_CPATH, setting the values of package.path and package.cpath with the default paths defined in luaconf.h.

All options are handled in order, except -i and -E. For instance, an invocation like

     $ lua -e'a=1' -e 'print(a)' script.lua
will first set a to 1, then print the value of a, and finally run the file script.lua with no arguments. (Here $ is the shell prompt. Your prompt may be different.)

Before running any code, lua collects all command-line arguments in a global table called arg. The script name goes to index 0, the first argument after the script name goes to index 1, and so on. Any arguments before the script name (that is, the interpreter name plus its options) go to negative indices. For instance, in the call

     $ lua -la b.lua t1 t2
the table is like this:

     arg = { [-2] = "lua", [-1] = "-la",
             [0] = "b.lua",
             [1] = "t1", [2] = "t2" }
If there is no script in the call, the interpreter name goes to index 0, followed by the other arguments. For instance, the call

     $ lua -e "print(arg[1])"
will print "-e". If there is a script, the script is called with parameters arg[1], ···, arg[#arg]. (Like all chunks in Lua, the script is compiled as a vararg function.)

In interactive mode, Lua repeatedly prompts and waits for a line. After reading a line, Lua first try to interpret the line as an expression. If it succeeds, it prints its value. Otherwise, it interprets the line as a statement. If you write an incomplete statement, the interpreter waits for its completion by issuing a different prompt.

In case of unprotected errors in the script, the interpreter reports the error to the standard error stream. If the error object is not a string but has a metamethod __tostring, the interpreter calls this metamethod to produce the final message. Otherwise, the interpreter converts the error object to a string and adds a stack traceback to it.

When finishing normally, the interpreter closes its main Lua state (see lua_close). The script can avoid this step by calling os.exit to terminate.

To allow the use of Lua as a script interpreter in Unix systems, the standalone interpreter skips the first line of a chunk if it starts with #. Therefore, Lua scripts can be made into executable programs by using chmod +x and the #! form, as in

     #!/usr/local/bin/lua
(Of course, the location of the Lua interpreter may be different in your machine. If lua is in your PATH, then

     #!/usr/bin/env lua
is a more portable solution.)

#8 – Incompatibilities with the Previous Version

Here we list the incompatibilities that you may find when moving a program from Lua 5.2 to Lua 5.3. You can avoid some incompatibilities by compiling Lua with appropriate options (see file luaconf.h). However, all these compatibility options will be removed in the future.

Lua versions can always change the C API in ways that do not imply source-code changes in a program, such as the numeric values for constants or the implementation of functions as macros. Therefore, you should not assume that binaries are compatible between different Lua versions. Always recompile clients of the Lua API when using a new version.

Similarly, Lua versions can always change the internal representation of precompiled chunks; precompiled chunks are not compatible between different Lua versions.

The standard paths in the official distribution may change between versions.

8.1 – Changes in the Language

The main difference between Lua 5.2 and Lua 5.3 is the introduction of an integer subtype for numbers. Although this change should not affect "normal" computations, some computations (mainly those that involve some kind of overflow) can give different results.
You can fix these differences by forcing a number to be a float (in Lua 5.2 all numbers were float), in particular writing constants with an ending .0 or using x = x + 0.0 to convert a variable. (This recommendation is only for a quick fix for an occasional incompatibility; it is not a general guideline for good programming. For good programming, use floats where you need floats and integers where you need integers.)

The conversion of a float to a string now adds a .0 suffix to the result if it looks like an integer. (For instance, the float 2.0 will be printed as 2.0, not as 2.) You should always use an explicit format when you need a specific format for numbers.
(Formally this is not an incompatibility, because Lua does not specify how numbers are formatted as strings, but some programs assumed a specific format.)

The generational mode for the garbage collector was removed. (It was an experimental feature in Lua 5.2.)
8.2 – Changes in the Libraries

The bit32 library has been deprecated. It is easy to require a compatible external library or, better yet, to replace its functions with appropriate bitwise operations. (Keep in mind that bit32 operates on 32-bit integers, while the bitwise operators in standard Lua operate on 64-bit integers.)
The Table library now respects metamethods for setting and getting elements.
The ipairs iterator now respects metamethods and its __ipairs metamethod has been deprecated.
Option names in io.read do not have a starting '*' anymore. For compatibility, Lua will continue to ignore this character.
The following functions were deprecated in the mathematical library: atan2, cosh, sinh, tanh, pow, frexp, and ldexp. You can replace math.pow(x,y) with x^y; you can replace math.atan2 with math.atan, which now accepts one or two parameters; you can replace math.ldexp(x,exp) with x * 2.0^exp. For the other operations, you can either use an external library or implement them in Lua.
The searcher for C loaders used by require changed the way it handles versioned names. Now, the version should come after the module name (as is usual in most other tools). For compatibility, that searcher still tries the old format if it cannot find an open function according to the new style. (Lua 5.2 already worked that way, but it did not document the change.)
8.3 – Changes in the API

Continuation functions now receive as parameters what they needed to get through lua_getctx, so lua_getctx has been removed. Adapt your code accordingly.
Function lua_dump has an extra parameter, strip. Use 0 as the value of this parameter to get the old behavior.
Functions to inject/project unsigned integers (lua_pushunsigned, lua_tounsigned, lua_tounsignedx, luaL_checkunsigned, luaL_optunsigned) were deprecated. Use their signed equivalents with a type cast.
Macros to project non-default integer types (luaL_checkint, luaL_optint, luaL_checklong, luaL_optlong) were deprecated. Use their equivalent over lua_Integer with a type cast (or, when possible, use lua_Integer in your code).
#9 – The Complete Syntax of Lua

Here is the complete syntax of Lua in extended BNF. As usual in extended BNF, {A} means 0 or more As, and [A] means an optional A. (For operator precedences, see §3.4.8; for a description of the terminals Name, Numeral, and LiteralString, see §3.1.)


	chunk ::= block

	block ::= {stat} [retstat]

	stat ::=  ‘;’ | 
		 varlist ‘=’ explist | 
		 functioncall | 
		 label | 
		 break | 
		 goto Name | 
		 do block end | 
		 while exp do block end | 
		 repeat block until exp | 
		 if exp then block {elseif exp then block} [else block] end | 
		 for Name ‘=’ exp ‘,’ exp [‘,’ exp] do block end | 
		 for namelist in explist do block end | 
		 function funcname funcbody | 
		 local function Name funcbody | 
		 local namelist [‘=’ explist] 

	retstat ::= return [explist] [‘;’]

	label ::= ‘::’ Name ‘::’

	funcname ::= Name {‘.’ Name} [‘:’ Name]

	varlist ::= var {‘,’ var}

	var ::=  Name | prefixexp ‘[’ exp ‘]’ | prefixexp ‘.’ Name 

	namelist ::= Name {‘,’ Name}

	explist ::= exp {‘,’ exp}

	exp ::=  nil | false | true | Numeral | LiteralString | ‘...’ | functiondef | 
		 prefixexp | tableconstructor | exp binop exp | unop exp 

	prefixexp ::= var | functioncall | ‘(’ exp ‘)’

	functioncall ::=  prefixexp args | prefixexp ‘:’ Name args 

	args ::=  ‘(’ [explist] ‘)’ | tableconstructor | LiteralString 

	functiondef ::= function funcbody

	funcbody ::= ‘(’ [parlist] ‘)’ block end

	parlist ::= namelist [‘,’ ‘...’] | ‘...’

	tableconstructor ::= ‘{’ [fieldlist] ‘}’

	fieldlist ::= field {fieldsep field} [fieldsep]

	field ::= ‘[’ exp ‘]’ ‘=’ exp | Name ‘=’ exp | exp

	fieldsep ::= ‘,’ | ‘;’

	binop ::=  ‘+’ | ‘-’ | ‘*’ | ‘/’ | ‘//’ | ‘^’ | ‘%’ | 
		 ‘&’ | ‘~’ | ‘|’ | ‘>>’ | ‘<<’ | ‘..’ | 
		 ‘<’ | ‘<=’ | ‘>’ | ‘>=’ | ‘==’ | ‘~=’ | 
		 and | or

	unop ::= ‘-’ | not | ‘#’ | ‘~’

Last update: Tue Jan 6 10:10:50 BRST 2015
