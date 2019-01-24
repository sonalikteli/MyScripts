#!/usr/bin/python
import multiprocessing
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import Popen, PIPE
import os
import logging
import sys, getopt


#multiprocessing.log_to_stderr(logging.DEBUG)

def main(argv):
   itteration = ''
   users = ''
   try:
      opts, args = getopt.getopt(argv,"hi:u:",["iter=","user="])
   except getopt.GetoptError:
      print 'scriptname -i <itteration> -u <user>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'scriptname -i <itteration> -u <user>'
         sys.exit()
      elif opt in ("-i", "--iter"):
         itteration = arg
      elif opt in ("-u", "--user"):
         users = arg
   print 'The number of iteration is : ', itteration
   print 'The number of user is : ', users
   itteration = int(itteration)
   users = int(users)
   
   def child(cmd):
      p = Popen(cmd, stdout=PIPE, shell=True)
      out, err = p.communicate()
      return out, p.returncode

   commands = []

   command = "curl -s "

   for i in range(itteration):   # run 10 curl commands in total
       #print os.system(command)
       commands.append(command)

   pool = Pool(users) # Nummber of concurrent commands at a time

   times = []
   for i, (output, returncode) in enumerate(pool.imap(child, commands)):
       if returncode != 0:
           print("{} command failed: {}".format(i, returncode))
       else:
           print("{} success: {}".format(i, output))
           times.append(float(output))
   
   print 'Average: {}'.format(sum(times) / len(times) if times else 0)

if __name__ == "__main__":
   main(sys.argv[1:])
