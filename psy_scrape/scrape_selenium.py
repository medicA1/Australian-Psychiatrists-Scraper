from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import re

def remove_title(full_name):
    title_pattern = r'\b(?:Dr|A/Prof|Prof)\b\s*'

    cleaned_name = re.sub(title_pattern, '', full_name)

    return cleaned_name.strip()

loaded_pages = 120 # 10 psychiatrists per load * 120 pages

url = f"https://www.yourhealthinmind.org/find-a-psychiatrist/results?country=AU&seed=581638&onlineConsultations=false&radius=10&expertiseIn=%5B%5D&servicesOffered=%5B%5D&experienceWith=%5B%5D&treatsAges=%5B%5D&languages=%5B%5D&page={loaded_pages}&searchLoading=true&initialSearch=true"

options = Options()
options.headless = True
driver = webdriver.Chrome()

driver.get(url)
time.sleep(60)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

containers = soup.select(".s-psychresults__item")

with open("psychiatrists.csv", "w") as file:
    for i, container in enumerate(containers, start=1):
        full_name = container.select_one(".s-psychresults__item__name").text.strip()
        cleaned_name = remove_title(full_name)

        email = "N/A"
        
        for link in container.select("a[href^='mailto:']"):
            email = link.get("href").replace("mailto:", '').strip()

        tel_number = container.select_one(".s-psychresults__item__location__content__detail__alt-link").text.strip() if container.select_one(".s-psychresults__item__location__content__detail__alt-link") else "N/A"
        
        file.write(f"{i}, {cleaned_name}, {email}, {tel_number}\n")

driver.quit()

