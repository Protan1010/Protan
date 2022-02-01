import requests
def Sent(num):
    url = "https://www.grameenphone.com/myoffers/verify-number/e242660df1b69b74dcc7fde711f924ff"
    data = { "anon_token":"Mtc3D20L4TWVY0M8dgPNx5tp-EaEtezpecSYJKX_oI4+","myoffer_msisdn":num}
    response = requests.post(url=url , data=data)
    if response.status_code == 200:
        return True
    else:
        return False
