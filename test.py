import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome(ChromeDriverManager().install())
# start the browser in full screen
driver.maximize_window()
url = "https://ca.indeed.com/jobs?q=software+intern&fromage=1&vjk=f4112d1451a84ec2"
url2 = "https://ca.indeed.com/jobs?q=&l=Calgary%2C+AB&from=searchOnHP&vjk=181141f55ab488e0"
driver.get(url)
driver.implicitly_wait(20)
html = driver.page_source
encode = (html.encode('utf-8'))
time.sleep(0)
driver.quit()
soup = BeautifulSoup(html, "html.parser")
jobs = []
# for div in soup.find_all(name="h2", attrs={"class":"jobTitle jobTitle-newJob css-bdjp2m eu4oa1w0"}):
#     title = div.find("span").text
#     print("Title:", title)
    # print(title)

for div in soup.find_all(name="div", attrs={"class":"job_seen_beacon"}):
    title = div.find("span").text
    location = div.find("div", attrs={"class":"companyLocation"}).text
    job_url = div.find("a",).get("href")
    days_ago = div.find("span", attrs={"class":"date"}).text
    company_name = div.find("span", attrs={"class":"companyName"}).text
    # print(div.find("div", attrs={"class":"companyLocation"}))
    # print(div.find("div", attrs={"class":"attribute_snippet"}))
    # print("")
    # a = div.find("div", attrs={"class":"attribute_snippet"})
    # print("text:")
    # print(a.text)
    # try:
    #         get_salary = div.find("div", attrs={"class":"attribute_snippet"})
    #         salary = get_salary.find("span").text
    #         print(s)
    #     # salary = div.find("div").text
    # except:
    #     salary = "N/A"

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

# soup.find("div", attrs={"class":"job_seen_beacon"})





# results = soup.find_all(name="ul", attrs={"class":"jobsearch-ResultsList css-0"})

# # print(results)
# print(results.find_all(name="li", attrs={"class"}))
# for element in results.find_all(name="li", attrs={"class"}):
#     title = element.find("h2", attrs={"class":"jobTitle jobTitle-newJob css-bdjp2m eu4oa1w0"}).text
#     print("Title:", title)
 


# for li in soup.find_all(name="ul", attrs={"class":"jobsearch-ResultsList css-0"}):
#     title = li.find("h2", attrs={"class":"jobTitle jobTitle-newJob css-bdjp2m eu4oa1w0"})
#     print("Title:", title)














    # # Specify the HTML elements that contain the information
    # title_element = div.find("a", attrs={"data-tn-element":"jobTitle"})
    # company_element = div.find("span", attrs={"class":"company"})
    # location_element = div.find("span", attrs={"class":"location"})
    # salary_element = div.find("span", attrs={"class":"salaryText"})
    # # Extract the text from the elements
    # title = title_element.text.strip() if title_element else "N/A"
    # company = company_element.text.strip() if company_element else "N/A"
    # location = location_element.text.strip() if location_element else "N/A"
    # salary = salary_element.text.strip() if salary_element else "N/A"
    # # Print the extracted information
    # print("Title:", title)
    # print("Company:", company)
    # print("Location:", location)
    # print("Salary:", salary)
    # print("---"*10)







# soup = BeautifulSoup(encode, "lxml")
# print(soup.prettify())

