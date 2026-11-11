import random

ip = (str(random.randint(0, 255)) + "." +
      str(random.randint(0, 255)) + "." +
      str(random.randint(0, 255)) + "." +
      str(random.randint(0, 255)))

print("随机产生的IPv4地址为: " + ip)