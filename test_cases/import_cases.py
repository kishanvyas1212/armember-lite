from features.wp_login import login
from features.register import setup
from features.validate import validate
from features.wp_login import driver_initlise
import pandas as pd
import json
data = pd.read_csv("test_cases\\automated_test_cases.csv")
# column_lists = {}
# for col in data.columns:
#     column_lists[col] = data[col].tolist()

# user_data_unfiltered = column_lists["user_data"]
# user_data = []
# for listitem in user_data_unfiltered:
#     listitem = listitem.replace("\n","")
#     user_data.append(listitem)
# Action_id = column_lists["Action_id"]
# case_id = column_lists["id"]



class actions:


    def loginfun(drivers,action_id,data,url,error_message):
        if action_id == 1:
            usercookies = login.login_with_armember(drivers,data,url)
            status =validate.verifyuser(drivers,usercookies,data,error_message)
            if status == 1:
                redirected = validate.redirection_validation(drivers,data["redirect_url"])
                return redirected,usercookies
        elif action_id == 0:
            usercookies = login.login_with_wordpress(drivers,data,url)
            return [1,"using wordpress"], usercookies
        
                

    def action_identifier(action_id,user_data,i,url,error_msg):
        drivers = driver_initlise()
        if action_id == 1 or action_id ==0:
            actions.loginfun(drivers,action_id,user_data,url,error_msg)    
        drivers.quit()
        
        pass



    
def run_test_cases():
    column_lists = {}
    for col in data.columns:
        column_lists[col] = data[col].tolist()

    user_data_unfiltered = column_lists["user_data"]
    user_data = []
    for listitem in user_data_unfiltered:
        listitem = listitem.replace("\n","")
        
        user_data.append(listitem)
    Action_id = column_lists["Action_id"]
    case_id = column_lists["id"]

    for i in range(0,len(case_id)):
        
        json_string = user_data[i]
        data_dict = json.loads(json_string)
        # print(column_lists["url"][i] + user_data[i]["end_point"] )
        status = actions.action_identifier(Action_id[i],data_dict,i,column_lists["url"][i],column_lists["Error_Message"][i])
        print('itereation is over '+ str(i))

