# logging level: 
debug, info, warning, error, critical  
The default level is WARNING  

# A simple example:  

import logging  
logging.warning('Watch out!')  \# will print a message to the console  
logging.info('I told you so')  \# will not print anything  

which would print:  

WARNING:root:Watch out!  

# Logging to a file:  

import logging  
logging.basicConfig(filename='example.log',level=logging.DEBUG)  
logging.debug('This message should go to the log file')  
logging.info('So should this')  
logging.warning('And this, too')  

which would write in example.log:  

DEBUG:root:This message should go to the log file  
INFO:root:So should this  
WARNING:root:And this, too  

# Changing the format of displayed messages:  

import logging  
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)  
logging.debug('This message should appear on the console')  
logging.info('So should this')  
logging.warning('And this, too')  

which would print:  

DEBUG:This message should appear on the console  
INFO:So should this  
WARNING:And this, too  


# Displaying the date/time in messages:  

import logging  
logging.basicConfig(format='%(asctime)s %(message)s')  
logging.warning('is when this event was logged.')  

which should print something like this:  

2010-12-12 11:41:42,612 is when this event was logged.  

## changing the date/time format:  

The default format for date/time display (shown above) is ISO8601. If you need more control over the formatting of the date/time, provide a datefmt argument to basicConfig, as in this example:  

import logging  
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')  
logging.warning('is when this event was logged.')  

which would display something like this:  

12/12/2010 11:46:36 AM is when this event was logged.  


# Logger objects:  

Logger.setLevel()  
specifies the lowest-severity log message a logger will handle  

Logger.addHandler() and Logger.removeHandler() 
add and remove handler objects from the logger object.  

the following methods create log messages:  
Logger.debug(), Logger.info(), Logger.warning(), Logger.error(), and Logger.critical()  

getLogger()   
returns a reference to a logger instance with the specified name if it is provided, or root if not.  

## handlers:  

few handler types: StreamHandler, FileHandler, ...  

## methods:  

### setLevel()   
method, just as in logger objects, specifies the lowest severity that will be dispatched to the appropriate destination.   
Why are there two setLevel() methods?  
The level set in the logger determines which severity of messages it will pass to its handlers.   
The level set in each handler determines which messages that handler will send on.  

### setFormatter()   
selects a Formatter object for this handler to use.  

the default date format is:  
%Y-%m-%d %H:%M:%S  
with the milliseconds at the end  

The following message format string will log the time in a human-readable format, the severity of the message, and the contents of the message, in that order:  
'%(asctime)s - %(levelname)s - %(message)s'  

# full example  

import logging  

\# create logger  
logger = logging.getLogger('simple_example')  
logger.setLevel(logging.DEBUG)  

\# create console handler and set level to debug  
ch = logging.StreamHandler()  
ch.setLevel(logging.DEBUG)  
  
\# create formatter  
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  

\# add formatter to ch  
ch.setFormatter(formatter)  

\# add ch to logger  
logger.addHandler(ch)  

\# 'application' code  
logger.debug('debug message')  
logger.info('info message')  
logger.warn('warn message')  
logger.error('error message')  
logger.critical('critical message')  

## Running this module from the command line produces the following output:  

$ python simple_logging_module.py  
2005-03-19 15:10:26,618 - simple_example - DEBUG - debug message  
2005-03-19 15:10:26,620 - simple_example - INFO - info message  
2005-03-19 15:10:26,695 - simple_example - WARNING - warn message  
2005-03-19 15:10:26,697 - simple_example - ERROR - error message  
2005-03-19 15:10:26,773 - simple_example - CRITICAL - critical message  


FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'  
logging.basicConfig(format=FORMAT)  
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}  
logger = logging.getLogger('tcpserver')  
logger.warning('Protocol problem: %s', 'connection reset', extra=d)  

would print something like:  

2006-02-08 22:20:02,165 192.168.0.1 fbloggs  Protocol problem: connection reset  


