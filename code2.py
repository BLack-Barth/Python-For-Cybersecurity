import py_compile
import marshal
import dis
from rich import print

py_compile.compile('fuc.py',cfile='n_fuc.pyc')
print('DONE')

with open("n_fuc.pyc","rb") as file :
    file.seek(16)
    de_code = marshal.loads(file.read())
    print(de_code)

code_str = dis.code_info(de_code)
print(code_str)

dis.dis(de_code)