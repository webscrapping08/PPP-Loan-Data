import streamlit as st

from requests_html  import  HTMLSession
from bs4 import BeautifulSoup
import requests
from csv import writer

import pandas as pd
st.set_page_config(page_title="Onlone jobe.ph",page_icon=":tada:",layout="wide")
st.title (':tada: Searchable PPP Loan Data :tada:')

st.write('Please wait for the data . it will reload 50 Because the site . is no pagenation and randomly give data . pleasee see on site https://pppreport.org/ ')
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

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(jj)

st.download_button(
    label="Download data as Csv",
    data=csv,
    file_name='Result.csv',
    mime='text/csv',
)


st.write('Create by Allan Paul Dela Cruz')
    

        

    
    

