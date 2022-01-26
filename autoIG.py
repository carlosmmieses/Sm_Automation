from os import path
from instapy_cli import client

username = 'FinSoft_pr'
password = 'Cm841164818!%'
path = 'images/Kirby.PNG'#r'C:\Users\cas\Documents\Automation\SM_Automation\images\Kirby.png'
text = 'This is an automated post!!! :)'

user = client(username,password)
user.upload(path,text)


# with client(username, password) as cli:
#     cli.upload(image, text)