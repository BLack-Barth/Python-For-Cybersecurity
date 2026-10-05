import marshal 
from rich import print

import requests

url = 'https://jsonplaceholder.typicode.com/'

response = requests.get(url)
if response.status_code == 200 :
    print("[bold red]Technology Enumeration :[/]")
    for key,value in response.headers.items() :
        print(f"[underline yellow]{key} [/]: [italic blue]{value} [/]")
else :

    print('[bold red] The server is down')


with open("fuc.py","r",encoding="utf-8") as file:
    code = file.read()
    print(code)
    print('_'*120 + '\n')
en_code = marshal.dumps(compile(code,'<string>','exec'))
print(en_code)

with open("script.py","wb") as file:
    file.write(en_code)

with open("script.py","rb") as file:
    de_code = marshal.loads(file.read())
    print(de_code, '_'*120 +'\n')

import py_compile

py_compile.compile('fuc.py',cfile='n_fuc.pyc')
print('DONE')

