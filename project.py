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
import socket
domain = 'testaspnet.vulnweb.com'
ip = socket.gethostbyname(domain)
url = 'http://testaspnet.vulnweb.com/Comments.aspx?id=2'
try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        print(f'[bold green]| OK | {url} | {response.status_code} | UP | IPs : {ip} |[/bold green]')
    else:
        print(f'[yellow]| WARNING | {url} | {response.status_code} |[/yellow]')

except requests.exceptions.RequestException:
    print(f'[red]| FAILED | {url} | DOWN |[/red]')
