from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

relative_path = './resume.pdf' 
absolute_path = os.path.abspath(relative_path)

def print_green(text):
    print('\033[32m' + text + '\033[0m')

def print_red(text):
    print('\033[31m' + text + '\033[0m')


cover_letter="""I'm Sanyam Jain, and I am thrilled to express my interest in this role. I am skilled and experienced in Frontend Development. 

With more than 1 year of experience in frontend development, I have a strong foundation in HTML, CSS, and JavaScript. I am also proficient in using modern frontend frameworks like React to build dynamic and responsive web applications. I am constantly learning and staying updated with the latest industry trends and best practices.

Throughout my career, I have successfully collaborated with designers, backend developers, and managers to bring projects to life.

Some Achievements:

# Among top 15 finalists at Vihaan 6.0 Hackathon organized by IEEE DTU.
# Mentor at AccioJob.
# Development Coordinator at DTU Times.
# Volunteering: Taught underprivileged students in Teach for India NGO.
# Technical Head at Dcoder DTU.
"""
success=0
failed=0 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://jobs.lever.co/talentkompass-deutschland?team=Frontend%20Development")
apply_btns = driver.find_elements(By.CLASS_NAME,'posting-btn-submit')

for apply_btn in apply_btns:
    apply_btn.click()
    appy_for_this_job_btn=driver.find_element(By.CLASS_NAME,'postings-btn')
    appy_for_this_job_btn.click()
    resume_btn=driver.find_element(By.ID,'resume-upload-input')
    resume_btn.send_keys(absolute_path)
    wait = WebDriverWait(driver, 10)
    success_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='resume-upload-label']")))

    if success_element is not None:
        success+=1
        print(success_element.text)
        print_green("Resume Uploaded Successfully! "+str(success))
    else:
        failed+=1
        print_red("Failed! "+str(failed))

    extra_info=driver.find_element(By.ID,"additional-information")
    extra_info.send_keys(cover_letter)
    driver.find_element(By.ID,"btn-submit").click()

    break





