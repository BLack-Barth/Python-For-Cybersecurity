#def addnum(num1 , num2):
#
#    #num1 = int(input('Enter number 1:'))
#    #num2 = int(input('Enter number 2:'))
#
#    result = num1 + num2
#    return result
#    pass
#
#rich | pyfiglet | keyword | range
#list=[,] | sets={,} | tuples=(,) | dict={key:value,}
# range(start,stop,step)
# input -> str |  int(input) -> int | float(input) -> float
# import getpass
#password = getpass.getpass('Please enter psswd:')
# def => define
# https://jsonplaceholder.typicode.com/posts
from rich import print
import requests
url = 'http://testaspnet.vulnweb.com/Comments.aspx?id=2'
response = requests.get(url)
if response.status_code == 200 :
    print("[bold red]Technology Enumeration :[/]")
    for key,value in response.headers.items() :
        print(f"[underline yellow]{key} [/]: [italic blue]{value} [/]")
else :
    print('[bold red] The server is down')