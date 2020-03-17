from datetime import datetime
from splinter import Browser

now1 = datetime.now().date()
print(now1)
current_year = str(now1.year)
print(f'Год:  {current_year}')
current_month = str(now1.month)
print(f'Месяц: {current_month}')
current_day = str(now1.day)
print(f'День:  {current_day}')

browser = Browser('chrome')
# browser.maximize_window()
browser.visit('http://google.com')
browser.fill('q', 'splinter - python acceptance testing for web applications')
button = browser.find_by_name('btnK').click()

if browser.is_text_present('splinter.readthedocs.io'):
    print ("Yes, found it! :)")
else:
    print ("No, didn't find it :(")

browser.quit()