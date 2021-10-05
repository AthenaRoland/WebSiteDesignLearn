import requests
print('===========Grendel网络爬虫===========')
print('你可以输入grendel -h获得帮助\n©copying zcl Dev ZhangSan.\n')
exit1 = 0
while exit1 != 1:
	choice = input('GrendelRequestsSpider~$:')
	if choice == 'grendel -h':
		print('    -h          获得帮助')
		print('    -r          爬取网站')
		print('    -l          学习及更多')
		print('    -d          信息及版本')
		print('    exit             退出')
	else:
		if choice == 'grendel -r':
			print('请按照标准格式输入')
			print('格式:[请求方式get,post],[网址],[打印方式url,text,content]')
			print('示例:get,http://www,baidu.com,text')
			print('要退出请输入exit')
			exit = 0
			while exit != 1:
				shell = input('RequestsShell~^$:')
				list = shell.split(',')
				if shell.find('exit') != -1:
					exit = 1
				else:
					if shell == " ":
						pass
					else:
						if list[0] == 'get':
							response = requests.get(list[1])
							if list[2] == 'text':
								print(response.text)
								print('\n\n')
							else:
								if list[2] == ' ':
									pass
								else:
									if list[2]  == 'url':
										print(response.url)
									else:
										if list[2] == 'content':
											print(response.content)
						else:
							if list[0] == 'post':
								response = requests.post(list[1])
								if list[2] == 'text':
									print(response.text)
									print('\n\n')
								else:
									if list[2] == ' ':
										pass
									else:
										if list[2]  == 'url':
											print(response.url)
										else:
											if list[2] == 'content':
												print(response.content)
							else:
								print('无效的语法')
		else:
			if choice == 'grendel -l':
							print('本版本只提供requests基本用法\n更多用法请参考https://cn.python-requests.org/zh_CN/latest/')
			else:
				if choice == 'grendel -d':
							print('版本号:1.0\n开发者:张三\n资源所属:ZCL\n©Grendel ZCL by Requests\n建于requests库\n2021.8.27')
				else:
					if choice == 'exit':
						exit1 = 1
					else:
						print('无效的语法')
