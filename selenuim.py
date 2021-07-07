import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MoreThanTwoWindows(unittest.TestCase) :
	def test_browser_Window(self):

			# open chrome browser
			driver = webdriver.Chrome(executable_path=r'D:PATHchromedriver.exe')
			# set implicit time to 30 seconds
			driver.implicitlyWait(30)
			# navigate to the url
			driver.get("https://chercher.tech/python/windows-selenium-python")
			# get the Session id of the Parent
			parentGUID = driver.current_window_handle
			# click the button to open new window
			driver.find_element_by_id("three-window").click()
			time.sleep(5000)
			# get the All the session id of the browsers
			allGUID = driver.window_handles
			# print number of windows
			print("Total Windows : "+allGUID.size())
			# iterate through windows
			for guid in  allGUID:
				driver.switch_to_window(guid)
				# check the title of the page to match with "bing"
				if("bing" in driver.title.lower()):
					driver.findElementBy.className("b_searchbox").send_keys("gates")
					time.sleep(3000)
					break


			# close all the windows
			driver.quit(


class TwoWindows(unittest.TestCase) :
	def test_browser_Window :
		# open chrome browser
		driver = webdriver.Chrome(executable_path=r'D:PATHchromedriver.exe')
		# set implicit time to 30 seconds
		driver.implicitlyWait(30)
		# navigate to the url
		driver.get("https://chercher.tech/python/windows-selenium-python")
		# get the Session id of the Parent
		parentGUID = driver.current_window_handle
		# click the button to open new window
		driver.find_element_by_id("two-window").click()
		time.sleep(5000)
		# get the All the session id of the browsers
		allGUID = driver.window_handles
		# print the title of the page
		print("Page title before Switching : "+ driver.getTitle())
		print("Total Windows : "+allGUID.size())
		# iterate the values in the set
		for guid in all allGUID:
			# one enter into if blobk if the GUID is not equal to parent window's GUID
			if(guid != parentGUID):
				# switch to the guid
				driver.switch_to_window(guid)
				# break the loop
				break


		# search on the google page
		driver.find_element_by_name("q").send_keys("success")
		# print the title after switching
		print("Page title after Switching to goolge : "+ driver.getTitle())
		time.sleep(5000)
		# close the browser
		driver.close()
		# switch back to the parent window
		driver.switch_to_window(parentGUID)
		# print the title
		print("Page title after switching back to Parent: "+ driver.getTitle())