import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time

def scrapper(link,file_name):
    print(link,file_name)

    dataframe = pd.DataFrame(columns=['Job Name', 'Company Name','Location','Salary','Description'])

    for i in range(0,800,10):
        url = link+str(i)
        r = requests.get(url)
        htmlcontent = r.content
        

        soup = BeautifulSoup(htmlcontent, 'html.parser')
        

    
        job_container = soup.find_all('div', class_='result')
        
        print('*'*160)
        for job in job_container:
            
            try:
                job_name = job.find("h2", class_="title").text.strip().replace('new','').replace('\n','')

            except:
                job_name = 'NA'

            try:
                company_name = job.find("span", class_="company").text.strip().replace('\n','')
            
            except:
                company_name = 'NA'

            try:
                job_location = job.find("span", class_="location").text.strip().replace('\n','')
            
            except:
                job_location = 'NA'

            try:
                salary = job.find("span", class_="salaryText").text.strip().replace('₹','').replace('\n','').replace(' a month','').replace(',','').replace(' a year','')
            
            except:
                salary = 'NA'

            try:
                summary = job.find("div", class_="summary").text.strip().replace('\n','')
                
            
            except:
                summary = 'NA'



            
            
        try:
            print('Job Name:- ',job_name, 'Company Name:-',company_name,
                'Location:-', job_location,'Salary:-', salary, 'Summary:-', summary)     
                    
            dataframe = dataframe.append({'Job Name':job_name, 'Company Name':company_name,
                'Location':job_location,'Salary':salary, 'Description': summary},ignore_index=True)
            
            dataframe.to_csv(file_name+'.csv',index=False)
        except Exception as e:
            print('Error:-',e)






if __name__=='__main__':
    scrapper("https://www.indeed.co.in/jobs?q=web+developer&l=India&start=",'Web_Developer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=android+developer&l=India&start=",'Android_Developer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=ios+developer&l=India&start=",'iOS_Developer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=react+native+developer&l=India&start=",'React_Native_Developer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=flutter+developer&l=India&start=",'Flutter_Developer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=react+js+developer&l=India&start=",'React_Js_Developer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=full+stack+developer&l=India&start=",'Full_Stack_Developer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=python+developer&l=India&start=",'Python_Developer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=java+developer&l=India&start=",'Java_Developer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=node+js+developer&l=India&start=",'Node_Js_Developer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=php+developer&l=India&start=",'PHP_Developer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=mean+stack+developer&l=India&start=",'MEAN_Stack_Developer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=mern+stack+developer&l=India&start=",'MERN_Stack_Developer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=data+scientist&l=India&start=",'Data_Scientist')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=data+analyst&l=India&start=",'Data_Analyst')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=business+analyst&l=India&start=",'Business_Analyst')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=backend+developer&l=India&start=",'Backend_Developer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=game+developer&l=India&start=",'Game_Developer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=game+artist&l=India&start=",'Game_Artist')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=game+designer&l=India&start=",'Game_Designer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=machine+learning&l=India&start=",'Machine_Learning')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=artificial+intelligence&l=India&start=",'Artificial_Intilligence')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=deep+learning&l=India&start=",'Deep_Learning')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=ui+ux+developer&l=India&start=",'UI_UX_Developer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=cloud+computing&l=India&start=",'Cloud_Computing')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=devops+engineer&l=India&start=",'Devops_Engineer')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=system+administrator&l=India&start=",'System_Administrator')
    time.sleep(120)
    scrapper("https://www.indeed.co.in/jobs?q=network+security+engineer&l=India&start=",'Network_Security_Engineer')
    print("*"*15,'END',"*"*15)










# android_dev.shape
# ai
# backend_dev.shape
# business_analyst.shape
# cloud_computing.shape
# data_analyst.shape
# data_scientist.shape
# deep_learning.shape
# devops.shape
# flutter_dev.shape
# full_stack_dev.shape
# game_artist.shape
# game_designer.shape
# iOS_dev.shape
# java_dev.shape
# ml.shape
# mean.shape
# mern.shape
# net_security_engg.shape
# node_js.shape
# php_dev.shape
# py_dev.shape
# react_js.shape
# react_native_dev.shape
# sys_admin.shape
# ui_ux.shape
# web_dev.shape

# android_dev, ai, backend_dev, business_analyst, cloud_computing, data_analyst, data_scientist, deep_learning, devops, 
# full_stack_dev, game_artist, game_designer, iOS_dev, java_dev, ml, mean, mern, net_security_engg,
# node_js, php_dev, py_dev, react_js, react_native_dev, sys_admin, ui_ux, web_dev,



# android_dev['Salary'].fillna('',inplace=True)
# android_dev