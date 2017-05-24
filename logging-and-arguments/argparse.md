# argparse   
It is a parsing module  

## Example   
import argparse  
parser = argparse.ArgumentParser()  
parser.parse_args()  

$ python prog.py --help  
usage: prog.py [-h]  

optional arguments:  
  -h, --help  show this help message and exit  

The --help option, which can also be shortened to -h, is the only option we get for free (i.e. no need to specify it)  
## Introducing Positional arguments  
import argparse  
parser = argparse.ArgumentParser()  
parser.add_argument("echo", help="echo the string you use here")  
args = parser.parse_args()  
print args.echo 

And we get:  
$ python prog.py -h  
usage: prog.py [-h] echo  

positional arguments:    
  echo        echo the string you use here  

optional arguments:  
  -h, --help  show this help message and exit  

## Introducing Optional arguments  

import argparse  
parser = argparse.ArgumentParser()  
parser.add_argument("--verbose", help="increase output verbosity",action="store_true")  
args = parser.parse_args()  
if args.verbose:  
   print "verbosity turned on"  
   
And the output:  
$ python prog.py --verbose  
verbosity turned on  

$ python prog.py --help  
usage: prog.py [-h] [--verbose]  

optional arguments:  
  -h, --help  show this help message and exit  
  --verbose   increase output verbosity  

### store_true  
keyword, action, and give it the value "store_true". 
This means that, if the option is specified, assign the value True to args.verbose  

### Short options  
import argparse  
parser = argparse.ArgumentParser()  
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")  
args = parser.parse_args()  
if args.verbose:  
    print "verbosity turned on"  

And here goes:  
$ python prog.py -v  
verbosity turned on  
$ python prog.py --help  
usage: prog.py [-h] [-v]  

optional arguments:  
  -h, --help     show this help message and exit  
  -v, --verbose  increase output verbosity  


### choices  
import argparse  
parser = argparse.ArgumentParser()  
parser.add_argument("square", type=int, help="display a square of a given number")  
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], help="increase output verbosity")  
args = parser.parse_args()    
answer = args.square**2 
if args.verbosity == 2:   
    print "the square of {} equals {}".format(args.square, answer)  
elif args.verbosity == 1:  
    print "{}^2 == {}".format(args.square, answer)  
else:  
    print answer  
