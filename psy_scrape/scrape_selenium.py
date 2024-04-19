from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
import csv

def remove_title(full_name):
    title_pattern = r'\b(?:Dr|A/Prof|Prof)\b\s*'
    cleaned_name = re.sub(title_pattern, '', full_name)
    return cleaned_name.strip()

loaded_pages = 120 # Example load page

url = f"https://www.yourhealthinmind.org/find-a-psychiatrist/results?country=AU&seed=581638&onlineConsultations=false&radius=10&expertiseIn=%5B%5D&servicesOffered=%5B%5D&experienceWith=%5B%5D&treatsAges=%5B%5D&languages=%5B%5D&page={loaded_pages}&searchLoading=true&initialSearch=true"

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

driver.get(url)

try:
    # Wait for the elements to be loaded
    WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".s-psychresults__item"))
    )
except TimeoutException:
    print("Timed out waiting for page to load")
    driver.quit()

containers = driver.find_elements(By.CSS_SELECTOR, ".s-psychresults__item")

with open("psychiatrists.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Index", "Name", "Email", "Telephone"])
    
    for i, container in enumerate(containers, start=1):
        full_name = container.find_element(By.CSS_SELECTOR, ".s-psychresults__item__name").text.strip()
        cleaned_name = remove_title(full_name)
        
        email_links = container.find_elements(By.CSS_SELECTOR, "a[href^='mailto:']")
        email = email_links[0].get_attribute("href").replace("mailto:", '').strip() if email_links else "N/A"
        
        tel_element = container.find_element(By.CSS_SELECTOR, ".s-psychresults__item__location__content__detail__alt-link")
        tel_number = tel_element.text.strip() if tel_element else "N/A"
        
        writer.writerow([i, cleaned_name, email, tel_number])

driver.quit()
