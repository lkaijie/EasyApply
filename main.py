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
    glassdoor_jobs = scraper.get_jobs_glassdoor("https://www.glassdoor.com/Job/canada-software-intern-jobs-SRCH_IL.0,6_IN3_KO7,22_IP5.htm?includeNoSalaryJobs=true&pgc=AB4ABIEAeAAAAAAAAAAAAAAAAfguUPkAOQEBAQ8AtXNCwoLC1efs%2Fta6qygcKyqG%2FVg4HjhTQV7WY8UDX6AA9crtyQfPh9BthtnMqncrpXBuPwAA")
    scraper.create_csv(glassdoor_jobs, "glassdoor_jobs")
    time.sleep(1)
    google_jobs = scraper.get_jobs_googlelisting("https://www.google.com/search?q=computing+science+intern+canda&ei=RtDmY_jjAuS30PEP29efCA&uact=5&oq=computing+science+intern+canda&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCCEQoAEQCjIHCCEQoAEQCjIHCCEQoAEQCjIHCCEQoAEQCjIECCEQFTILCCEQFhAeEPEEEB06CggAEEcQ1gQQsAM6BQghEKABOggIIRAWEB4QHToJCAAQFhAeEPEEOgUIABCGA0oECEEYAEoECEYYAFCPIFioImCxI2gCcAF4AIABowGIAbwEkgEDMC40mAEAoAEByAEIwAEB&sclient=gws-wiz-serp&ibp=htl;jobs&sa=X&ved=2ahUKEwjjp-f-ioz9AhVhIn0KHQXzB38QudcGKAF6BAgYECk#htivrt=jobs&fpstate=tldetail&htichips=date_posted:today&htischips=date_posted;today&htidocid=svzAopNcfaAAAAAAAAAAAA%3D%3D")
    scraper.create_csv(google_jobs, "google_jobs")
    time.sleep(1)
    scraper.driver_quit()
    
    # test = scraper.get_jobs_glassdoor("https://www.glassdoor.com/Job/canada-software-intern-jobs-SRCH_IL.0,6_IN3_KO7,22_IP5.htm?includeNoSalaryJobs=true&pgc=AB4ABIEAeAAAAAAAAAAAAAAAAfguUPkAOQEBAQ8AtXNCwoLC1efs%2Fta6qygcKyqG%2FVg4HjhTQV7WY8UDX6AA9crtyQfPh9BthtnMqncrpXBuPwAA")
    # for i in test:
    #     print(i)
    # # jobs = indeed_jobs.get_jobs_indeed  ()
    # # indeed_jobs.create_csv(jobs, "jobs_scraped")
    
    # test2 = scraper.get_jobs_googlelisting("https://www.google.com/search?q=computing+science+intern+canda&ei=RtDmY_jjAuS30PEP29efCA&uact=5&oq=computing+science+intern+canda&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCCEQoAEQCjIHCCEQoAEQCjIHCCEQoAEQCjIHCCEQoAEQCjIECCEQFTILCCEQFhAeEPEEEB06CggAEEcQ1gQQsAM6BQghEKABOggIIRAWEB4QHToJCAAQFhAeEPEEOgUIABCGA0oECEEYAEoECEYYAFCPIFioImCxI2gCcAF4AIABowGIAbwEkgEDMC40mAEAoAEByAEIwAEB&sclient=gws-wiz-serp&ibp=htl;jobs&sa=X&ved=2ahUKEwjjp-f-ioz9AhVhIn0KHQXzB38QudcGKAF6BAgYECk#htivrt=jobs&fpstate=tldetail&htichips=date_posted:today&htischips=date_posted;today&htidocid=svzAopNcfaAAAAAAAAAAAA%3D%3D")
    # for i in test2:
    #     print(i)

if __name__ == "__main__":
    main()