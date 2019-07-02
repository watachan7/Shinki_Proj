import module1
import importlib

module_name='hlz'

f = open('module1.py', 'a')
f.write('\ndef hlz():\n print(\'helloworldz\')')
f.close() 

importlib.reload(module1)

