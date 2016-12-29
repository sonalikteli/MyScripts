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
#command = "curl -s -w \"%{time_total}\" \"http://su-vm-060.anant.saama.com:9090/CohortBuilder/vividSenseAppService/api/dashboards/cohort/widgets/patients?QUERYTYPE=select' -H 'Pragma: no-cache' -H 'Origin: http://su-vm-060.anant.saama.com:9090' -H 'Accept-Encoding: gzip, deflate' -H 'X-CSRF-TOKEN: ' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: application/json, text/plain, */*' -H 'Cache-Control: no-cache' -H 'Referer: http://su-vm-060.anant.saama.com:9090/CohortBuilder/' -H 'Cookie: JSESSIONID=08FEE6937ABDA28E7EE12002FC37F437; visid_incap_362573=bzDpfPRCRly2dhEemv4R4p0A/lcAAAAAQUIPAAAAAAD7+eE33fGjDL0ma3lXhGbK; incap_ses_165_362573=JCKVApU3mFQh5eosrjJKAvliCFgAAAAAUzmUYtURGp5TujWDchtjxg==' -H 'Connection: keep-alive' --data 'one=%7B%22canvas%22%3A%5B%7B%22type%22%3A%22Diagnosis%22%2C%22index%22%3A%22Index%22%2C%22dataId%22%3A%5B%222%22%5D%2C%22operator%22%3A%22And%22%7D%5D%7D&digObj=0&digObj=730&procObj=0&procObj=730&therapyObj=0&therapyObj=730&testObj=0&testObj=730&cleanPeriod=0&enrollmentPeriod=0&gender=0&ageFrom=0&ageTo=120&userName=demo&preDigObj=0&preDigObj=730&postDigObj=0&postDigObj=730&preProcObj=0&preProcObj=730&postProcObj=0&postProcObj=730&preTherapyObj=0&preTherapyObj=730&postTherapyObj=0&postTherapyObj=730&preTestObj=0&preTestObj=730&postTestObj=0&postTestObj=730&diagnosisIds=2&selectDataSouce=cprd_mock1\" --compressed"

   command = "curl -s -w \"%{time_total}\" -o /dev/null  'http://su-vm-060.anant.saama.com:9090/CohortBuilder/vividSenseAppService/api/dashboards/cohort/widgets/patients?QUERYTYPE=select' -H 'Pragma: no-cache' -H 'Origin: http://su-vm-060.anant.saama.com:9090' -H 'Accept-Encoding: gzip, deflate' -H 'X-CSRF-TOKEN: ' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: application/json, text/plain, */*' -H 'Cache-Control: no-cache' -H 'Referer: http://su-vm-060.anant.saama.com:9090/CohortBuilder/index.jsp' -H 'Cookie: JSESSIONID=A2504F536FF3F99DA43BDE643A05C87C; visid_incap_362573=bzDpfPRCRly2dhEemv4R4p0A/lcAAAAAQUIPAAAAAAD7+eE33fGjDL0ma3lXhGbK; incap_ses_165_362573=JCKVApU3mFQh5eosrjJKAvliCFgAAAAAUzmUYtURGp5TujWDchtjxg==' -H 'Connection: keep-alive' --data 'one=%7B%22canvas%22%3A%5B%7B%22type%22%3A%22Therapy%22%2C%22index%22%3A%22Pre_Index%22%2C%22dataId%22%3A%5B%2215%22%5D%2C%22operator%22%3A%22And%22%7D%2C%7B%22type%22%3A%22Diagnosis%22%2C%22index%22%3A%22Index%22%2C%22dataId%22%3A%5B%221273%22%5D%2C%22operator%22%3A%22And%22%7D%2C%7B%22type%22%3A%22Laboratory+Results%22%2C%22index%22%3A%22Post_Index%22%2C%22dataId%22%3A%5B%22173%22%5D%2C%22operator%22%3A%22And%22%7D%5D%7D&digObj=0&digObj=730&procObj=0&procObj=730&therapyObj=0&therapyObj=730&testObj=0&testObj=730&cleanPeriod=0&enrollmentPeriod=0&gender=0&ageFrom=0&ageTo=120&userName=demo&preDigObj=0&preDigObj=730&postDigObj=0&postDigObj=730&preProcObj=0&preProcObj=730&postProcObj=0&postProcObj=730&preTherapyObj=0&preTherapyObj=730&postTherapyObj=0&postTherapyObj=730&preTestObj=0&preTestObj=730&postTestObj=0&postTestObj=730&diagnosisIds=1273&selectDataSouce=cprd_mock1' --compressed"

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
