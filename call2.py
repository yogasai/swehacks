import requests
import json


stri = ""
j = 0

for k in range(1, 10):

	if len(stri) < 100000:
		par = (('page', k), ('per_page', 100))
		response = requests.get('https://api.github.com/repos/kamranahmedse/developer-roadmap/issues/comments', auth = ('satvikshukla', '&azgithub19'), params = par)

		# for i in response(1,10):
		# 	pass

		i = 0

		# for obj in json.loads(response.content)
		# 	print("a")
			# dict2 = 
			# print(dict2['body'])
		var = len(json.loads(response.content))
		j = j + var
		while (i < var):
			dict2 = json.loads(response.content)[i]
			comment = dict2['body']
			# print(comment)
			i = i + 1
			stri = stri + comment

print(len(stri))
print(j)

text_file = open("sent.txt", "w")
text_file.write(stri)
text_file.close()