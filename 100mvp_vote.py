#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# 讀取設定檔
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

login_method = config['login_method'] # 可選 "google", "facebook", "email"
vote_count = config['vote_count'] # 每次登入要投票的次數
email = config['email']
password = config['password']

# 初始化瀏覽器
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def login_with_email(email, password):
    try:
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        email_field.clear()
        email_field.send_keys(email)
        
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_field.clear()
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
    except TimeoutException:
        print("登入失敗，元素未找到")

def login_with_google():
    # 點擊 Google 登入按鈕
    google_login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Google")]'))
    )
    google_login_button.click()
    # 切換到 Google 登入的彈出視窗
    driver.switch_to.window(driver.window_handles[-1])
    # 輸入 Google 帳號
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'identifierId'))
    )
    email_field.send_keys(email)
    email_field.send_keys(Keys.RETURN)
    # 輸入密碼
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'password'))
    )
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    # 切換回主視窗
    driver.switch_to.window(driver.window_handles[0])

def login_with_facebook():
    # 點擊 Facebook 登入按鈕
    facebook_login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Facebook")]'))
    )
    facebook_login_button.click()
    # 切換到 Facebook 登入的彈出視窗
    driver.switch_to.window(driver.window_handles[-1])
    # 輸入 Facebook 帳號
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email'))
    )
    email_field.send_keys(email)
    # 輸入密碼
    password_field = driver.find_element(By.ID, 'pass')
    password_field.send_keys(password)
    # 提交登入表單
    password_field.send_keys(Keys.RETURN)
    # 切換回主視窗
    driver.switch_to.window(driver.window_handles[0])


def vote_action():
    for _ in range(vote_count):
        try:
            # 等待「立即投票」按鈕
            vote_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div/div/div[3]/div[3]/div/div[2]/a'))
            )
            vote_button.click()

            # 使用完整 XPath 定位「是的送出」按鈕
            confirm_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/button[2]'))
            )
            
            # 滾動至按鈕可見（如果必要）
            driver.execute_script("arguments[0].scrollIntoView();", confirm_button)

            # 點擊「是的送出」
            confirm_button.click()

            # 確認投票成功
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//p[contains(text(), "感謝您參與今日的投票應援")]'))
            )
            print("投票成功！")

            # 刷新頁面以進行下一次投票
            driver.refresh()
            time.sleep(1)

        except TimeoutException as e:
            print(f"投票過程中遇到問題，元素未找到: {e}")



try:


    # 開啟投票頁面
    driver.get('https://100mvp.managertoday.com.tw/2024/view/13')
    
    # 等待「登入 / 註冊」按鈕的「登入」部分可點擊
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[text()="登入"]'))
    )
    login_button.click()
    
    # 根據設定檔選擇登入方式
    if login_method == 'email':
        login_with_email(email, password)  # 傳遞 email 和 password 參數
    else:
        raise ValueError("目前僅支援 Email 登入")
    # elif login_method == 'google':
    #     login_with_google()
    # elif login_method == 'facebook':
    #     login_with_facebook()
    # else:
    #     raise ValueError("不支援的登入方式")
    
    # 等待登入完成
    vote_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div/div/div[3]/div[3]/div/div[2]/a'))
    )
    # 點擊按鈕
    vote_button.click()
    vote_action()

    
except Exception as e:
    print(f"發生錯誤：{e}")

finally:
    # 關閉瀏覽器
    driver.quit()


# In[ ]:





# In[ ]:




