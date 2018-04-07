import requests
import json

response = requests.get('https://api.github.com/repos/code-dot-org/code-dot-org/comments', auth = ('satvikshukla', '&azgithub19'))
dict2 = json.loads(response.content)[0]
# print(response.text)
# print(response.content)
print(dict2['body'])