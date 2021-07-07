from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pprint import pprint
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

chrome_driver_path = r"C:\Users\tramr\OneDrive\Desktop\website\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2599001570&geoId=103104382&keywords=python%20developer&location=Los%20Angeles%20County%2C%20California%2C%20United%20Statesn")
# storing the current window handle to get back to dashbord
main_page = driver.current_window_handle
driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]").click()

# wait for page to load completely
time.sleep(5)
# changing the handles to access login page
    # if handle != main_page:
    #     # change the control to signin page
    #     driver.switch_to.window(handle)
    #     driver.implicitly_wait(15)
# for handle in driver.window_handles:
#     if handle != main_page:
#         driver.switch_to.window(handle)
#         break


email = driver.find_element_by_id("username")
email.send_keys("")
password = driver.find_element_by_id("password")
password.send_keys("")
sign_in = driver.find_element_by_css_selector("button")
sign_in.send_keys(Keys.ENTER)

time.sleep(5)
#getting all the clickable elements
jobs_list = driver.find_elements_by_css_selector(".job-card-container--clickable")

for job in jobs_list:
    print("'''''''''''''''''''''''''''''''"+job.text)
    job.click()
    try:
        # Getting apply button
        driver.find_element_by_css_selector(".jobs-s-apply button").click()

        time.sleep(2)

    except NoSuchElementException:
        print("Complex application")




# driver.implicitly_wait(60*5)
time.sleep(1*60)
driver.quit()