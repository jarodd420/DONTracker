'''
Test Cases ID(s):   3.4.1.2_TC_001

Test Case Title:    ADD COMMENT WITH ATTACHMENTS TO A TASKER

Objectives:         This SQT contains test steps and verifications for exporting an audit log for a file located in My Files.

Description:        Audit logs can be exported for files and folders located in My Files and a site’s Document Library.
                    Audit logs can be exported in three (3) file formats: Excel, Word, and PDF, are exported directly to the user,
                    and can be saved in any location. Exported audit logs are automatically named after the file or folder being
                    exported and include the date of export; however, the file name can be edited if desired. Before exporting an
                    audit log, the user can manipulate the content such as hiding columns and moving columns in a desired order.
                    Exported audit logs are sorted by timestamp from most recent entry to oldest. Exported audit logs also include a
                    footer displaying a timestamp of the date and time of export, with the exception of Excel files. In previous
                    versions of DON TRACKER, exporting an audit log for files and folders located in My Files and a site’s Document
                    Library wasn’t available; a user could only view an audit log.

Pre-requisites:     1. 1. Testers have been granted the appropriate Roles/Permissions to complete their Assigned Steps (see Constraints).

Constraints:        1. Tasker inbox style is set to detail view.
                    2. Any type of tasker has been sent with any combination of actions.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver_status = "good"
test_status = "good"
########################## LOG INTO DON TRACKER #########################################
try:
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox()

    #driver = webdriver.Firefox()

    driver.get("https://test.dontracker.navy.mil")
    driver.find_element_by_id("button-1005-btnIconEl").click()
    driver.implicitly_wait(5) #seconds
    print("PASS STEP 1: Login to DON TRACKER as a user.")
except:
    print("Could not lanuch webdriver or URL")
    exit()
##########################################################################################

########################## CLICK 'HEADER_MY_FILES_text' ##################################

driver.find_element_by_id("HEADER_MY_FILES_text").click()


##########################################################################################

########################## getting an element and performing hover action ################

hover_element = driver.find_element_by_xpath("//a[contains(text(),'Tasker Space')]")

hover = ActionChains(driver).move_to_element(hover_element)
hover.perform()

##########################################################################################
#driver.find_element_by_xpath("//div[5]/div[4]/a/span").click()
driver.find_element_by_xpath("//div[4]/a/span").click()
driver.find_element_by_xpath("//div[5]/div[4]/a/span").click()

####################### GET INTO THE NEW POP-UP WINDOW ##################################
main_window_handle = driver.current_window_handle
for handle in driver.window_handles:
    if handle != main_window_handle:
        popup_window_handle = handle
        break

driver.switch_to.window(popup_window_handle)

driver.implicitly_wait(10) #seconds

#driver.find_element_by_xpath("//div[3]/div/div/div[2]/div/div").click()
#element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"datecolumn-1015-triggerEl")))
#driver.find_element_by_id("datecolumn-1015-triggerEl").click()
driver.find_element_by_id("button-1020-btnInnerEl").click()
#driver.find_element_by_xpath("//div[4]/a/span").click()