# Australian Psychiatrists Scraper

This was a freelance assignment done for a client who required a tool to extract information about psychiatrists 
listed on the [Your Health in Mind](https://www.yourhealthinmind.org/find-a-psychiatrist/) website.
The website dynamically loads content, requiring the use of Selenium WebDriver for scraping.


## Project Overview

**Objective**: Extract name, surname and contact information for Australian psychiatrists and store the data in a CSV file

**Initial Instructions**: Load the webpage without altering filters, click search, and extract all psychiatrists.

**Challenge**: The website initially loaded only 10 psychiatrists, with an option to load 10 more by clicking "Load More." 
Instead of using Selenium for loading each page, I utilized the URL's page loading mechanism to fetch all available 
psychiatrists.

**Simplicity**: The code is intentionally kept simple, since the client only required data stored inside CSV.
However, you can enhance the code and possibly make a more sophisticated waiting mechanisms if desired.


## Required Installs
pip install beautifulsoup4
pip install selenium


## Discalimer

If you are an Australian seeking psychiatric services, please consider using the Your Health in Mind website to find 
suitable professionals.
