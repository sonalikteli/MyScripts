#!/usr/bin/python


import pycurl, timeit
c = pycurl.Curl()
c.setopt(c.URL, "'http://su-vm-060.anant.saama.com:9090/CohortBuilder/vividSenseAppService/api/dashboards/cohort/widgets/patients?QUERYTYPE=select' -H 'Pragma: no-cache' -H 'Origin: http://su-vm-060.anant.saama.com:9090' -H 'Accept-Encoding: gzip, deflate' -H 'X-CSRF-TOKEN: ' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: application/json, text/plain, */*' -H 'Cache-Control: no-cache' -H 'Referer: http://su-vm-060.anant.saama.com:9090/CohortBuilder/' -H 'Cookie: JSESSIONID=08FEE6937ABDA28E7EE12002FC37F437; visid_incap_362573=bzDpfPRCRly2dhEemv4R4p0A/lcAAAAAQUIPAAAAAAD7+eE33fGjDL0ma3lXhGbK; incap_ses_165_362573=JCKVApU3mFQh5eosrjJKAvliCFgAAAAAUzmUYtURGp5TujWDchtjxg==' -H 'Connection: keep-alive' --data 'one=%7B%22canvas%22%3A%5B%7B%22type%22%3A%22Diagnosis%22%2C%22index%22%3A%22Index%22%2C%22dataId%22%3A%5B%222%22%5D%2C%22operator%22%3A%22And%22%7D%5D%7D&digObj=0&digObj=730&procObj=0&procObj=730&therapyObj=0&therapyObj=730&testObj=0&testObj=730&cleanPeriod=0&enrollmentPeriod=0&gender=0&ageFrom=0&ageTo=120&userName=demo&preDigObj=0&preDigObj=730&postDigObj=0&postDigObj=730&preProcObj=0&preProcObj=730&postProcObj=0&postProcObj=730&preTherapyObj=0&preTherapyObj=730&postTherapyObj=0&postTherapyObj=730&preTestObj=0&preTestObj=730&postTestObj=0&postTestObj=730&diagnosisIds=2&selectDataSouce=cprd_mock1' --compressed")
c.setopt(c.VERBOSE, True) # to see request details
ts = timeit.default_timer()
c.perform()
print timeit.default_timer() - ts
