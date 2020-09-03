import requests
import bs4
from datetime import date,datetime

i=0

site=requests.get("http://datak.ir/mydatak/service_profile?detail_id=profile.show&oid=81336487")
soup=bs4.BeautifulSoup(site.content.decode("UTF-8"), 'html.parser')
for link in soup.findAll("span"):
    if(i==1):   
        v= float(link.string)
        i=0
    if(link.string=="صفحه اصلی"):
        i=1
        
f_date = date(2020, 6, 6)
l_date = datetime.now().date()
d = (l_date - f_date).days

print("حجم:",v)
print("زمان گذشته:",d)
if((100-v)/d>3.33):
    print("ریحانه داره اینترنتو میخوره")
else:
    print("وضع خوبه")