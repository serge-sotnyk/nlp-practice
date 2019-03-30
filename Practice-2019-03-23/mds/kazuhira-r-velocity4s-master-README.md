# Velocity4s [![Build Status](https://travis-ci.org/kazuhira-r/velocity4s.svg?branch=master)](https://travis-ci.org/kazuhira-r/velocity4s)
[Apache Velocity](http://velocity.apache.org/)のScala向けラッパーライブラリです。

UberspectをScala向け実装して、以下の機能拡張を行っています。

- foreachディレクティブでのScala CollectionやOptionを利用可能に
- Scalaのpublicなメンバへのプロパティ表記でのアクセスを可能に
- ScalaのMapに対して、$map['key']のような形式でのアクセスを可能に

## 使い方
### velocity.propertiesの設定変更で適用する場合

velocity.propertiesのUberspectの指定箇所に、「org.velocity4s.ScalaUberspect」を設定します。
```
runtime.introspector.uberspect = org.velocity4s.ScalaUberspect
```

### 拡張したVelocityEngineを使用する場合
ScalaVelocityEngineを使用します。

```scala
import org.velocity4s.ScalaVelocityEngine

val engine = ScalaVelocityEngine.create
// val engine = ScalaVelocityEngine.create(/* java.util.Properties */)
// val engine = ScalaVelocityEngine.create(/* "velocity.propertiesへのパス" */)

// more configuration...

engine.init()
```

ScalaVelocityEngine#createで、ScalaUberspectが追加されたVelocityEngineが取得できます。init後、通常のVelocityEngineと同様に使用します。

## サンプル
```scala
import org.velocity4s.ScalaVelocityEngine

case class Person(name: String, age: Int)

val engine = ScalaVelocityEngine.create
engine.addProperty(RuntimeConstants.RESOURCE_LOADER, "string")
engine.addProperty("string.resource.loader.class", classOf[StringResourceLoader].getName)
engine.init()

val templateAsString = """|$person.name
                          |$person.age
                          |
                          |#foreach ($e in $list)
                          |$e
                          |#end
                          |
                          |#foreach ($k in $map.keys())
                          |$map[$k]
                          |#end
                          |
                          |#foreach ($v in $some)
                          |some($v)
                          |#end
                          |#foreach ($v in $none)
                          |none
                          |#end
                          |
                          |""".stripMargin
val templateName = "template.vm"

StringResourceLoader.getRepository.putStringResource(templateName, templateAsString)

val context = new VelocityContext
context.put("person", Person("Taro", 20))
context.put("list", List("Java", "Scala", "Groovy", "Clojure"))
context.put("map", Map("key1" -> "value1", "key2" -> "value2"))
context.put("some", Some("hello"))
context.put("none", None)

val template = engine.getTemplate(templateName)

val writer = new StringWriter
template.merge(context, writer)
println(writer)
```

結果。
```
Taro
20

Java
Scala
Groovy
Clojure

value1
value2

some(hello)


```

## LICENSE
Copyright &copy; 2014 kazuhira-r


Licensed under the [Apache License, Version 2.0][Apache]
 
[Apache]: http://www.apache.org/licenses/LICENSE-2.0

