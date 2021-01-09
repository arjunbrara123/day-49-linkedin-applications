from selenium import webdriver
import os

LINKEDIN_USERNAME = os.environ['LINKEDIN_USERNAME']
LINKEDIN_PASSWORD = os.environ['LINKEDIN_PASSWORD']

chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/feed/")

btn_goto_signin = driver.find_element_by_class_name('main__sign-in-link')
btn_goto_signin.click()

input_email = driver.find_element_by_xpath('//*[@id="username"]')
input_email.send_keys(LINKEDIN_USERNAME)
input_password = driver.find_element_by_xpath('//*[@id="password"]')
input_password.send_keys(LINKEDIN_PASSWORD)
btn_signin = driver.find_element_by_xpath('//*[@id="app__container"]/main/div[3]/form/div[3]/button')
btn_signin.click()

driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=101165590&keywords=python%20developer&location=United%20Kingdom')

msg_close = driver.find_element_by_class_name('msg-overlay-bubble-header__control')
msg_close.click()

job_posts = driver.find_elements_by_class_name('job-card-container--clickable')

for post in job_posts:
    post.click()

    btn_apply = driver.find_element_by_class_name('jobs-s-apply button')
    btn_apply.click()
    breakpoint()

breakpoint()
