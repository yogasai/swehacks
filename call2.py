import requests
import json

response = requests.get('https://api.github.com/repos/code-dot-org/code-dot-org/comments', auth = ('satvikshukla', '&azgithub19'))

# for i in response(1,10):
# 	pass

i = 0
str = ""

# for obj in json.loads(response.content)
# 	print("a")
	# dict2 = 
	# print(dict2['body'])
print(len(json.loads(response.content)))

while (i < 30):
	dict2 = json.loads(response.content)[i]
	print(dict2['body'])
	i = i + 1