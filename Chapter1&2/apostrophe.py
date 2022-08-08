message="one of python's strength is its diverse community."
print(message)
### 撇号位于两个双引号之间，因此Python解释器能够正确地理解这个字符串

### 然而，如果使用单引号，Python将无法正确地确定字符串的结束位置
### message = 'One of Python's strengths is its diverse community.'
### print(message)

###   File "E:\python_work\apostrophe.py", line 6
###    message = 'One of Python's strengths is its diverse community.'
###                                                                  ^
### SyntaxError: unterminated string literal (detected at line 6)
### [Finished in 125ms] 

### 所以尽量用双引号表示字符串吧!!!