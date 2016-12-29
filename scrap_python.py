import urllib2
wiki = "http://si-vm-188:8081/job/FAE%20MAP/544/com.saama.fae$fae-mdp-workflow/"
page = urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)
#print soup.prettify()
all_links=soup.find_all("a")
for link in all_links:
	print link.get("href")

