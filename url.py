from urllib.parse import urlsplit
import requests
url = 'http://testaspnet.vulnweb.com:8080/default.aspx'
parsed_url = urlsplit(url if "://" else f'//{url}')
print(parsed_url)
print(parsed_url.netloc)
domain = parsed_url.hostname
print(domain)