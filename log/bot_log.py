import logging
import sys

logging.basicConfig(filename='log/bot.log',level=logging.DEBUG,\
      format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')

logging.debug('Start bot')