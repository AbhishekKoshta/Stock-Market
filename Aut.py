import urllib
import urllib2, cookielib
url = "https://nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=797&symbol=pnb&symbol=pnb&instrument=OPTSTK&date=-&segmentLink=17&segmentLink=17"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
     'Referer': 'https://cssspritegenerator.com',
     'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
     'Accept-Encoding': 'none',
     'Accept-Language': 'en-US,en;q=0.8',
     'Connection': 'keep-alive'}

#d = get(url,headers=hdr)

df = urllib2.Request(url,headers=hdr)
#page = urllib.urlopen(df)

try:
    page = urllib2.urlopen(df)
except urllib2.HTTPError, e:
    print e.fp.read()

content = page.read()
with open("Backend.txt", 'w') as bm:
    bm.write("{}".format(content))
#for line in content:
#    print line
for x in open("Backend.txt","r").readlines():
    print x    


from bs4 import BeautifulSoup
import  requests
# Main Coding Sectio
start = 0
while True:
    try:
        nxt = url.format(start)
        r = requests.get(nxt)
        soup = BeautifulSoup(r.content)
        print(soup.find("table",{"class": "gf-table historical_price"}).get_text())
    except Exception as e:
        print(e)
        break
    start += 30

<table id="octable" width="100%" border="0" cellpadding="0" cellspacing="0">
					
    