### change delay and wait time periods where ever necessary

import os
import sys
if sys.version_info[0]!=3:
    print('install python 3')
    sys.exit

def path(driver):
    

    path=(os.getcwd()+'\\geckodriver')
    print('path set to ',path)
    driver = webdriver.Firefox(executable_path=path)
    return driver

try:
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.common.keys import Keys
    import csv
    import time
except :
    print("please install selenium")
username = input("username or email")
password = input("password")
def passs(driver,username,password):
    password = input("password")
    driver.find_element_by_xpath("//input[@name='password']").clear()
    login(driver,username,password)



#username = "ramesh@intrees.org"
#password = "qwerty54321"

#password = "password"
user_name_to_search = input("first user name to search :")
#user_name_to_search="XXXXXXXXXXXXX"
userprofile_link = "https://www.instagram.com/"+user_name_to_search


def login(driver,username,password):
    driver.get('https://www.instagram.com/')
    delay = 10 #seconds
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'Log in')))
        print("Login Page is ready!")
    except TimeoutException:
        print("Loading took too much time!\n\n")
        

    
    driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    
    login_btn = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div")
    login_btn.click()

    
    time.sleep(5)
    try:

        if (driver.find_element_by_class_name("eiCW-")):
            print("inncorrect password")
            print("please retype password ")
            passs(driver,username,password)
    except:
        print()
    time.sleep(3)
    
    try:

    
        saveinfo_off=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        saveinfo_off.click()
        

    except:
        print()
    time.sleep(3)   

#    try:
       
    ntf_off=driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    ntf_off.click()
    print("logged in")
        
#    except:
    print()

    time.sleep(3)
    return driver

#search xpath/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input
def instaProfile(driver):
    driver.get(userprofile_link)
    delay = 5 #seconds
    follower_link = "/" + user_name_to_search + '/followers/'
    follower_xPath = "//a[@href='" + follower_link + "']"
    time.sleep(1)
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, follower_xPath)))
        print(str(user_name_to_search) + " page is ready!")
    except TimeoutException:
        print("Loading took too much time!\n\n")
    time.sleep(0.5)
#/html/body/div[1]/section/main/div/header/section/ul/li[2]/a
#    ele =  driver.find_element_by_xpath(follower_xPath)
    ele =  driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
    ele.click()
  
    return driver


def fetchUsers(driver):
    csv_output = open('output.csv', 'a')
    
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")

    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
#/html/body/div[1]/section/main/div/header/section/ul/li[2]/a for class_name isgrP
    a=0
    for _ in range(10000000):    
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(0.2)
        a+=1
        print(a)
   
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    time.sleep(1)


###change class_="wo9IH" wher li starts    
    for li in soup.find_all("li", class_ = "wo9IH"):
        user = {}

        user['username'] = li.find(attrs={"class" : "d7ByH"}).text

        w = csv.DictWriter(csv_output, user.keys())
        w.writerow(user)
        
    csv_output.close()   
        
    return driver 

def task1(driver):
    driver = instaProfile(driver)
    time.sleep(2)
    driver = fetchUsers(driver)
    print('this scrap succesful')
    return driver

def main():
    print('if gecodriver is in this directory, \n press \'Y\' if path already included by default (user) type \'N\' type \'Y\': \n ')
    
    a=input()

    if (a == ('y' or 'Y')):
        driver=path()
    else :
        print('path is already defined by user \n')
        driver = webdriver.Firefox()
    a=input('Do you want to add header')
    if (a==("Y" or 'y')):
        headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
        print('default header is ',headers)
        driver=webdriver.addheaders = [('User-Agent',headers['User-Agent'])]
    
    driver = login(driver,username,password)
    time.sleep(5)
 #   user_name_to_search = input("first user name to search :")
    
    driver = instaProfile(driver)
    time.sleep(2)
    task1(driver)



main()    
#task1(driver)

driver.close()

print("Successfully scrapped")
