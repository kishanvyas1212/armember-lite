from utilities.get_element import get_element as ge
#  this file contains all payment gateways and i can call it from setup form

class payment_gateways:
        
    def bank_transfer(drivers,data):
        
        plan_locator = data['plan_locator']
        bank_locator = data["bank_locator"]
        bank_identified = data["bank_identified"]
        ge.findelement(drivers,plan_locator[0],plan_locator[1],plan_locator[2],value=1)
        ge.findelement(drivers,bank_identified[0],bank_locator[0],"send_keys",data["tr_id"])
        ge.findelement(drivers,bank_identified[1],bank_locator[1],"send_keys",data['bankname'])
        ge.findelement(drivers,bank_identified[2],bank_locator[2],"send_keys",data['holdername'])
        ge.findelement(drivers,bank_identified[3],bank_locator[3],"send_keys",data['note'])
        return 1
        
        
        
        
    def paypal():
        pass
        # currently not adding any code because i have no https website
    

    