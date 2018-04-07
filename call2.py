import requests
import json

response = requests.get('https://api.github.com/repos/tensorflow/tensorflow/comments', auth = ('satvikshukla', '&azgithub19'))

# for i in response(1,10):
# 	pass

i = 0
stri = ""

# for obj in json.loads(response.content)
# 	print("a")
	# dict2 = 
	# print(dict2['body'])
var = len(json.loads(response.content))

while (i < var):
	dict2 = json.loads(response.content)[i]
	comment = dict2['body']
	# print(comment)
	i = i + 1
	stri = stri + comment

print(stri)
print(var)