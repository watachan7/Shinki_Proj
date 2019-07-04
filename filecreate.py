import module1
import base_modules
#import importlib

#module_name='hlz'

texts="texts/testidiom.txt"

textdata = base_modules.textfile_wordfile_creator(texts)

print(textdata)

#f = open('module1.py', 'a')
#f.write('\ndef hlz():\n print(\'helloworldz\')')
#f.close() 

#importlib.reload(module1)

