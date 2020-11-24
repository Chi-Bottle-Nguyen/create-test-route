from selenium import webdriver
from random import randint
from datetime import datetime, timedelta
import time

# *** CONFIG ***
#Put your email, password, driver name, admin, admin's phone n0 here
email = 'NAME.sharingexcess@gmail.com'
password = 'YOUR-PASS-WORD'
mydriver = 'NAME' #eg: Chi Nguyen
admin = 'NAME'
admin_phone = '555555555'

# *** UTILS ***
#Convert time to string
def strTime(time):
    if time.hour < 12:
        mytime = time.strftime("%H%M") + "AM"
        return mytime
    else:
        mytime = time.strftime("%H%M")
        return mytime

#Create Start Time
def createStart(minutes):
    minutes_added = timedelta(minutes = minutes)
    start_time = datetime.now() + minutes_added
    start_str = strTime(start_time)
    return start_str

#Create End Time
def createEnd(hours):
    hours_added = timedelta(hours = hours)
    end_time = datetime.now() + hours_added
    end_str = strTime(end_time)
    return end_str

#Open Chrome window
driver = webdriver.Chrome()

# *** CREATING ROUTE ***
#Logging in
driver.find_element_by_css_selector('#email').send_keys(email)
driver.find_element_by_css_selector('#password').send_keys(password)
login = driver.find_element_by_css_selector('#submit')
login.click()
time.sleep(1) #load time, can be reduced

#Click on Post and choose One Time Route
post_button = driver.find_element_by_css_selector('#schedule-content > div.mb-4 > button.btn.btn-primary.network-activate-button.modal-button')
post_button.click()
one_time = driver.find_element_by_css_selector('#onetime-route-button')
one_time.click()
time.sleep(1)

#Selecting a random route template
select)template = driver.find_element_by_css_selector('#select-route-template')
select_template.click()

table = driver.find_element_by_class_name('network-table')
rows = table.find_elements_by_tag_name('tr')

route = 'RT-' + str(random.randint(1, 10))

for row in rows:
	col = row.find_elements_by_tag_name("td")
	if len(col) != 0 and col[0].text == route:
		col[-1].click()
		break

#Sending driver and admin information
driver.find_element_by_css_selector('#assign-employee-input').send_keys(mydriver)
time.sleep(1)
driver.find_element_by_class_name('assign-employee-button').click()
driver.find_element_by_css_selector('#admin_name').send_keys(admin)
driver.find_element_by_css_selector('#admin_phone').send_keys(admin_phone)

#Sending today's date
date = datetime.now().strftime("%m%d%Y")
driver.find_element_by_css_selector('#route_date').send_keys(date)

#Sending start and end time
start = createStart(5)
end =  createEnd(2)
driver.find_element_by_css_selector('#route_time-start_time').send_keys(start)
driver.find_element_by_css_selector('#route_time-end_time').send_keys(end)

#Submiting route
driver.find_element_by_css_selector('#submit').click()
time.sleep(2)

#Logging out and close window
driver.find_element_by_xpath('/html/body/header/nav/div/div/div/a[2]').click()
driver.close()

















    
