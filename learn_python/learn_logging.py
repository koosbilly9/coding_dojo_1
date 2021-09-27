import logging

# basic config can only be called once
## filename sets filename else it writes to stio
## format : of the message this one is with time
## level : from what level to log
logging.basicConfig(filename='app.log', format='%(asctime)s - %(message)s', level=logging.INFO)



logging.info('Admin logged in')