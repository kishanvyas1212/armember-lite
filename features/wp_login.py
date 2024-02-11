import time
from selenium import webdriver #by this we can access the webdriver which is inbuild method of selenium
from selenium.webdriver.chrome.service import Service   #This is selenium 4 new feature in which we import service 
from utilities.get_element import get_element as ge

# test
def driver_initlise():
    ser_Obj = Service("C:\\Users\\91635\\Desktop\\drivers\\chromedriver.exe")
# ser_Obj = Service("C:\\Users\\91635\\Desktop\\drivers\\geckodriver.exe")

    drivers = webdriver.Chrome(service= ser_Obj)
    drivers.implicitly_wait(60)
    
    return drivers
    

              
class login():
    
    def login_with_wordpress(drivers,data,url):
        login_url = url + data["end_point"]
        print(login_url)
        drivers.get(login_url)
        usernamef = ge.findelement(drivers,"ID","user_login","send_keys",data["username"])
        pwd = ge.findelement(drivers,"ID","user_pass","send_keys",data["password"])
        beforelogin = drivers.get_cookies()
        login = ge.findelement(drivers,"NAME","wp-submit","click")
        usercookies = drivers.get_cookies()
        drivers.delete_all_cookies()
        return usercookies
    def login_with_armember(drivers,data,url):
        # login_url = 
        print(url)
        drivers.get(url + data["end_point"])
        usernamef = ge.findelement(drivers,"NAME","user_login","send_keys",data["username"]) 
        pwd = ge.findelement(drivers,"NAME","user_pass","send_keys",data["password"])   
        beforelogin = drivers.get_cookies()
        login = ge.findelement(drivers,"NAME","armFormSubmitBtn","click")
        time.sleep(2)
        # drivers.refresh() #commented this because later want to validate user so if refresh then error message will disappear so increase wait to avoid issue
        time.sleep(2)
        usercookies = drivers.get_cookies()
        # print(usercookies)
        # print(len(usercookies))
        return usercookies
        
    
    
    
        
