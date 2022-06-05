import requests
import lists
from bs4 import BeautifulSoup
ids=input("Enter the ID of the Company:")
datas={}
k = input("1.Daily\n2.Monthly\n3.Yearly\nEnter Your Input:")
if(k == '1'):
    datas["frm_dy"] = int(input('From Date:'))
    datas["frm_mth"] = int(input('From Month:'))
    datas["frm_yr"] = int(input('From Year:'))
    datas["to_dy"] = int(input('To Date:'))
    datas["to_mth"] = int(input('To Month:'))
    datas["to_yr"] = int(input('To Year:'))
    datas["hdn"] = "daily"
elif(k == '2'):
    datas["mth_frm_mth"] = int(input('From Month:'))
    datas["mth_frm_yr"] = int(input('From Year:'))
    datas["mth_to_mth"] = int(input('To Month:'))
    datas["mth_to_yr"] = int(input('To Year:'))
    datas["hdn"] = "monthly"
else:
    datas["frm_yrly_yr"] = int(input('From Year:'))
    datas["hdn"] = "yearly"

url = "https://www.moneycontrol.com/stocks/hist_stock_result.php?ex=B&sc_id=" +ids+"&mycomp="+lists.Dict[ids]

x = requests.post(url, data=datas)
soup = BeautifulSoup(x.content, 'html5lib')
Name = soup.find_all('b')[1].text
param= soup.find_all('strong')
print(Name)
table = soup.find('table', attrs={'class': 'tblchart'})
f = open('output.csv', 'w')
str = ""
for j in table.find_all('th'):
    str += j.text+','
str += '\n'
for i in table.find_all('tr'):
    for j in i.find_all('td'):
        str += j.text+','
    str += '\n'
f.write(Name+'\n')
for each in param:
    f.write(each.text.replace(':',',')+'\n')

f.write("Price History\n\n")
f.write(str)
print("Data Entered Successfully!! check Output.csv for the output")