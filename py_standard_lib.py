# dir built-in funcgets attributes of objects
import sys
import os 
# print( dir(sys.stdin))
# print( dir(()) )
# print( dir(sys)) #modules are objects too
# print( dir(os))
# print( os.environ)



# # type built-in procides a way to learn about object youre manipulating
# # print('type: ',type(sys.version))
# print( type(os.environ ))

class IntegerField(object):
	"""docstring for IntegerField"""
	pass
		
integer = IntegerField()
# name = integer.attributeName()
# print(dir(integer),'\n')
# print('weakref ----------------',dir(integer.__repr__))
# print(dir(os))
from dis import dis
dis(IntegerField)

# print(dir(integer.attributeName))