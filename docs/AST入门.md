## 1. 什么是AST

在计算机科学中，抽象语法树（Abstract Syntax Tree，AST），或简称语法树（Syntax tree），是源代码语法结构的一种抽象表示。**它以树状的形式表现编程语言的语法结构，树上的每个节点都表示源代码中的一种结构。**

之所以说语法是“抽象”的，是因为这里的语法并不会表示出真实语法中出现的每个细节。比如，嵌套括号被隐含在树的结构中，并没有以节点的形式呈现；而类似于 if-condition-then 这样的条件跳转语句，可以使用带有三个分支的节点来表示。

举例：

console.log("Hello,AST!") 对应的语法树如下：
![img](http://markdown-media.oss-cn-beijing.aliyuncs.com/2020/08/26/15984215749701.jpg?x-oss-process=style/markdown-media)

详情见 维基百科：[https://zh.wikipedia.org/wiki/%E6%8A%BD%E8%B1%A1%E8%AA%9E%E6%B3%95%E6%A8%B9](https://zh.wikipedia.org/wiki/抽象語法樹)

## 2. 工具及语法树参考资料

1.  js在线解析成语法树: https://astexplorer.net/

2.  查看AST结构图：https://resources.jointjs.com/demos/rappid/apps/Ast/index.html

3.  查看JavaStript代码流程: https://bogdan-lyashenko.github.io/js-code-to-svg-flowchart/docs/live-editor/index.html

4.  语法树语义文档：

    1.  https://developer.mozilla.org/zh-CN/docs/Mozilla/Projects/SpiderMonkey/Parser_API
    2.  [https://github.com/yacan8/blog/blob/master/posts/JavaScript%E6%8A%BD%E8%B1%A1%E8%AF%AD%E6%B3%95%E6%A0%91AST.md](https://github.com/yacan8/blog/blob/master/posts/JavaScript抽象语法树AST.md)
    3.  https://segmentfault.com/a/1190000015653342
    4.  各个节点解释：https://github.com/babel/babylon/blob/master/ast/spec.md#expressionstatement

5.  Babel（操作语法树的库）:

    1.  官方文档：https://www.babeljs.cn/docs/
    2.  Babel 插件手册：https://github.com/jamiebuilds/babel-handbook/blob/master/translations/zh-Hans/plugin-handbook.md
    3.  babel剖析：http://www.alloyteam.com/2017/04/analysis-of-babel-babel-overview/

    安装：

    ```
    npm init
    # 安装在当前项目下
    
    npm install @babel/core
    
    # 全局
    
    npm install @babel/core -g        
    ```

6.  代码加密：https://obfuscator.io/

## 3. 语法树结构简介

![-w1781](http://markdown-media.oss-cn-beijing.aliyuncs.com/2020/08/26/15984208898337.jpg?x-oss-process=style/markdown-media)

1.  type: 表示当前节点的类型
2.  start: 表示当前节点的起始位。
3.  end: 表示当前节点的末尾。
4.  loc : 表示当前节点所在的行列位置，里面也有start与end节点，这里的start与上面的start是不同的，这里的start是表示节点所在起始的行列位置，而end表示的是节点所在末尾的行列位置。
5.  errors:是File节点所特有的属性，可以不用理会。
6.  program:包含整个源代码，不包含注释节点。
7.  comments:源代码中所有的注释会在这里显示。

逆向过程中需关注 **type,start,end以及它的子节点**， 其他的属性我们在还原的时候一般用不到。

**console.log("Hello,AST!"); 结构分析：**

1.  ExpressionStatement 类型的节点，这个节点一定会有一个 expression 的子节点
2.  这里 expression 节点的类型是 CallExpression，它同时又包含了callee 和 arguments 两个子节点，callee 可以理解为函数名，而 arguments 则是它的参数。
3.  callee 节点 包含了 object，property和 computed 节点，object 表示对象，property 表示其属性，而 computed 表示其方式。
4.  arguments 节点，是一个Array类型，因此单词是复数形式。在这里它只有一个元素，说明该函数只有一个实参，实参是一个 StringLiteral 类型的节点，也就是字变量。

## 5. babel基本使用

### 5.1 常用的代码结构

#### 1. 读取js文件，并取出所有源代码:

```
const fs = require('fs');
var jscode = fs.readFileSync("./encode.js", {
    encoding: "utf-8"
});
```

特别注意:一定要将从网上copy下面的代码保存为 utf-8 格式

#### 2. 将JavaScript源代码 转换成一棵AST树：

```
const {parse} = require("@babel/parser");
let ast = parse(jscode);
// 打印
JSON.stringify(ast, null, '\t')
```

#### 3. 遍历 各个节点的函数:

```
const traverse = require("@babel/traverse").default;
traverse(ast,visitor);
```

#### 4. 节点的类型判断、构造、替换等操作:

```
const t = require("@babel/types");
// 判断类型
t.isXXXXX(node) 如 t.isStringLiteral(init)
```

#### 5. 将AST转换成JavaScript源代码：

```
const generator = require("@babel/generator").default;
let {code} = generator(ast);
// 写文件
fs.writeFile('decode.js', code, (err)=>{});
```

#### 整体框架

```
const fs = require('fs');
const {parse} = require("@babel/parser");
const traverse = require("@babel/traverse").default;
const t = require("@babel/types");
const generator = require("@babel/generator").default;

let jscode = fs.readFileSync("./jscode.js", {
    encoding: "utf-8"
});
let ast = parse(jscode);

const visitor = 
{
  //TODO  write your code here！
}


//some function code


traverse(ast,visitor);
let {code} = generator(ast);
fs.writeFile('decode.js', code, (err)=>{});
```

### 5.1. path 常用方法介绍：

1.  当前路径所对应的源代码 `path.toString()`

2.  判断path是什么type：`path.isXXX()`, 如：

    ```
    if(path.isStringLiteral())
     {
    
       //do something;
    
     }
    ```

3.  获取path的上一级路径：`path.parentPath;`

4.  获取path的子路径：`path.get('xxx');`

5.  删除path：`path.remove()`

6.  替换path：单路径可以使用replaceWith方法，多路径则使用replaceWithMultiple方法，比如你想将 1 + 2 替换成 3，你可以像下面这样的代码进行替换:

    ```
    path.replaceWith({type:"NumericLiteral",value:3});
    ```

    或

    ```
     const t = require("@babel/types");
     path.replaceWith(t.NumericLiteral(3));
    ```

7.  查看path/node源代码：

    path: path.toString() 
    node: generator(node).code;

了解更多，查看源码：@babel\traverse\lib\path

### 5.2 TODO

## 示例1: 十六进制还原

```
var a = "\x48\x65\x6c\x6c\x6f";
```

方法1:

```
const visitor = {
  VariableDeclaration(path){
      console.log(JSON.stringify(path.node, null, "\t"));
      const init = path.get('declarations')[0].get("init");
      console.log(t.isStringLiteral(init));
      if (!t.isStringLiteral(init)) return;
      const node = init.node;
      let {value, extra} = node;
      extra.raw = '"'  + value + '"'
      console.log(JSON.stringify(extra, null, "\t"));
  }
};
```

方法2：

```
const visitor = {
  StringLiteral(path) {
    let { value, extra } = path.node;
    extra.raw = '"' + value + '"';
  },
};
```

方法3：

```
const visitor = {
  StringLiteral(path) {
    let { value } = path.node;
    path.replaceWith(t.StringLiteral(value)); // 替换init
    path.stop(); //  替换完停止StringLiteral的遍历，防止递归溢出
  },
};
```

方法4：

```
const visitor = {
  StringLiteral(path) {
    delete path.node.extra.raw;
  },
};
```

方法6：

```
const visitor = {
  StringLiteral(path) {
    delete path.node.extra;
  },
};
```

## 示例2：

将如下代码还原

```
function test(u){
    return function(n,r, t){
      return (t = (r = n.B(0),n).B(1),u)(r, t);
    }
  }
```

思路：

1.因为要处理的是逗号表达式，因此我们在这里直接遍历 SequenceExpression 节点即可。
2.将每个expressions里面的节点提取到 Statement 节点前面，代码效果是一样的
3.因为可能有嵌套的逗号表达式，因此采用exit的方式进行遍历

代码如下：

```
const visitor = {
  SequenceExpression: {
    exit(path) {
      let expressions = path.get("expressions");

      let last_expression = expressions.pop();

      let statement = path.getStatementParent();

      if (statement) {
        for (let expression of expressions) {
          statement.insertBefore(
            t.ExpressionStatement((expression = expression.node))
          );
        }

        path.replaceInline(last_expression);
      }
    },
  },
};
```