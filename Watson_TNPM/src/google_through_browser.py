import webbrowser
import urllib3

url = "https://eclient.lenexa.ibm.com:9445/search/?q={}".format("TNPM")
webbrowser.open(url)




#import the library used to query a website

#from bs4 import BeautifulSoup
#wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
#page = urllib3.get_host(wiki)
#soup = BeautifulSoup(page)

