import logging
import sys

logging.basicConfig(filename='daphne.log',level=logging.DEBUG,\
      format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')

try:
    if sys.argv[1] == '-r':
        logging.debug('Restart daphne')
except:
    logging.debug('Start daphne')