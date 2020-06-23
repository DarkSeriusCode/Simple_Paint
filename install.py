'''
This file will install all components
'''
import platform, os

def Install (Module):
	if platform.system() == 'Windows':
		os.system('pip install %s' % (Module))

	else:
		print('Error!')

MODULES = ['threading', 'colorama', 'time']

for x in MODULES:
	Install(x)

print('Complite!')
