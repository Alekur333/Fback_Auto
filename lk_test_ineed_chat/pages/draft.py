from datetime import datetime
from splinter import Browser
import time
import os


# browser = Browser('chrome')
# # browser = Browser('chrome', headless=True)
# browser.driver.maximize_window()

now1 = datetime.now().date()
print(now1)
current_year = str(now1.year)
print(f'Год:  {current_year}')
current_month = str(now1.month)
print(f'Месяц: {current_month}')
current_day = str(now1.day)
print(f'День:  {current_day}')

# browser.visit('http://google.com')
# browser.fill('q', 'splinter - python acceptance testing for web applications')
# button = browser.find_by_name('btnK').click()
#
# if browser.is_text_present('splinter.readthedocs.io'):
#     print ("Yes, found it! :)")
# else:
#     print ("No, didn't find it :(")

# screenshot_path = browser.screenshot('C:/Users/user/Pictures/your_screenshot.png', full=True)
# time.sleep(2)

current_dir = os.path.dirname(r'C:\Users\user\pics\\')
file_path = os.path.join(current_dir, 'autotest_se.png')
print(file_path)

# browser.quit()