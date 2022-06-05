# The following python libraries are required
from bs4 import BeautifulSoup
import requests
# Website from which data scraping need to be done. To change the company name, rename Asian Paints with any other company eg: MRF
url="https://www.moneycontrol.com/stocks/hist_stock_result.php?ex=B&sc_id=API&mycomp=Asian Paints"
# Enter the "from and to date"
datas={}
datas["frm_dy"] = 11
datas["frm_mth"] = 11
datas["frm_yr"] = 2020
datas["to_dy"] = 15
datas["to_mth"] = 11
datas["to_yr"] = 2020
datas["hdn"] = "daily"
send_date=requests.post(url,data=datas)
soup=BeautifulSoup(send_date.text,"html.parser")
table = soup.find('table', attrs={'class': 'tblchart'})

str = ""
for j in table.find_all('th'):
    str += j.text+','
for i in table.find_all('tr'):
    for j in i.find_all('td'):
        str+= j.text+','
    str+= '\n'
print(str)
