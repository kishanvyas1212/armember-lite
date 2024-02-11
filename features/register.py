import time
from utilities.get_element import get_element as ge
from features.validate import validate
from features.payment_gateway import payment_gateways as pw

    
class setup:
    
        # this is for armember registration check and setup check using bank
        # transport and paypal method but as of now i cann't check the paypal in local so only bank transfer
        # drivers = driver_initlise()
        # before_cookies = drivers.get_cookies()
        def register(drivers,data,called_by,url):
            # before_cookies = drivers.get_cookies()
            drivers.get(url+"/" +data["end_point"])         
            locator = data["locator"]
            locatorpath = data["locatorpath"]
            action = data["action"]
            # error_locator = data["error"]       
            redirection_url = data["redirect_url"] 
            check_validation = data["check_validation"]
            # for i in range(0, len(locator)):
            #     element = findelement(drivers,locator[i],locatorpath[i],action[i])
            #     time.sleep(1)
            #     if i == (i-1):
            #         validate.registerformverification(username_value,user_email_value,error_locator)
            ge.findelement(drivers,locator[0],locatorpath[0],action[0],data["username"])
            ge.findelement(drivers,locator[1],locatorpath[1],action[1],data["first_name"])
            ge.findelement(drivers,locator[2],locatorpath[2],action[2],data["lastname_name"])
            ge.findelement(drivers,locator[3],locatorpath[3],action[3],data["user_email"])
            ge.findelement(drivers,locator[4],locatorpath[4],action[4],data["user_pass"])
            time.sleep(1)
            if check_validation == 1:
                validation = validate.registerformverification(drivers)
                if validation[0] == 0:
                    submit_form = ge.findelement(drivers,locator[5],locatorpath[5],action[5])
                else:
                    print("add error handling, if use the csv or spread sheet to move forward then add the required code")
                    error_msg = validation[1]
                    print(error_msg)
                    print(type(error_msg))
                    if "username" in validation[1]:
                        print("the used username is already exist")
                        return validation[1]
                    elif "email" in validation[1] :
                        print("the used email is already exist")
                        return validation[1]
            elif called_by==0:
                submit_form = ge.findelement(drivers,locator[5],locatorpath[5],action[5])
                time.sleep(10)
                drivers.refresh()
                time.sleep(1)
                after_cookies = drivers.get_cookies()
                # check the redirection validation
                redirection = validate.redirection_validation(drivers,data["redirect_url"])
                if redirection[0] == 1:
                    print("redirected to " + redirection_url + " which is working properly")
                elif redirection[0] ==0:
                    print("redirection is not working proeprly, it redirected to " + redirection[1] + " and which is not same as the expected url " + redirection_url)
                return after_cookies
            elif called_by==1:
                return locator[5],locatorpath[5],action[5]
            
        
        def setup_with_new(drivers,data,url):
            # devide it in three parts first select plan, 
            # then fill the form, 
            # select payment gateways and fill the details 
            # for form we can user above the fuction as it is except submit button

            called_by = 1
            submitbtn = "ARMSETUPSUBMIT"
            first_setp = setup.register(drivers,data,called_by,url)
            pw.bank_transfer(drivers,data)
            time.sleep(2)       
            # add bank details
            time.sleep(5)
            submit_form = ge.findelement(drivers,"NAME",submitbtn,"click")
            time.sleep(10)
            
            return drivers.get_cookies() 
