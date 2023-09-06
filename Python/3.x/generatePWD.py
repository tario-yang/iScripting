import random
import string

# 定义密码长度
length = 10

# 定义密码字符集
characters = string.ascii_letters + string.digits + string.punctuation

# 生成随机密码
password = ''.join(random.choice(characters) for i in range(length))

print("您的随机密码是：", password)
