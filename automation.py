from selenium import webdriver

chrome_browser = webdriver.Chrome("./chromedriver.exe")
print(chrome_browser)


chrome_browser.maximize_window()
