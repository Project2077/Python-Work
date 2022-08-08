first_name="ada"
last_name="lovelace"

### f字符串 f是format(设置格式)的简写
### 格式 f"{}{}..."    {} 花括号
### python会将花括号中的变量替换成其值 
### 注：花括号之间增加空格会影响格式 ada lovelace adalovelace
full_name=f"{first_name} {last_name}"
print(full_name)


### 不加花括号就是字符串
### 花括号中可以引用python变量及函数 Hello，Ada Lovelace!
print(f"Hello,{full_name.title()}!")

### 也可以以使用f字符串来创建消息，再把整条消息赋给变量 
### 这样以后调用起来方便
message=f"Hello,{full_name.title()}!"

