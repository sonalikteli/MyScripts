#!/usr/bin/python
import multiprocessing
import requests

def capture_ap_response():
   time= requests.get("http://google.com").elapsed.total_seconds()
   print time

if __name__ == '__main__':
  pool = multiprocessing.Pool()
  results = pool.capture_ap_response()
  print(results)
