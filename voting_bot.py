#from threading import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

url="https://www.some-page-with-buttons-to-vote.com/"
vote_count = 0
executable_path='/mnt/c/Users/username/Downloads/chromedriver/chromedriver.exe'

while True:
    proxy_file = open(r"C:\Users\username\Downloads\promo code bot\socks4.txt", "r+") # ip:port
    success_file = open(r"C:\Users\username\Downloads\promo code bot\successfull_socks4.txt", "a")
    proxy = proxy_file.readline()
    proxies = proxy_file.readlines()    # used
    proxy_file.seek(0)                  # to remove
    proxy_file.truncate()               # one
    proxy_file.writelines(proxies[0:])  # line
    proxy_file.close()

    options = Options()
    options.add_argument('--proxy-server=socks4://%s' % proxy) # or change to socks5:// or http://
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    try:
        driver = webdriver.Chrome(options=options) # OR webdriver.Chrome(executable_path='/mnt/c/Users/holie/Downloads/chromedriver', options=options)
        driver.set_page_load_timeout(20) # sets the amount of time to wait for a page load to complete before throwing an error.
        driver.get(url)
        sleep(1)
        # button Vote
        driver.find_element_by_xpath("/html/body/div/div[2]/section[2]/div/section[2]/ul/li[2]/div/div[2]/button").click()
        sleep(1)
        # button Confirm (Voted successfuly)
        driver.find_element_by_xpath("/html/body/div/div[2]/section[2]/div/div/div[2]/button").click()
        sleep(1)
        vote_count = vote_count + 1
        print("voted count: %s" % vote_count)
        print("good proxy: %s" % proxy)
        success_file.write(proxy)
        driver.quit()
    except:
        print("Proxy Connection Error")
        driver.quit()
    else:
        sleep(7)
        driver.quit()
