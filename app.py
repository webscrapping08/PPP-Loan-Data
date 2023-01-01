from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
import requests
from csv import writer
import time

st.set_page_config(page_title="Onlone jobe.ph",page_icon=":tada:",layout="wide")

st.title(':tada: Online job Philippines filter using Python Web scrapping:tada:')

st.write(f'Please reload this page after 3min to reload update for onlinejob.ph this show 480 result for example . Please see the website to see on https://www.onlinejobs.ph/jobseekers/jobsearch')
apple = pd.read_excel('apple.xlsx')

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(apple)

st.download_button(
    label="Download data as Csv :tada:",
    data=csv,
    file_name='Result.csv',
    mime='text/csv',
)

st.dataframe (apple)
lenn = len(apple)
st.write(f'Total : {lenn}')
def extract(page):
    url = f'https://www.onlinejobs.ph/jobseekers/jobsearch/{page}'
    page=requests.get(url)

    soap = BeautifulSoup (page.content,'html.parser')
    
    return soap



        

def transform(soap):
    lists =soap.find_all('div',class_='jobpost-cat-box latest-job-post card-hover-default')

    with open ('apple.csv','w',encoding='utf8',newline='') as f:
        thewrite = writer(f)
        header=['Title', 'Salary', 'Posted']
        thewrite.writerow(header)
        for list in lists:
            Title = list.find('h4',class_= 'fs-16 fw-700').text.replace('Full Time','').replace('Part Time ','').replace('Freelance ','').replace('Any ','').strip()
            Salary = list.find('dd',class_= 'col').text
            Posted = list.find('em').text
            
            info = [Title, Salary, Posted]
            thewrite.writerow(info)
            
            
            job = {
                'Title' : Title,
                'Salary' :Salary,
                'Posted' : Posted,
            }
            joblist.append(job)
        return joblist
            
            
if __name__ == '__name__':
    while True :
        transform()
        time.sleep(3)
               

            
joblist = []

for i in range(0,80,5):
    
    c = extract(i)
    transform(c)
        
        
df=pd.DataFrame(joblist)

df.to_excel('apple.xlsx',index=False)





print(df)