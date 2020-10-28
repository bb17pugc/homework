from django.shortcuts import render
from django.shortcuts import render , redirect
import logging

logging.basicConfig(filename='app.log', level=logging.NOTSET,filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# logging.basicConfig(filename='output.log')
def index(request):
    
    logging.debug('Watch out!')
    logging.info('Watch out!')
    logging.warning('Watch out!')
    logging.critical('Watch out!')
    logging.error('Watch out!')
    
    return render(request, 'index.html')