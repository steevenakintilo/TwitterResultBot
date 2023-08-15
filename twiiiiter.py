from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from os import system
import time
import pickle

from selenium.webdriver.common.by import By
import traceback
from random import randint
import yaml

from discord_webhook import DiscordWebhook
import json


class Scraper:
    wait_time = 5
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome( options=options)  # to open the chromedriver    

    username_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
    
    button_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
    password_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
    login_button_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div'
    test_tweet = 'https://twitter.com/Twitter/status/1580661436132757506'
    like_button_xpath = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div[1]/article/div/div/div/div[3]/div[7]/div/div[3]/div'
    cookie_button_xpath = '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]/div/span/span'
    notification_button_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/span/span'
    path1 = ""
    path2 = ""
    

def login(S,_username,_password):
    try:

        S.driver.get("https://twitter.com/i/flow/login")
        print("Starting Twitter")

        #USERNAME
        element = WebDriverWait(S.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, S.username_xpath)))

        username = S.driver.find_element(By.XPATH,S.username_xpath)
        username.send_keys(_username)    
        
        element = WebDriverWait(S.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, S.button_xpath)))


        #FIRST BUTTON

        button = S.driver.find_element(By.XPATH,S.button_xpath)
        button.click()
        print("button click")


        #PASSWORD

        element = WebDriverWait(S.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, S.password_xpath)))
        
        password = S.driver.find_element(By.XPATH,S.password_xpath)
        password.send_keys(_password)
        print("password done")


        #LOGIN BUTTON

        element = WebDriverWait(S.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, S.login_button_xpath)))
        
        login_button = S.driver.find_element(By.XPATH,S.login_button_xpath)
        login_button.click()
        print("login done")

        #print("Closing Twitter")
    except:
        print("Error either selenium or wrong username restart please")
        quit()

def accept_coockie(S):
    try:
        S.driver.get(S.test_tweet)

        element = WebDriverWait(S.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, S.cookie_button_xpath)))
        
        cookie_button = S.driver.find_element(By.XPATH,S.cookie_button_xpath)
        cookie_button.click()

    except:
        print("error")
        pass    
    
    
    print("coockie done")


def accept_notification(S):
    try:
        S.driver.get(S.test_tweet)

        element = WebDriverWait(S.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, S.notification_button_xpath)))
        
        cookie_button = S.driver.find_element(By.XPATH,S.notification_button_xpath)
        cookie_button.click()
    except:
        pass    
    try:
        S.driver.get(S.test_tweet)

        element = WebDriverWait(S.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, S.cookie_button_xpath)))
        
        cookie_button = S.driver.find_element(By.XPATH,S.cookie_button_xpath)
        cookie_button.click()

    except:
        print("error")
        pass    
    
    print("notification done")
    
def forever_loop():
    while True:
        try:
            main_one()
        except Exception as e:
            print("Flop " + str(e))
            time.sleep(600)
        time.sleep(172800)


def print_file_info(path):
    f = open(path, 'r')
    content = f.read()
    f.close()
    return(content)

def send_message_discord(msg,path,only_msg):
    urls = print_file_info("webhook_url.txt")
    if only_msg == False:
        webhook = DiscordWebhook(url=urls, content=msg)
    else:
        webhook = DiscordWebhook(url=urls, content=msg)        
        if path:
            with open(path, "rb") as f:
                webhook.add_file(file=f.read(), filename=path)
    response = webhook.execute()

def take_screen_of_mention(S,account):
    try:
        my_url = "https://twitter.com/notifications/mentions"
        S.driver.get(my_url)
        time.sleep(30)
        S.driver.execute_script("document.body.style.zoom='50%'")
        S.driver.save_screenshot("screens/mention/"+str(account)+"_mention.png")
        S.path1 = (str("screens/mention/"+str(account)+"_mention.png"))
        
    except:
        print("Error during screen of this account " , account)
        time.sleep(30)
        S.driver.save_screenshot("screens/mention/"+str(account)+"_mention.png")
        S.path1 = (str("screens/mention/"+str(account)+"_mention.png"))
        

def take_screen_of_dm(S,account):
    try:
        my_url = "https://twitter.com/messages"
        S.driver.get(my_url)
        time.sleep(30)
        S.driver.execute_script("document.body.style.zoom='50%'")
        S.driver.save_screenshot("screens/dm/"+str(account)+"_dm.png")
        
        S.path2 = (str("screens/dm/"+str(account)+"_dm.png"))
        

    except:        
        S.path2 = (str("screens/dm/"+str(account)+"_dm.png"))
        time.sleep(30)

def check_login_good(selenium_session):
    try:
        selenium_session.driver.get("https://twitter.com/home")
        element = WebDriverWait(selenium_session.driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="AppTabBar_Notifications_Link"]')))
        return True
    except Exception as e:
        
        return False
       
def main_one():
    print("Inside main one")
    giveaway_done = 0
    with open("configuration.yml", "r") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    
    print("Starting the program")
    print("Screenshoot go bang bang")
    username_info = data["account_username"]
    password_info = data["account_password"]
    check_dm = data["check_dm"]
    for i in range(len(username_info)):
        print("Connecting to " + str(username_info[i]))
        time.sleep(1)
        S = Scraper()
        login(S,username_info[i],password_info[i])
        time.sleep(3)
        if check_login_good(S) == False:
            print(f"The account is locked or password of {username_info[i]} is wrong change it on the configuration.yml file")
            print("Skipping the account")
            continue
        accept_coockie(S)
        time.sleep(S.wait_time)    
        accept_notification(S)
        time.sleep(S.wait_time)
        accept_coockie(S)
        time.sleep(S.wait_time)
        print("Picture from " + str(username_info[i]) + " account")
        take_screen_of_mention(S,username_info[i])
        send_message_discord(str("Picture from " + str(username_info[i]) + " account"),S.path1,True)
        if check_dm == True:
            take_screen_of_dm(S,username_info[i])
            send_message_discord(str("Picture from " + str(username_info[i]) + " account"),S.path2,True)
        print("Screenshot finished for this account sleeping a bit")
        time.sleep(20)
    print("End of the program")
    send_message_discord("Screenshot done for today bye bye",S.path1,False)