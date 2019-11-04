from selenium import webdriver


driver = webdriver.Chrome('chromedriver')

driver.get('https://pixabay.com/ko/')
search_box = driver.find_element_by_class_name('q')
search_box.send_keys("공부")
search_box.submit()