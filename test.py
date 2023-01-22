import csv
from datetime import datetime
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import pandas as pd


driver = webdriver.Chrome(ChromeDriverManager().install())
# start the browser in full screen
driver.minimize_window()

url = "https://ca.indeed.com/jobs?q=software+intern&fromage=1&vjk=f4112d1451a84ec2"
url2 = "https://ca.indeed.com/jobs?q=&l=Calgary%2C+AB&from=searchOnHP&vjk=181141f55ab488e0"
seven_days = "https://ca.indeed.com/jobs?q=software+intern&fromage=7&vjk=9e9d4bdff732d2b8"
driver.get(seven_days)
driver.implicitly_wait(20)
html = driver.page_source
encode = (html.encode('utf-8'))
time.sleep(1)
driver.quit()
soup = BeautifulSoup(html, "html.parser")
jobs = []
def export_to_csv(info):
    with open("jobs.csv", "a", newline="") as f:
        writer = csv.writer(f)
        # writer.writerow(["Title", "Company", "Location", "Salary", "Days ago", "URL", "Date Scraped"])
        for x in info:
            writer.writerow(x)
    
    data = pd.read_csv("jobs.csv", encoding = "ISO-8859-1")
    data.drop_duplicates(subset="URL", keep='first', inplace=True)
    data.to_csv("jobs.csv", index=False)


job_list = []
for div in soup.find_all(name="div", attrs={"class":"job_seen_beacon"}):
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
    
    # print("Company:", company_name)
    days_ago = days_ago.replace("PostedPosted", "")
    # print("Days ago:", days_ago)
    job_url = "https://ca.indeed.com"+job_url
    # print("URL: "+job_url)
    # print("")
    # print("")
    now = datetime.now()

    current_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    job_list.append([title, company_name, location, salary, days_ago, current_time, job_url])
    

export_to_csv(job_list)