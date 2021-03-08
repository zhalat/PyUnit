import logging
import os

# common setup
root_log = logging.getLogger()
root_log.setLevel(level=logging.DEBUG if 'DEBUG' in os.environ else logging.INFO)
root_log.name = 'main'

# logger console channel
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('%(asctime)s::%(levelname)s\t[%(filename)s]\t%(message)s'))
root_log.addHandler(ch)

# logger file channel
fh = logging.FileHandler('UT.log')
fh.setFormatter(logging.Formatter('%(asctime)s::%(levelname)s\t[%(filename)s]\t%(message)s'))
root_log.addHandler(fh)
