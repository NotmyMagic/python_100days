from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]



timeout = time.time() + 5
five_min = time.time() + 60*0.5


while True:
    cookie.click()
    if timeout < time.time():
        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []

        for price in all_prices:
            check = price.text
            cut = check.split(" ")

            try:
                if cut[2] == "-":
                    item_prices.append(cut[3].replace(",", ""))
                else:
                    item_prices.append(cut[2].replace(",", ""))
                    
            except IndexError:
                pass

        item_prices = [int(price) for price in item_prices]
        # print(item_prices)
        
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]
        # print(cookie_upgrades)

        money = driver.find_element(By.CSS_SELECTOR, value="#money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        affordable_upgrades = {}
        for item_prices, id in cookie_upgrades.items():
            if cookie_count > item_prices:
                affordable_upgrades[item_prices] = id
        
        highest_price_affordable_upgrade = max(affordable_upgrades)
        # print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        # if money > 0:
        #     for item_price in item_prices[::-1]:
        #         for item in item_names[::-1]:
        #             print(f"#buy{item}")
        #             buy_upgrade = driver.find_element(By.ID, value=f"#buy{item}")
        #             buy_upgrade.click()
        #             print(money)

        timeout = time.time() + 5

    if time.time() > five_min:
        break