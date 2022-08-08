print("——————————————————————————————————————————————————————")

### 在编程中，空白 泛指任何非打印字符，如空格、制表符和换行符。你可以使用空白来组
### 织输出，让用户阅读起来更容易。

### 制表符 \t 相当于用了一次tab
print("python")
print("	"+"python")
print("\tpython")
### 换行符 \n 相当于用了一次enter
print("Languages:\nPython\nC\nJavaScript")

### \n \t都是放在字符串中的(引号""中的) 
### 合用 注：先换行再tab   一般都是\n\t 谐音脑瘫
print("Languages:\n\tPython\n\tC\t\nJavascript") 



### 删除空白
favorite_language=" python "
favorite_language.strip()
favorite_language.lstrip()
favorite_language.rstrip()
### strip() 同时剔除字符串两边的空白 
### lstrip() 剔除字符串左边(left)的空白
### rstrip() 剔除字符串右边(right)的空白
### 注意：要永久删除这个字符串中的空白，必须将删除操作的结果关联到变量
favorite_language=favorite_language.strip()
