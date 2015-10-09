'''
Created on Oct 8, 2015

@author: ljiang
'''
import requests
import json

#create a session
s = requests.Session()

#Get the id of the post with string 'voluptate suscipit sunt' in the title of the post
r = s.get('http://jsonplaceholder.typicode.com/posts')
contents_json = json.loads(r.content)
for post in contents_json:
    if 'voluptate suscipit sunt' in post['title']:
        id = post['id']
        title = post['title']
        body = post['body']
        userId = post['userId']
        print id
        break

#Update the tile and body of the post with the id you have printed to 'Hacker' and 'Information hacked' respectively. Then print the new title and body from the response respectively.
json_to_update = {
  'id': id,
  'title': 'Hacker',
  'body': 'Information hacked',
  'userId': userId
}
r2 = s.put('http://jsonplaceholder.typicode.com/posts/'+str(id), json_to_update)
content_json_2 = json.loads(r2.content)
print content_json_2['title'], content_json_2['body']

#Delete the post you got and print the status code of delete
r3 = s.delete('http://jsonplaceholder.typicode.com/posts/'+str(id))
print r3.status_code
pass