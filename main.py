import EasyApply
import time


def main():
    scraper = EasyApply.scrape("https://ca.indeed.com/jobs?q=software+intern&fromage=1&vjk=8280af2280ba31d1")
    # glassdoor_jobs
    # linkedin_jobs
    # talent_jobs

    indeed_jobs = scraper.get_jobs_indeed("https://ca.indeed.com/jobs?q=software+intern&fromage=1&vjk=8280af2280ba31d1")
    scraper.create_csv(indeed_jobs, "indeed_jobs")
    time.sleep(1)
    glassdoor_jobs = scraper.get_jobs_glassdoor("https://www.glassdoor.com/Job/canada-software-intern-jobs-SRCH_IL.0,6_IN3_KO7,22.htm?fromAge=3")
    scraper.create_csv(glassdoor_jobs, "glassdoor_jobs")
    time.sleep(1)
    google_jobs = scraper.get_jobs_googlelisting("https://www.google.com/search?q=computing+science+intern+canda&ei=RtDmY_jjAuS30PEP29efCA&uact=5&oq=computing+science+intern+canda&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCCEQoAEQCjIHCCEQoAEQCjIHCCEQoAEQCjIHCCEQoAEQCjIECCEQFTILCCEQFhAeEPEEEB06CggAEEcQ1gQQsAM6BQghEKABOggIIRAWEB4QHToJCAAQFhAeEPEEOgUIABCGA0oECEEYAEoECEYYAFCPIFioImCxI2gCcAF4AIABowGIAbwEkgEDMC40mAEAoAEByAEIwAEB&sclient=gws-wiz-serp&ibp=htl;jobs&sa=X&ved=2ahUKEwjjp-f-ioz9AhVhIn0KHQXzB38QudcGKAF6BAgYECk#htivrt=jobs&fpstate=tldetail&htichips=date_posted:today&htischips=date_posted;today&htidocid=svzAopNcfaAAAAAAAAAAAA%3D%3D")
    scraper.create_csv(google_jobs, "google_jobs")
    time.sleep(1)
    # https://ca.talent.com/jobs?context=&k=Software+Engineer+Intern&l=Edmonton%2C+Alberta&id=b0462c848355


    # to add https://ca.jobrapido.com/Software-Engineering-Intern-jobs-in-Canada?shm=all&sortby=publish_date
    # https://www.workopolis.com/jobsearch/find-jobs?ak=software+development+intern&l=&sr=100&t=15&job=CASdfyplYSQNUmyf8r7Jj_7XMaAzuFL2QTWKjfJ-S4r8HOu6BeFfDAX4Q_e2nlZg
    scraper.driver_quit()
    

if __name__ == "__main__":
    main()
    