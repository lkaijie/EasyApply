import EasyApply


def main():
    indeed_jobs = EasyApply.Indeed("https://ca.indeed.com/jobs?q=software+intern&fromage=1&vjk=8280af2280ba31d1")
    jobs = indeed_jobs.get_jobs()
    indeed_jobs.create_csv(jobs, "jobs_scraped")
    

if __name__ == "__main__":
    main()