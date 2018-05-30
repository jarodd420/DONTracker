from selenium import webdriver
import zipfile

zip_ref = zipfile.ZipFile('C:/Users/jared/Downloads/FirefoxProfiles.zip', 'r')
#zip_ref.extractall('C:/Users/jared/Downloads/')
zip_ref.extractall("Azam/")
zip_ref.close()

fp = webdriver.FirefoxProfile("Azam/FirefoxProfiles")
driver = webdriver.Firefox(fp)
driver.get("https://test.dontracker.navy.mil")

#driver.close()
