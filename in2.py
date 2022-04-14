from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import  csv
from bs4 import BeautifulSoup as bs 
import  pandas as pd
import requests


page=['https://in.indeed.com/jobs?q=dot%20net%20developer&l=Mumbai%2C%20Maharashtra&vjk=9ed29808e9d88131',
       'https://in.indeed.com/jobs?q=dot%20net%20developer&l=Mumbai%2C%20Maharashtra&start=10&vjk=cba4dcfcd5d01203',
       'https://in.indeed.com/jobs?q=dot%20net%20developer&l=Mumbai%2C%20Maharashtra&start=20&vjk=0f0080c86715d252',
       'https://in.indeed.com/jobs?q=dot%20net%20developer&l=Mumbai%2C%20Maharashtra&start=30&vjk=caf6ac7e82e326c1',
       'https://in.indeed.com/jobs?q=dot%20net%20developer&l=Mumbai%2C%20Maharashtra&start=40&vjk=929bd5893068d01e',
       'https://in.indeed.com/jobs?q=dot%20net%20developer&l=Mumbai%2C%20Maharashtra&start=50&vjk=a05242b764f80c09',
       'https://in.indeed.com/jobs?q=dot%20net%20developer&l=Mumbai%2C%20Maharashtra&start=60&vjk=aa061955c97aa633']
titles=[]
comP=[]
location=[]
for url in range(0,7):
    req = requests.get(page[url])
    soup = bs(req.text, 'html.parser')
    job_title=soup.find_all('div',class_='heading4 color-text-primary singleLineTitle tapItem-gutter')
    for job in job_title:
        titles.append(job.text)
    print(titles)
    print(len(titles))
    
    company_name = soup.find_all('div',class_='heading6 company_location tapItem-gutter companyInfo')
    for com in company_name:
        comP.append(com.text)
    print(comP)
    print(len(comP))

    location_name = soup.find_all('div',class_='companyLocation')
    for loc in location_name:
        location.append(loc.text)
    print(location)
    print(len(location))

indeed = pd.DataFrame({
'Titles': titles,
'Company' : comP,
'location': location,

})



#add dataframe to csv file named 'movies.csv'
indeed.to_csv('indeed.csv')
