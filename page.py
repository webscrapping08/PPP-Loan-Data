import streamlit as st

from requests_html  import  HTMLSession
from bs4 import BeautifulSoup
import requests
from csv import writer

import pandas as pd
st.set_page_config(page_title="Onlone jobe.ph",page_icon=":tada:",layout="wide")
st.title (':tada: Searchable PPP Loan Data :tada:')
url= 'https://pppreport.org/'

s =HTMLSession()
r=s.get(url)


p = r.html.xpath('//*[@id="results"]',first=True)


with open('jen.csv','w',encoding='utf8',newline='') as f:
    thewriter = writer(f)
    header = ['Business_Name','Address','Jobs_Retained','Date_Approved']
    thewriter.writerow(header)
    for item in p.absolute_links:
        url1 = item
        r=requests.get(url1)
        soap =BeautifulSoup(r.text,'html.parser')
        tablel= soap.find('div',class_='panel-body')
        
        #for ten in tablel.find_all('td'):
        #    print(ten)
        Business_Name = tablel.find_all('td')[3].text
        Address = tablel.find_all('td')[5].text
        Jobs_Retained = tablel.find_all('td')[17].text
        Date_Approved = tablel.find_all('td')[19].text
        
        info = [Business_Name,Address,Jobs_Retained,Date_Approved]
        thewriter.writerow(info)
        
        
jj = pd.read_csv('jen.csv')

st.dataframe(jj)
lenn = len(jj)
st.write(f'total: {lenn}')

  
    

        

    
    

