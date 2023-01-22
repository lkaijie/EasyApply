import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
import requests
from bs4 import BeautifulSoup





# does not work because i am apparently banned from indeed







# driver = webdriver.Chrome(ChromeDriverManager().install())
# # start the browser in full screen
# driver.minimize_window()
# driver.maximize_window()

url = "https://ca.indeed.com/jobs?q=software+intern&fromage=1&vjk=f4112d1451a84ec2"
url2 = "https://ca.indeed.com/jobs?q=&l=Calgary%2C+AB&from=searchOnHP&vjk=181141f55ab488e0"
options = webdriver.ChromeOptions() 
options.headless = True 
# driver.get(url)
with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver: 
    driver.get(url)
    print("Page URL:", driver.current_url) 
    driver.implicitly_wait(2)
    html = driver.page_source
    encode = (html.encode('utf-8'))
    time.sleep(0)
    driver.quit()
    soup = BeautifulSoup(html, "html.parser")
    print(soup)
    for div in soup.find_all(name="div", attrs={"class":"job_seen_beacon"}):
        title = div.find("span").text
        location = div.find("div", attrs={"class":"companyLocation"}).text
        job_url = div.find("a",).get("href")
        days_ago = div.find("span", attrs={"class":"date"}).text
        company_name = div.find("span", attrs={"class":"companyName"}).text
        print("Title:", title)
        print("Location:", location)
        try:
            a = div.find("div", attrs={"class":"attribute_snippet"})
            salary = a.text
            print("Salary/Info:", salary)
        except:
            print("Salary/Info: N/A")
        print("Company:", company_name)
        print("Days ago:", days_ago.replace("PostedPosted", ""))
        print("URL: https://ca.indeed.com"+job_url)
        print("")
        print("")
