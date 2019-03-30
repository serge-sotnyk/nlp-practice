# fetpl
---
一个非常简洁的模板解析引擎. 线上Demo：[http://fetpl.org/](http://fetpl.org/)

## Install
```bash
$ npm install fetpl
```

### 使用说明
```bash
1. 引用fetpl并注册模板引擎
...
app.engine('text', require('./fetpl').render)
app.set('views', './views') // specify the views directory  
app.set('view engine', 'text') // register the template engine  
...

2. 使用模板
...
app.get('/hi', function (req, res) {
  res.render('index', { title: 'Hey', message: 'Hello there!' })
})
...

3. 完整实例
var express = require('express')
var app = express()
app.set('port', 3000)

app.engine('text', require('./fetpl').render)
app.set('views', './views') // specify the views directory  
app.set('view engine', 'text') // register the template engine  

app.get('/hi', function (req, res) {
  res.render('index', { title: 'Hey', message: 'Hello there!' })
})

app.listen(app.get('port'), function () {
  console.log('listening port ' + app.get('port'))
})

注：需安装 npm install fetpl express

4. 模板文件示例

-- views/index.text --
{{include: a}}
{{include: b}}
This is index 

-- views/a.text --
{{include: b}}
This is a 

-- views/b.text --
This is b 



```

### 模板语法   

```bash
1. 值输出   
示例: {{ it.title }} 或 {{ it['title'] }}   

输出: Hey 或 Hey   

2. 循环  
示例1[数组]:    
{{ for: index,vv,cc in it.persons }}    
  {{ index }},{{ cc }} | {{ vv.name }} | {{ vv.email }}    
{{/for}}   
  
输出:     
  0,1 | haiyang | haiyang5210@gmail.com    
  1,2 | haiyang2014 | wanghaiyang@bilibili.com    

  
示例2[键值对]:    
{{ for: key,value,cc of it.maps }}    
  {{ key }},{{ value }},{{ cc }}    
{{/for}}  

输出:     
  name,tom,1    
  age,18,2    
  
3. 条件判断  
it.rand = 29  
示例1:   
{{if: it.rand > 60}}  
  it.rand > 60  
{{elif: it.rand > 30 }}  
  it.rand > 30  
{{else:}}  
  it.rand <= 30  
{{/if}}  

输出:  
it.rand <= 30  

4. 变量定义  
示例:   
{{var: age = 15.5 }}  
I am {{age}} years old.  

输出:   
I am 15.5 years old.  
  
5. 编码/解码（注: 为防止XSS攻击输出默认会用encodeURI编码）  
a. 输出特殊标记    
示例: {\{ or }\}   

输出:   
{{ or }}  

b. 输出特殊标记 
示例: {{'{\{'}} or {{'}\}'}}   

输出:   
{\{ or }\}  

c. URI编码/解码: encodeURI/decodeURI  
示例:  
{{ it.text_str }} | {{ it.text_str|decodeURI }} |

输出:   
%26lt%3Bu%26gt%3B%20text%20%26lt%3B%2Fu%26gt%3B | <u> text </u> |

d. HTML编码/解码: encode/decode  
示例:   
{{ it.text_ogi }} | {{ it.text_ogi|decodeURI|encode }} | {{ it.text_ogi|decodeURI|encode|encode }} |   

输出:   
%3Cu%3E%20text%20%3C%2Fu%3E | <u> text </u> | &lt;u&gt;&nbsp;text&nbsp;&lt;/u&gt; |   

6. 引用子模板 
<pre id="common/footer">
  This is footer.
</pre>  
示例: {{include: common/footer}}  
输出:   
This is footer.
  
7. 注意以下几种情况
it.num = 10  
示例:    
{{ it.num == 10 }} : true   
{{ it.num === 10 }} : true   
{{ it.num == '10' }} : true   
{{ it.num === '10' }} : false   
{{ 0 == '0' }} : true   
{{ 0 === '0' }} : false   
{{ 0 == false }} : true   
{{ 0 === false }} : false   
{{ 0 == null }} : false   
{{ 0 === null }} : false   
{{ 0 == undefined }} : false   
{{ 0 === undefined }} : false   
{{ null == undefined }} : true   
{{ null === undefined }} : false  

```

