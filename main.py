import logging
import urllib.request
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")

#hitting the URL
driver.get("https://github.com/](https://github.com/)")
title=driver.title
assert "GitHub" in title , "Incorrect page opened"
print("correct title displayed")
#search operation and hitting submit button
driver.find_element_by_id("not-found-search").send_keys("react")
driver.find_element_by_css_selector('button[class="btn"]').click()
#verifying current URL matches post search
assert "https://github.com/search?q=react" in driver.current_url , "search operation failed as current URl doesn't match"
print("correct URL displayed {}".format(driver.current_url))
driver.find_element_by_link_text("Advanced search").click()
assert "https://github.com/search/advanced?q=react&type=Repositories" in driver.current_url , "landed on wrong URL"

# Using Select class to handle dropdown
dropdown=Select(driver.find_element_by_id("search_language"))
dropdown.select_by_visible_text("JavaScript")
#stars: >45;
driver.find_element_by_id("search_stars").send_keys(">45")

#followers: > 50;
driver.find_element_by_id("search_followers").send_keys(">50")

#license : Boost Software License 1.0
driver.find_element_by_id("search_license").send_keys("Boost Software License 1.0")
#hit submit button
driver.find_element_by_xpath('//button[contains(@class,"flex-auto btn")]').click()
respository_result=(driver.find_element_by_xpath('//div[contains(@class,"pb-3")]').text)
print("Repository result shown : {}".format(respository_result))
print("Verifying correct number of repository shown")
assert "1 repository result" in respository_result , "Incorrect number of repository result showing up"
#verifying Repository name
repo_list=driver.find_elements_by_css_selector(".repo-list-item")
print(repo_list)
for repo in repo_list:
    if "mvoloskov/decider" in repo.text:
        print("Correct Repository name found")
        break
driver.find_element_by_link_text("mvoloskov/decider").click()
url="https://raw.githubusercontent.com/mvoloskov/decider/master/README.md"
file = urllib.request.urlopen(url)
print(file.read(300))

