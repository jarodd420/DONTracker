'''
SEND GENERAL PARALLEL TASKER WITH ATTACHMENTS

This SQT contains test steps and verifications for sending a general parallel tasker with attachments.

During tasker creation, the Tasker Originator can add attachments. Attachment categories have been expanded and include:
Action/Info Memo, Draft Response, Incoming Letter, Organizational Response, Original Source Document, Reference,
and Working Document. The attachment category is a required field and attachments cannot be added if a category is not
designated. When selecting the category magnifying glass, a modal window appears and when each category is selected, a
description is shown in the right panel. In previous versions of DON TRACKER, the attachment categories included: Draft
Response, Enclosure, Incoming Letter, Reference, and Working Document. A modal window did not exist.

1. Testers have been granted the appropriate Roles/Permissions to complete their Assigned Steps (see Constraints).

1. Tasker Originator, Responder 1, and Responder 2 are three (3) different users.
2. Tasker Originator is a Tasker Coordinator and belongs to [Organization 1].
3. Responder 1 is a Tasker Coordinator and belongs to [Organization 2].
4. Responder 2 is a Tasker Coordinator and belongs to [Organization 3].
5. Tasker inbox style is set to detail view.

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

code_status = "good"
test_status = "good"
ffOptions = webdriver.FirefoxOptions()
task_originator = webdriver.FirefoxProfile("AbrahamAzam") #Task originator is Abraham Azam who is a task coordinator belonging to TEST-1
responder1 = webdriver.FirefoxProfile("AmyeAbdulla") #Responder 1 is Amye Abdulla who is a task coordinator belonging to TEST-B1
responder2 = webdriver.FirefoxProfile("TreenTsuyoshi") #Responder 2 is Treen Tsuyoshi who is a task coordinator belonging to TEST-C1C

task_originator.accept_untrusted_certs = True
task_originator.assume_untrusted_cert_issuer = True

task_originator.set_preference("webdriver_accept_untrusted_certs", True)

# Step 1: Login to DON TRACKER as Tasker Originator.
try:
    driver = webdriver.Firefox(firefox_profile=task_originator)
    driver.get("https://test.dontracker.navy.mil")

    driver.find_element_by_id("button-1005-btnIconEl").click()
    driver.implicitly_wait(8)  # seconds
except:
    test_status = "bad: element 'button-1005-btnIconEl' does not exist"
    print(test_status)
    exit()

# Step 2: Click the Taskers tab and select Inbox from the drop down list.

try:
    element = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.ID, "HEADER_TASKS_text")))
    driver.find_element_by_id("HEADER_TASKS_text").click()
    driver.implicitly_wait(1)  # seconds
except:
    test_status = "bad: element 'HEADER_TASKS_text' does not exist"
    print(test_status)
    exit()

try:
    driver.find_element_by_link_text("Inbox").click()
    driver.implicitly_wait(5)  # seconds
except:
    test_status = "bad: element 'Inbox' does not exist"
    print(test_status)
    exit()

# Step 3: Click the inbox down arrow and select TEST-1 inbox.
try:
    driver.find_element_by_xpath("//td[starts-with(@id, 'ext-gen')]").click()
    driver.implicitly_wait(1)  # seconds

except:
    test_status = "bad: element '//td[starts-with(@id, 'ext-gen')]' failed or does not exist"
    print(test_status)
    exit()

try:
    blist = driver.find_element_by_xpath("//div[starts-with(@id, 'boundlist-')]")

    items = blist.find_elements_by_tag_name("li")
    for item in items:
        if item.text == "TEST-1":
            item.click()

    driver.implicitly_wait(5)  # seconds
except:
    test_status = "bad: element '//div[starts-with(@id, 'boundlist-')]' failed or does not exist"
    print(test_status)
    exit()

# Step 4: Click the New button and select General from the drop down list.
#driver.find_element_by_xpath("//span[starts-with(@id, 'button-')]//span[starts-with(@class, 'x-btn-wrap')]").click()

try:
    driver.implicitly_wait(10)
    buttonList = driver.find_elements_by_xpath("//span[starts-with(@id, 'button-')]")
    for item in buttonList:
        if "New" in item.text:
            try:
                #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(item))
                print(item.get_attribute("id"))
                print(item.text)
                print(item.get_attribute("class"))
                if item.get_attribute("class") == "x-btn-button":
                    print("item clicked")
                    #element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(item))
                    item.click()
                print("item is clickable")
            except:
                print("item is NOT clickable")
                print(item.id)
                print(item.text)
except:
    test_status = "bad: element '//span[starts-with(@id, 'button-')]' failed or does not exist"
    print(test_status)
    exit()
try:
    menuItemList = driver.find_elements_by_xpath("//span[starts-with(@id, 'menuitem-')]")

    for item in menuItemList:
        print(item.tag_name + " " + item.text)
        if item.text == "General":
            item.click()

except:
    test_status = "bad: element '//span[starts-with(@id, 'menuitem-')]' failed or does not exist"
    print(test_status)
    exit()

# Step 5: Enter text in the Subject field.

try:
    driver.find_element_by_name("subject").send_keys("AUTOMATED Test Case 266-TC-001")
except:
    test_status = "bad: find_element_by_name('subject') failed or does not exist"
    print(test_status)
    exit()

# Step 6: Click the calendar picker widget in the Due Date field and select a date.

try:
    driver.find_element_by_xpath("//div[starts-with(@class, 'x-trigger-index-0 x-form-trigger x-form-date-trigger')]").click()
    #driver.find_element_by_xpath("//div[starts-with(@id, 'ext-gen')]").click()
    driver.implicitly_wait(1)  # seconds
except:
    test_status = "bad: find_element_by_xpath('x-trigger-index-0 x-form-trigger x-form-date-trigger') failed or does not exist"
    print(test_status)
    exit()

try:
    datepicklist = driver.find_elements_by_xpath("//a[contains(text(),'30')]")
    datepicklist[-1].click()
except:
    test_status = "bad: find_element_by_xpath('//a[contains(text(),'30')]') failed or does not exist"
    print(test_status)
    exit()
# Step 7: Click on the magnifying glass in the SSIC field and select a SSIC.

searchMagnify = driver.find_elements_by_xpath("//div[starts-with(@class, 'x-trigger-index-0 x-form-trigger x-form-search-trigger x-form-trigger-first')]")
searchMagnify[1].click()

driver.implicitly_wait(5)  # seconds
#driver.find_element_by_xpath("//div[2]/div/div/div/div[2]/div/table/tbody/tr/td/div/span").click()
driver.find_element_by_xpath("//span[contains(text(),'01 Military Personnel')]").click()
driver.implicitly_wait(5)  # seconds
# USE BELOW LOGIC WHEN POSSIBLE!!!
driver.find_element_by_xpath("//span[contains(text(),'1000-001 Policy, Strategy, and Planning')]").click()
#driver.implicitly_wait(5)  # seconds
#driver.find_element_by_xpath("//div[3]/div/div/a/span/span/span").click()
driver.find_element_by_xpath("//span[contains(text(),'Accept')]").click()

# Step 8: Enter text in the Description/Instructions field.
try:
    driver.find_element_by_name("description").send_keys("AUTOMATED A description for Test Case 266-TC-001")
except:
    test_status = "bad: find_element_by_name('subject') failed or does not exist"
    print(test_status)
    exit()

# Step 9: Click the Add button from the Responders pane.
try:
    addButtonList = driver.find_element_by_xpath("//span[contains(text(),'Add')]")
    addButtonList.click()
except:
    test_status = "bad: find_element_by_name('//span[contains(text(),'Add')]') failed or does not exist"
    print(test_status)
    exit()

# Step 10: Click the Organizations tab.
# SELECTED BY DEFAULT

# Step 11: Enter [Organization 2 TEST-B1] in the Search field and click the Search button.
try:
    driver.find_element_by_xpath("//div[2]/div/div/div/div/table/tbody/tr/td[2]/input").send_keys("TEST-B1")
except:
    test_status = "bad: find_element_by_xpath('//div[2]/div/div/div/div/table/tbody/tr/td[2]/input') failed or does not exist"
    print(test_status)
    exit()

#driver.find_element_by_xpath("//span[contains(text(),'Search')]").click()
try:
    actions = ActionChains(driver)

    actions.send_keys(Keys.TAB)
    actions.perform()

    actions = ActionChains(driver)

    actions.send_keys(Keys.ENTER)
    actions.perform()
except:
    test_status = "bad: issue with ActionChains"
    print(test_status)
    exit()
# Step 12: Double-click [Organization 2].
try:
    org2 = driver.find_element_by_xpath("//div[contains(text(),'(TEST-B1)')]")
    actions = ActionChains(driver)
    actions.double_click(org2).perform()
except:
    test_status = "bad: double clicking Org 2 with ActionChains did not work"
    print(test_status)
    exit()

# Step 13: Enter [Organization 3] TEST-C1C in the Search field and click the Search button.
try:
    driver.find_element_by_xpath("//div[2]/div/div/div/div/table/tbody/tr/td[2]/input").clear()
    driver.find_element_by_xpath("//div[2]/div/div/div/div/table/tbody/tr/td[2]/input").send_keys("TEST-C1C")
except:
    test_status = "bad: find_element_by_xpath('//div[2]/div/div/div/div/table/tbody/tr/td[2]/input') failed or does not exist"
    print(test_status)
    exit()

# driver.find_element_by_xpath("//span[contains(text(),'Search')]").click()
try:
    actions = ActionChains(driver)

    actions.send_keys(Keys.TAB)
    actions.perform()

    actions = ActionChains(driver)

    actions.send_keys(Keys.ENTER)
    actions.perform()
except:
    test_status = "bad: issue with ActionChains"
    print(test_status)
    exit()

# Step 14: Double-click [Organization 3].
try:
    org3 = driver.find_element_by_xpath("//div[contains(text(),'(TEST-C1C)')]")
    actions = ActionChains(driver)
    actions.double_click(org3).perform()
except:
    test_status = "bad: double clicking Org 2 with ActionChains did not work"
    print(test_status)
    exit()

# Step 18: Click the Accept button.
try:
    acceptButton = driver.find_element_by_xpath("//span[contains(text(),'Accept')]")
    acceptButton.click()
except:
    test_status = "bad: find_element_by_xpath(//span[contains(text(),'Accept')]') failed or does not exist"
    print(test_status)
    exit()
# Step 19: Click the Workflow Type down arrow and select Parallel.
# SELECTED BY DEFAULT

# Step 20: Click the Add Attachment button in the Attachments pane.

try:
    addAttachmentsButton = driver.find_element_by_xpath("//span[contains(text(),'Add Attachment')]")
    addAttachmentsButton.click()
except:
    test_status = "bad: find_element_by_xpath(//span[contains(text(),'Add Attachment')]) failed or does not exist"
    print(test_status)
    exit()

'''
NOTE: The following attachments are used throughout the test procedure. Testers should use a combination of local and system files.		
'''

# Step 21: Add six (6) files [test_notepad_file.txt, test_word_doc.docx, test_ppt.pptx, Text-Excel.xlsx.
# UPLOAD FILE 1
try:
    addFilesFromRepository = driver.find_element_by_xpath("//span[contains(text(),'Add Files from Repository')]")
    addFilesFromRepository.click()
except:
    test_status = "bad: find_element_by_xpath(//span[contains(text(),'Add Files from Repository')]) failed or does not exist"
    print(test_status)
    exit()

try:
    myFiles = driver.find_element_by_xpath("//span[contains(text(),'My Files')]")
    myFiles.click()
except:
    test_status = "bad: find_element_by_xpath(//span[contains(text(),'My Files')]) failed or does not exist"
    print(test_status)
    exit()


driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/table/tbody/tr/td[2]/input").clear()
driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/table/tbody/tr/td[2]/input").send_keys("test_notepad_file.txt")

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()

element = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'test_notepad_file.txt')]")))
driver.find_element_by_xpath("//div[contains(text(),'test_notepad_file.txt')]").click()

actions = ActionChains(driver)

actions.send_keys(Keys.TAB)
actions.perform()

actions = ActionChains(driver)

actions.send_keys(Keys.ENTER)
actions.perform()
# END UPLOAD FILE 1

# UPLOAD FILE 2
try:
    addFilesFromRepository = driver.find_element_by_xpath("//span[contains(text(),'Add Files from Repository')]")
    addFilesFromRepository.click()
except:
    test_status = "bad: find_element_by_xpath(//span[contains(text(),'Add Files from Repository')]) failed or does not exist"
    print(test_status)
    exit()

try:
    myFiles = driver.find_element_by_xpath("//span[contains(text(),'My Files')]")
    myFiles.click()
except:
    test_status = "bad: find_element_by_xpath(//span[contains(text(),'My Files')]) failed or does not exist"
    print(test_status)
    exit()


driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/table/tbody/tr/td[2]/input").clear()
driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/table/tbody/tr/td[2]/input").send_keys("test_word_doc.docx")

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()

element = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'test_word_doc.docx')]")))
driver.find_element_by_xpath("//div[contains(text(),'test_word_doc.docx')]").click()

actions = ActionChains(driver)

actions.send_keys(Keys.TAB)
actions.perform()

actions = ActionChains(driver)

actions.send_keys(Keys.ENTER)
actions.perform()
# END UPLOAD FILE 2

# UPLOAD FILE 3
try:
    addFilesFromRepository = driver.find_element_by_xpath("//span[contains(text(),'Add Files from Repository')]")
    addFilesFromRepository.click()
except:
    test_status = "bad: find_element_by_xpath(//span[contains(text(),'Add Files from Repository')]) failed or does not exist"
    print(test_status)
    exit()

try:
    myFiles = driver.find_element_by_xpath("//span[contains(text(),'My Files')]")
    myFiles.click()
except:
    test_status = "bad: find_element_by_xpath(//span[contains(text(),'My Files')]) failed or does not exist"
    print(test_status)
    exit()


driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/table/tbody/tr/td[2]/input").clear()
driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/table/tbody/tr/td[2]/input").send_keys("test_ppt.pptx")

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()
driver.implicitly_wait(2)

element = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'test_ppt.pptx')]")))
driver.find_element_by_xpath("//div[contains(text(),'test_ppt.pptx')]").click()
driver.implicitly_wait(1)  # seconds


actions = ActionChains(driver)

actions.send_keys(Keys.TAB)
actions.perform()

actions = ActionChains(driver)

actions.send_keys(Keys.ENTER)
actions.perform()
# END UPLOAD FILE 3

# UPLOAD FILE 4
try:
    addFilesFromRepository = driver.find_element_by_xpath("//span[contains(text(),'Add Files from Repository')]")
    addFilesFromRepository.click()
except:
    test_status = "bad: find_element_by_xpath(//span[contains(text(),'Add Files from Repository')]) failed or does not exist"
    print(test_status)
    exit()

try:
    myFiles = driver.find_element_by_xpath("//span[contains(text(),'My Files')]")
    myFiles.click()
except:
    test_status = "bad: find_element_by_xpath(//span[contains(text(),'My Files')]) failed or does not exist"
    print(test_status)
    exit()


driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/table/tbody/tr/td[2]/input").clear()
driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/table/tbody/tr/td[2]/input").send_keys("Text-Excel.xlsx")

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()

element = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Text-Excel.xlsx')]")))

driver.find_element_by_xpath("//div[contains(text(),'Text-Excel.xlsx')]").click()

actions = ActionChains(driver)

actions.send_keys(Keys.TAB)
actions.perform()

actions = ActionChains(driver)

actions.send_keys(Keys.ENTER)
actions.perform()
# END UPLOAD FILE 4

# UPLOAD FILE 5
try:
    addFilesFromRepository = driver.find_element_by_xpath("//span[contains(text(),'Add Files from Repository')]")
    addFilesFromRepository.click()
except:
    test_status = "bad: find_element_by_xpath(//span[contains(text(),'Add Files from Repository')]) failed or does not exist"
    print(test_status)
    exit()

try:
    myFiles = driver.find_element_by_xpath("//span[contains(text(),'My Files')]")
    myFiles.click()
except:
    test_status = "bad: find_element_by_xpath(//span[contains(text(),'My Files')]) failed or does not exist"
    print(test_status)
    exit()


driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/table/tbody/tr/td[2]/input").clear()
driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/table/tbody/tr/td[2]/input").send_keys("test_pdf.pdf")

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()

element = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'test_pdf.pdf')]")))

driver.find_element_by_xpath("//div[contains(text(),'test_pdf.pdf')]").click()

actions = ActionChains(driver)

actions.send_keys(Keys.TAB)
actions.perform()

actions = ActionChains(driver)

actions.send_keys(Keys.ENTER)
actions.perform()
# END UPLOAD FILE 5

# UPLOAD FILE 6
try:
    addFilesFromRepository = driver.find_element_by_xpath("//span[contains(text(),'Add Files from Repository')]")
    addFilesFromRepository.click()
except:
    test_status = "bad: find_element_by_xpath(//span[contains(text(),'Add Files from Repository')]) failed or does not exist"
    print(test_status)
    exit()

try:
    myFiles = driver.find_element_by_xpath("//span[contains(text(),'My Files')]")
    myFiles.click()
except:
    test_status = "bad: find_element_by_xpath(//span[contains(text(),'My Files')]) failed or does not exist"
    print(test_status)
    exit()


driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/table/tbody/tr/td[2]/input").clear()
driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/table/tbody/tr/td[2]/input").send_keys("Test_Picture.PNG")

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()

element = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Test_Picture.PNG')]")))
driver.find_element_by_xpath("//div[contains(text(),'Test_Picture.PNG')]").click()

actions = ActionChains(driver)

actions.send_keys(Keys.TAB)
actions.perform()

actions = ActionChains(driver)

actions.send_keys(Keys.ENTER)
actions.perform()
# END UPLOAD FILE 6

# Step 22: Click the Category magnifying glass for attachment 1.
# Verify the following seven (7) categories are listed:
# 1) Action/Info Memo
# 2) Draft Response
# 3) Incoming Letter
# 4) Organizational Response
# 5) Original Source Document
# 6) Reference
# 7) Working Document

driver.find_element_by_xpath("//div[2]/div/div/div/div[3]/div/table/tbody/tr/td[3]/div").click()
driver.find_element_by_xpath("//div[4]/table/tbody/tr/td[2]/table/tbody/tr/td[3]/div").click()

# Step 23: Click once on a category.

driver.implicitly_wait(2)
WorkingDocs = driver.find_elements_by_xpath("//div[contains(text(),'Working Document')]")
WorkingDocs[1].click()

driver.implicitly_wait(2)
IncomingLetter = driver.find_elements_by_xpath("//div[contains(text(),'Incoming Letter')]")
IncomingLetter[1].click()

driver.implicitly_wait(2)
ActionInfoMemo = driver.find_elements_by_xpath("//div[contains(text(),'Action/Info Memo')]")
ActionInfoMemo[1].click()

driver.implicitly_wait(2)
DraftResponse = driver.find_elements_by_xpath("//div[contains(text(),'Draft Response')]")
DraftResponse[1].click()

driver.implicitly_wait(2)
OriginalSourceDocument = driver.find_elements_by_xpath("//div[contains(text(),'Original Source Document')]")
OriginalSourceDocument[1].click()

driver.implicitly_wait(2)
OrganizationalResponse = driver.find_elements_by_xpath("//div[contains(text(),'Organizational Response')]")
OrganizationalResponse[1].click()

# Step 24: Click the Accept button.

AcceptButtons = driver.find_elements_by_xpath("//span[contains(text(),'Accept')]")

AcceptButtons[1].click()

# Step 25: Click the Category magnifying glass for attachment 2.
driver.find_element_by_xpath("//div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[3]/div").click()
driver.find_element_by_xpath("//div[4]/table/tbody/tr/td[2]/table/tbody/tr/td[3]/div").click()

# Step 26: Double-click a category.
WorkingDocs = driver.find_elements_by_xpath("//div[contains(text(),'Working Document')]")

actions = ActionChains(driver)
actions.double_click(WorkingDocs[1]).perform()

# Step 27: Click the Category down arrow for attachment 3.
driver.find_element_by_xpath("//div[2]/div/div/div/div[3]/div/table/tbody/tr[3]/td[3]/div").click()
driver.find_element_by_xpath("//div[4]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/div").click()

# Step 28: Click once on a category.

driver.implicitly_wait(2)
#DraftResponse = driver.find_elements_by_xpath("//div[contains(text(),'Draft Response')]")
driver.find_element_by_xpath("//li[contains(text(),'Draft Response')]").click()
#DraftResponse[0].click()

# Step 29: Partially enter a category in the Category field for attachment 4.

CatRow4 = driver.find_element_by_xpath("//div[2]/div/div/div/div[3]/div/table/tbody/tr[4]/td[3]/div")
CatRow4.click()

inputMultiBox = driver.find_element_by_xpath("//div[4]/table/tbody/tr/td[2]/table/tbody/tr/td/input")
inputMultiBox.send_keys("O")
print(inputMultiBox.location)
print(inputMultiBox.size)
#xcoord = inputMultiBox

driver.implicitly_wait(2)

# Step 30: Click once on the suggested category

actions = ActionChains(driver)
actions.move_to_element_with_offset(inputMultiBox, 25, 25)
actions.click()
actions.perform()

# Step 31: Select a category for attachment 5.

# Step 32: Click the Category ‘X’ icon.

# Step 33: Select a new category for attachment 5.

# Step 34: Click the Accept button.

# Step 35: Click the OK button.
