def checkio(data):
	if 0 < len(data) <= 64:
		if any(i.islower() for i in data) and any(i.isdigit() for i in data) and any(i.isupper() for i in data):
			#列表生成器
			return True
		else:
			return False
	else:
		return False
		
#http://www.codexiu.cn/python/blog/33196/
#any(x)用于查找 true ， 只要有一个 true 函数就会返回 true 。