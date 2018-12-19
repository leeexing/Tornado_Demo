# Tornado_Demo
tornado框架学习。搭建简易的restful应用框架


```
+--------------------> X axis
|
|    (X,Y)      (X+W, Y)
|    +--------------+
|    |              |
|    |              |
|    |              |
|    +--------------+
v    (X, Y+H)     (X+W,Y+H)

Y axis
```

## client view

* 第一种方式可以通过直接前端 href 进行跳转，要求 href 里面必须有 `.html`
* 第二种方式是对每个前端路由进行单独的 `render` 函数处理。（tornado里面没有蓝图的概念，只能一个一个写）