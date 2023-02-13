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

class scrape:
    def __init__(self, url): # url with selected filters
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.minimize_window()
        self.job_list = []
        self.days_ago = ""
        self.title = ""
        self.location = ""
        self.company_name = ""
        self.salary = ""
        self.job_url = ""
        self.jobcsv = ""
        self.csv_created = False
        self.wait_time = 1
    
    def get_jobs_indeed(self, url):
        self.get_soup_indeed(url)
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
    def get_jobs_glassdoor(self, url):
        self.get_soup(url)
        job_list = []
        for div in self.soup.find_all(name="li", attrs={"class":"react-job-listing"}):
            url = div.find("a", attrs={"class":"jobLink"}).get("href")
            company_name = div.find("a", attrs={"class":"jobLink"}).get("title")
            days_ago = div.find("div", attrs={"data-test":"job-age"}).text
            location = div.find("span", attrs={"class":"css-3g3psg pr-xxsm css-iii9i8 e1rrn5ka0"}).text  # this might break in the future
            title = div.find("a", attrs={"data-test":"job-link"}).find("span").text   
            try:
                salary = div.find("span", attrs={"data-test":"detailSalary"}).text
                est = div.find("span", attrs={"class":"css-0 e1wijj240"}).text
            except:
                salary = "N/A"
                est = ""
            job_url = "https://www.glassdoor.com" + url
            now = datetime.now()
            current_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            job_list.append([title, company_name, location, salary, days_ago, current_time, job_url])
        self.job_list = job_list
        return self.job_list

    def get_jobs_googlelisting(self, url):
        self.get_soup(url)
        job_list = []
        for div in self.soup.find_all(name="li", attrs={"class":"iFjolb gws-plugins-horizon-jobs__li-ed"}):        
            url = div.find("span", attrs={"class":"DaDV9e"})
            try:
                url = url.find("a").get("href")
            except:
                pass
            title = div.find("div", attrs={"class":"BjJfJf PUpOsf"}).text
            company_name = div.find("div", attrs={"class":"vNEEBe"}).text
            location = div.find("div", attrs={"class":"Qk80Jf"}).text
            days_ago = div.find("span", attrs={"class":"LL4CDc"}).find("span").text
            try:
                print("URL: "+url)
            except:
                pass
            salary = "N/A"
            job_url = url
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
        data = pd.read_csv(self.jobcsv, encoding = "ISO-8859-1")
        data.drop_duplicates(subset=['Title','Company','Location'], keep='first', inplace=True)
        data.to_csv(self.jobcsv, index=False)


    def export_to_csv(self, info, name):
        # name = name+".csv"
        with open(name, "a", newline="") as f:
            writer = csv.writer(f)
            for x in info:
                writer.writerow(x)

        data = pd.read_csv(self.jobcsv, encoding = "ISO-8859-1")
        data.drop_duplicates(subset="URL", keep='first', inplace=True)
        data.to_csv(self.jobcsv, index=False)


    def get_soup(self, url):
        self.url = url
        self.driver.get(self.url)
        self.driver.implicitly_wait(20)
        # time.sleep(self.wait_time)
        time.sleep(1)
        self.html = self.driver.page_source
        self.encode = (self.html.encode('utf-8'))
        # self.driver.quit()
        self.soup = BeautifulSoup(self.html, "html.parser")
        return self.soup

    def get_soup_indeed(self, url):
        self.url = url
        self.driver.get(self.url)
        self.driver.implicitly_wait(20)
        # time.sleep(self.wait_time)
        time.sleep(5)
        self.html = self.driver.page_source
        self.encode = (self.html.encode('utf-8'))
        # self.driver.quit()
        self.soup = BeautifulSoup(self.html, "html.parser")
        return self.soup


    def set_wait_time(self, time):
        self.wait_time = time

    def driver_quit(self):
        self.driver.quit()