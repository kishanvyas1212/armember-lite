
from features.wp_login import setup, validate
from features.wp_login import driver_initlise
from time import sleep
url = "http://localhost/test_lite1"
register_data = {
    "username": "armember21",
    "first_name" :"armember21",
    "lastname_name" : "armember21",
    "user_email":"armember21@gmail.com",
    "user_pass":"armember21",
    "error" : "arm-df__fc--validation__wrap",
    "locator": ["NAME","NAME","NAME","NAME","NAME","NAME"],
    "locatorpath":["user_login","first_name","last_name","user_email","user_pass","armFormSubmitBtn"],
    "action":["send_keys","send_keys","send_keys","send_keys","send_keys","click"],
    "redirect_url" : "http://localhost/test_lite1/edit_profile/",
    "check_validation":0,
    "holdername":"test",
    "bankname":"test",
    "tr_id":"test",
    "note":"this is for testing purposes only",
    "plan_locator": ["id","arm_subscription_plan_option_2","click"],
    "bank_locator": ["bank_transfer[transaction_id]","bank_transfer[bank_name]","bank_transfer[account_name]","bank_transfer[additional_info]" ],
    "bank_identified":["name","name","name","name"],
    "end_point":"setup"
} 
# register = setup.register(register_data,0)
driver = driver_initlise()
signup = setup.setup_with_new(register_data,driver,url)
print(signup)
validate.verifyuser(signup,register_data,driver)

sleep(10)
driver.quit()

