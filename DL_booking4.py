#continuious check all auckland centres including next month

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

# List of centers to check
centers = [
    "//a[normalize-space()='VTNZ Silverdale']",
    "//a[normalize-space()='VTNZ North Shore']",
    "//a[normalize-space()='VTNZ Saturn Place']",
    "//a[normalize-space()='VTNZ Warkworth']"
]

def check_center(center_xpath):
    """Check a specific center for available slots."""
    slot_found = False
    while not slot_found:
        try:
            driver.find_element(By.XPATH, center_xpath).click()
            time.sleep(5)
            driver.find_element(By.CSS_SELECTOR,
                                "td[class='ui-datepicker-current-day'] a").click()  # select available date
            time.sleep(5)
            winsound.Beep(1000, 10000)  # Frequency: 1000 Hz, Duration: 10000 ms (10 seconds)
            slot_found = True
        except:
            print(f"No slot found at {center_xpath}, checking next month")
            try:
                driver.find_element(By.XPATH, "//a[@title='Next']").click()  # checking following month
                time.sleep(5)
            except:
                print("No further months to check")
                break
    return slot_found


# Infinite loop to keep checking for available slots
while True:
    try:
        # Click through the location hierarchy
        driver.find_element(By.XPATH, "//a[normalize-space()='Auckland']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[normalize-space()='North Auckland']").click()
        time.sleep(2)

        slot_found = False

        # Iterate through each center
        for center in centers:
            if check_center(center):
                slot_found = True
                break  # Exit the loop if slot is found

        if slot_found:
            break  # Exit the outer loop if a slot is found
    except Exception as e:
        print(f"Error occurred: {e}")
        continue  # Continue looping if an error occurs

# Close the driver after finishing
driver.quit()
