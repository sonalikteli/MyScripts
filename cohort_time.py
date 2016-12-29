import timeit
 
# Request the page 100 times, time the response time
 
t = timeit.Timer("h.request('http://su-vm-060.anant.saama.com:9090/CohortBuilder/vividSenseAppService/api/dashboards/cohort/widgets/patients?QUERYTYPE=select',headers={'cache-control':'no-cache'})", "from httplib2 import Http; h=Http()")
times_p1 = t.repeat(100,1)

print "The time taken by each request in  a list  : ", times_p1

average_time = reduce(lambda x, y: x + y, times_p1) / len(times_p1)

print "Average Time: ", average_time
