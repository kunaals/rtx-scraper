import itertools
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

base_gpus = ['3060', '3070', '3080', '3090']
variations = ['', 'ti', 'lhr', 'ti-lhr']
gpus = itertools.product(base_gpus, variations)
paths = [f'nvidia-rtx-{g[0]}-{g[1]}' if g[1] else f'nvidia-rtx-{g[0]}' for g in gpus]

driver = webdriver.Chrome('/Users/ksikka/Downloads/chromedriver')
for path in paths:
    try:
        driver.get(f'https://www.nicehash.com/profitability-calculator/{path}')
        sleep(10)
        # sometimes the implicit wait fails too early
        # driver.implicitly_wait(15)
        daily_income = driver.find_element(by=By.CLASS_NAME, value='text-success')
        print(path, daily_income.text.split(' ')[0])
    except:
        print(f"Couldn't get path {path}")
        continue

driver.close()