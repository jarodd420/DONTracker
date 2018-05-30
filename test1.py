'''
Test Cases ID(s):   266-TC-099

Test Case Title:    ADD COMMENT WITH ATTACHMENTS TO A TASKER

Objectives:         This SQT contains test steps and verifications for adding a comment with attachments to a tasker.			

Description:        When adding a comment, the Tasker Actor can add attachments. 
                    Attachment categories have been expanded and include: Final Signed Document, Organizational Response, 
                    Original Source Document, and Reference. The attachment category is a required field and attachments 
                    cannot be added if a category is not designated. When selecting the category magnifying glass, a modal 
                    window appears and when each category is selected, a description is shown in the right panel. 
                    In previous versions of DON TRACKER, the attachment categories included: Enclosure, Final Signed 
                    Document, and Reference. A modal window did not exist.			

Pre-requisites:     1. Testers have been granted the appropriate Roles/Permissions to complete their Assigned Steps (see Constraints).

Constraints:        1. Tasker inbox style is set to detail view.
                    2. Any type of tasker has been sent with any combination of actions.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_status = "good"
test_status = "good"

########################## SETUP FIREFOX PROFILE ########################################

abrahamAzam = webdriver.FirefoxProfile("C:/Users/jared/AppData/Roaming/Mozilla/Firefox/Profiles/4rv3vvf2.AbrahamAzam")

abrahamAzam.set_preference("webdriver_accept_untrusted_certs", True)
#driver = webdriver.Firefox(firefox_profile = abrahamAzam)
driver = webdriver.Firefox(abrahamAzam)
driver.get("https://test.dontracker.navy.mil")
exit()

########################## LOG INTO DON TRACKER #########################################

try:
    #driver = webdriver.Chrome()


    driver.get("https://test.dontracker.navy.mil")
    driver.find_element_by_id("button-1005-btnIconEl").click()
    driver.implicitly_wait(5) #seconds
    print("PASS STEP 1: Login to DON TRACKER as Tasker Actor.")
except:
    print("Could not lanuch webdriver or URL")
    exit()
##########################################################################################

driver.find_element_by_id("HEADER_TASKS_text").click()
driver.find_element_by_link_text("Inbox").click()
#driver.find_element_by_xpath("xpath=(//a[contains(text(),'Inbox')])[2]").click()

driver.implicitly_wait(6) #seconds
#driver.find_element_by_id("button-1033").click()
driver.find_element_by_xpath("//span[contains(text(),'New')]").click()

# BELOW IS IMPORTANT
driver.find_element_by_xpath("//span[contains(text(),'General')]").click()

driver.implicitly_wait(3) #seconds

driver.find_element_by_name("subject").send_keys("266-TC-099-TEST-AUTOMATED")

# Button ID is button-2338-btnE1, check later
driver.find_element_by_xpath("//span[contains(text(),'Send')]").click()

###                  CHECK DATE FIELD IS REQUIRED               #################

date_error = driver.find_element_by_xpath("//div[contains(text(),'Due Date is invalid, reason: This field is required')]")
print(date_error.get_attribute('innerHTML'))
driver.implicitly_wait(3) #seconds
driver.find_element_by_id("button-1005-btnIconEl").click()

#################################################################################

###                  CHECK DATE FIELD FORMAT                    #################
try:
    driver.find_element_by_name("dueDate").send_keys("non-working-date")

    driver.find_element_by_xpath("//span[contains(text(),'Send')]").click()
    date_error = driver.find_element_by_xpath("//div[contains(text(),'it must be in the format m/d/Y')]")
    driver.implicitly_wait(2) #seconds
    driver.find_element_by_id("button-1005-btnIconEl").click()
except:
    print("The Due Date element id's xpaths may have changed")

#################################################################################

###                  SELECT SSIC                                  #################
#driver.find_element_by_class_name("x-form-trigger-input-cell").click()

#driver.find_element_by_xpath("//table[18]/tbody/tr/td[2]/table/tbody/tr/td[2]/div").click(www
#driver.find_element_by_id("trackerTextField-2447-inputEl").send_keys("Military")
driver.find_element_by_xpath("//div[2]/div/div/div/div/div/div/table/tbody/tr/td[2]/input").send_keys("Military")
#trackerTextField-2447-inputEl

driver.find_element_by_xpath("//div[20]/div[2]/div/div/div/div/div/div/a/span/span/span").click()
driver.implicitly_wait(2) #seconds
driver.find_element_by_xpath("//div[2]/div[2]/div/table/tbody/tr/td/div").click()
driver.implicitly_wait(2) #seconds
#driver.find_element_by_xpath("//div[3]/div/div/a/span/span/span").click()
driver.find_element_by_xpath("//span[contains(text(),'Accept')]").click()

#################################################################################

###                  CLEAR AND SELECT VALID DATE                                  #################
driver.find_element_by_name("dueDate").clear()
driver.find_element_by_xpath("//table[15]/tbody/tr/td[2]/table/tbody/tr/td[2]/div").click()
driver.implicitly_wait(2) #seconds
driver.find_element_by_xpath("//tr[2]/td[4]/a").click()

#################################################################################

driver.find_element_by_xpath("//textarea").send_keys("266-TC-099-TEST-AUTOMATED Description and instructions for Tasker")
driver.implicitly_wait(2) #seconds

driver.find_element_by_xpath("//table[19]/tbody/tr/td[2]/textarea").send_keys("JR Comments for Tasker")

###                         ADD KEYWORDS TO FORM    #######################################

driver.find_element_by_xpath("//td[2]/div/span/div/table/tbody/tr/td[2]/input").send_keys("JROD SECDEF TASKER")
driver.implicitly_wait(2) #seconds
###                         SIGNATURE AUTHORITY    #######################################
#action_key_down_w = ActionChains(driver).key_down("w")
#action_key_down_w = ActionChains(driver).key_down("w")
signatureAuthority = driver.find_element_by_name("saDisplayName")
signatureAuthorityId = signatureAuthority.get_attribute("id")
print("ID:" + signatureAuthorityId)
driver.implicitly_wait(10) #seconds

signatureAuthority.send_keys("P")
signatureAuthority.send_keys("r")

#signatureAuthority.send_keys(Keys.CONTROL, "P")
#signatureAuthority.send_keys(Keys.CONTROL, "r")
#driver.implicitly_wait(10) #seconds

signatureAuthority.send_keys(Keys.CONTROL, "P")

#signatureAuthority.send_keys(Keys.TAB)
#signatureAuthority.send_keys(Keys.ARROW_DOWN)

driver.implicitly_wait(30) #seconds
#signatureAuthority.click()
#driver.implicitly_wait(10) #seconds



first_option = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//li")))
time.sleep(2)
signatureAuthority.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
signatureAuthority.send_keys(Keys.RETURN)
#exit()

#################################################################################

#########################       EXTERNAL DCN    #######################################

driver.find_element_by_name("externalDcn").send_keys("Testing External DCN")

#################################################################################

#########################       SUBMIT THE FORM    #######################################

driver.find_element_by_xpath("//span[contains(text(),'Send')]").click()

responder_error = driver.find_element_by_xpath("//div[contains(text(),'Non-Draft Taskers must have at least one responder')]")
print(date_error.get_attribute('innerHTML'))

#################################################################################