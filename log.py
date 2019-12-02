import logging

'''
logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')
'''

# Syntax for writing into the file
logging.basicConfig(filename='app_2.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
mylogger = logging.getLogger()

# This text will be logged!
def test(i):
    if i==1:
        mylogger.warning('Passed')
    else:
        mylogger.warning('Failed')

i=1
test(i)

