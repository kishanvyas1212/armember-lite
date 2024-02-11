from utilities.get_element import get_element as ge
class validate:
    def verifyuser(drivers,cookie_list,data,error_message):
        if len(cookie_list) > 1:
            desired_name = "wordpress_logged_in_d0ae86309cda26b347aa32d9ce217696"
            cookie_value = next((cookie for cookie in cookie_list if desired_name in cookie['name'] ), None) 
            if data["username"] in cookie_value["value"] : 
                print("login case is passed user:" + data["username"] + " is logged in successfully")
            else:
                print("it is not working")
                print(data["username"])
                print(cookie_value)
            return 1
        else:
            error = ge.wait_for_element_display(drivers,"arm-df__fc--validation__wrap",20)
            if error_message in error:
                print("Test Case Passed")
                print(error)
            return 0
    def registerformverification(drivers):
       
        # in this we can check only two field validation, username and user email, so need to check this two only
        # below code to check the error message
        try: 
            error_msg =  ge.wait_for_element_display(drivers,"arm-df__fc--validation__wrap")
            # print(type(error_msg))
            # print(error_msg)
        
        except: 
            
            print("no error is displayed it works properly")
            return 0, "no error is found"
        else: 
            return 1,error_msg
    def redirection_validation(drivers,expected_url):
        redirected_url = drivers.current_url
        if redirected_url == expected_url:
            print("it redirects properly, the redirection works properly")
            return 1, redirected_url
        else:
            print("redirection is not working properly")
            return 0, redirected_url