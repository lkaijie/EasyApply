import csv
from datetime import datetime
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# import requests
from bs4 import BeautifulSoup
import pandas as pd
# clean code from test.py
from os.path import exists

class Indeed:
    def __init__(self, url): # url with selected filters
        self.url = url
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.minimize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(20)
        self.html = self.driver.page_source
        self.encode = (self.html.encode('utf-8'))
        time.sleep(1)
        self.driver.quit()
        self.soup = BeautifulSoup(self.html, "html.parser")
        # self.jobs = []
        self.job_list = []
        self.days_ago = ""
        self.title = ""
        self.location = ""
        self.company_name = ""
        self.salary = ""
        self.job_url = ""
        self.jobcsv = ""
        self.csv_created = False
    
    def get_jobs(self):
        job_list = []
        for div in self.soup.find_all(name="div", attrs={"class":"job_seen_beacon"}):
            title = div.find("span").text
            location = div.find("div", attrs={"class":"companyLocation"}).text
            job_url = div.find("a",).get("href")
            days_ago = div.find("span", attrs={"class":"date"}).text
            company_name = div.find("span", attrs={"class":"companyName"}).text
            print("Location:", location)
            try:
                a = div.find("div", attrs={"class":"attribute_snippet"})

                salary = a.text
                print("Salary/Info:", salary)
            except:
                print("Salary/Info: N/A")
            days_ago = days_ago.replace("PostedPosted", "")
            job_url = "https://ca.indeed.com"+job_url
            now = datetime.now()
            current_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            job_list.append([title, company_name, location, salary, days_ago, current_time, job_url])
        self.job_list = job_list
        return self.job_list

    def create_csv(self, info, name):
        name = name+".csv"
        self.jobcsv = name        
        file_exists = exists(name)
        if self.csv_created == False:
            with open(name, "a", newline="") as f:
                writer = csv.writer(f)
                if file_exists == False:
                    writer.writerow(["Title", "Company", "Location", "Salary", "Days ago", "Date Scraped", "URL"])
                for x in info:
                    writer.writerow(x)

        # self.csv_created = True
        # if self.csv_created == True:
        #     self.export_to_csv(info, name)

    def export_to_csv(self, info, name):
        # name = name+".csv"
        with open(name, "a", newline="") as f:
            writer = csv.writer(f)
            for x in info:
                writer.writerow(x)

        data = pd.read_csv(self.jobcsv, encoding = "ISO-8859-1")
        data.drop_duplicates(subset="URL", keep='first', inplace=True)
        data.to_csv(self.jobcsv, index=False)


# indeed_jobs = Indeed("https://ca.indeed.com/jobs?q=software+intern&fromage=1&vjk=8280af2280ba31d1")
# jobs = indeed_jobs.get_jobs()
# indeed_jobs.export_to_csv(jobs, "jobs2.csv")