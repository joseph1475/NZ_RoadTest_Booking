from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import winsound

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://online.nzta.govt.nz/licence-test/identification")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@formcontrolname='LicenceNumber']").send_keys("EE418837")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@formcontrolname='LicenceVersion']").send_keys("045")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@formcontrolname='LastName']").send_keys("Peter")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@formcontrolname='DateOfBirth']").send_keys("03-03-1990")
time.sleep(2)
driver.find_element(By.ID,"btnContinue").click()   #login
time.sleep(5)
#driver.find_element(By.ID,"btnContinue").click()   #book if no slot select //button[@id='btnContinue']
#time.sleep(5)
driver.find_element(By.XPATH,"//button[@id='btnContinue']").click() #for resludule
time.sleep(5)
driver.find_element(By.XPATH,"//a[normalize-space()='Auckland']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='North Auckland']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='VTNZ Saturn Place']").click()
time.sleep(5)
#skipping 3 months as currect slots are after 3 months

driver.find_element(By.XPATH,"//a[@title='Next']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[@title='Next']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[@title='Next']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"td[class='ui-datepicker-current-day'] a").click() # select aviabile date
time.sleep(5)
# Play a simple beep sound
winsound.Beep(1000, 10000)  # Frequency: 1000 Hz, Duration: 10000 ms (10 second)
driver.close()