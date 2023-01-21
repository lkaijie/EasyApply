# indeed scraper application
import requests
from bs4 import BeautifulSoup
import csv


URL = "https://www.indeed.com/jobs?q=data+scientist+%2420%2C000&l=New+York&start=10"
page = requests.get(URL)

soup = BeautifulSoup(page.text, "html.parser")

print(soup.prettify())

# Extract job title, company, location, and salary information
for div in soup.find_all(name="div", attrs={"class":"row"}):
    # Specify the HTML elements that contain the information
    title_element = div.find("a", attrs={"data-tn-element":"jobTitle"})
    company_element = div.find("span", attrs={"class":"company"})
    location_element = div.find("span", attrs={"class":"location"})
    salary_element = div.find("span", attrs={"class":"salaryText"})

    # Extract the text from the elements
    title = title_element.text.strip() if title_element else "N/A"
    company = company_element.text.strip() if company_element else "N/A"
    location = location_element.text.strip() if location_element else "N/A"
    salary = salary_element.text.strip() if salary_element else "N/A"

    # Print the extracted information
    print("Title:", title)
    print("Company:", company)
    print("Location:", location)
    print("Salary:", salary)
    print("---"*10)
print("Done")