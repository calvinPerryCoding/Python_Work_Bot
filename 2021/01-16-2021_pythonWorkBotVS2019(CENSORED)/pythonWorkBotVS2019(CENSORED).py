from selenium import webdriver
#Allows common keys to be used
from selenium.webdriver.common.keys import Keys
import time

#Number of seconds between each question
timeBetweenQuestions = 3
#Number of seconds until browser closes
timeUntilQuit = 10

driverPath = r"CENSORED"

driver = webdriver.Chrome(driverPath)

#Opens webpage
driver.get("CENSORED")
#Wait x number of seconds before executing next line
time.sleep(timeBetweenQuestions)

#Question 1
#Drop the s in elements (Hu, 2017)
# //tagname[@attribute='value'] or //*[@attribute='value'] (Bhattacharjee, 2020)
questionOne = driver.find_element_by_xpath("CENSORED")
questionOne.send_keys("CENSORED")
time.sleep(timeBetweenQuestions)

#Question 2
questionTwo = driver.find_element_by_xpath("CENSORED']")
questionTwo.send_keys("CENSORED")
time.sleep(timeBetweenQuestions)

#Question 3
#Use .click() for check boxes (Mortensen, 2020)
driver.find_element_by_xpath("CENSORED").click()
time.sleep(timeBetweenQuestions)

#Question 4
driver.find_element_by_xpath("CENSORED").click()
questionFour = driver.find_element_by_xpath("CENSORED")
time.sleep(timeBetweenQuestions)
questionFour.send_keys("CENSORED")
time.sleep(timeBetweenQuestions)

#Question 5
#If two or more elements have the same name use indexing (Santoshsarma, 2014)
driver.find_element_by_xpath("CENSORED").click()
time.sleep(timeBetweenQuestions)

#Question 6
driver.find_element_by_xpath("CENSORED").click()
time.sleep(timeBetweenQuestions)

#Question 7
driver.find_element_by_xpath("CENSORED").click()
time.sleep(timeBetweenQuestions)

#Question 8
driver.find_element_by_xpath("CENSORED").click()
time.sleep(timeBetweenQuestions)

#Question 9
driver.find_element_by_xpath("CENSORED").click()
time.sleep(timeBetweenQuestions)

#Submit Button
# (Alecxe, 2016)
driver.find_element_by_class_name("CENSORED").click()

time.sleep(timeUntilQuit)
#Closes all tabs and browser
driver.quit



# References APA 7th Edition


# Alecxe. (2016, December 19). How can I click on a div Button with selenium webdriver? Stack Overflow. https://stackoverflow.com/questions/41230389/how-can-i-click-on-a-div-button-with-selenium-webdriver

# Bhattacharjee, D. (2020, July 29). What is XPath in selenium with Python? RxJS, ggplot2, Python Data Persistence, Caffe2, PyBrain, Python Data Access, H2O, Colab, Theano, Flutter, KNime, Mean.js, Weka, Solidity. https://www.tutorialspoint.com/what-is-xpath-in-selenium-with-python

# Birajdar, D. M. (2017, September 2). (Unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: Truncated \UXXXXXXXX escape. Stack Overflow. https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca

# Hu, H. (2017, August 1). Attributeerror list object has no attribute Send_keys. Hang's Blog. https://hang-hu.github.io/python/2017/08/01/AttributeError-list-object-has-no-attribute-send_keys.html

# Mortensen, P. (2020, December 1). Select checkbox using selenium with Python. Stack Overflow. https://stackoverflow.com/questions/21213417/select-checkbox-using-selenium-with-python

# Santoshsarma. (2014, May 23). How to access the second element that has the same class name in selenium using Java. Stack Overflow. https://stackoverflow.com/questions/23828893/how-to-access-the-second-element-that-has-the-same-class-name-in-selenium-using

# Tech With Tim. (2020, April 26). Python Selenium Tutorial #1 - Web Scraping, Bots & Testing [Video]. YouTube. https://www.youtube.com/watch?v=Xjv1sY630Uc

# Tech With Tim. (2020, April 28). Python Selenium Tutorial #2 - Locating Elements From HTML [Video]. YouTube. https://www.youtube.com/watch?v=b5jt2bhSeXs
