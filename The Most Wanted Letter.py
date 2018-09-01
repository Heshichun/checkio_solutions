def checkio(data:str):
	data = str.lower(data)
	data = list(filter(str.isalpha, data))#过滤 只保留字母
	l = {key: 0 for key in data}#生成一个字典
	for i in data:
		l[i] += 1#记录每个字母出现的次数
#	l = [x for x in l1.items()]
	l = sorted(list(l.items()) , key=lambda x:x[1])#sorted 函数需要传入一个列表，然后以列表内的键值对为标准排序
#	l = dict(l)
	max = l[-1][1]#因为是正序的，所以取最后一组键值对，其值即为最大值
	l = dict(l)
	if list(l.values()).count(max) > 1:#检查一共有几个最大值
		test = [x for x in list(l.keys()) if l.get(x) == max]
	else:
#		print(list(l.keys())[-1])
		return list(l.keys())[-1]
#	print(sorted(test)[0])
	return sorted(test)[0]
	
#https://blog.csdn.net/petib_wangwei/article/details/38685303
#https://segmentfault.com/q/1010000006990491
#https://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p11_strip_unwanted_characters.html
#stirng.ascii_lowercase 也就是 'a-z'
checkio('hello')