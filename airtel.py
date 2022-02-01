import imp


import requests


def Sent(num):
    url = "https://api.bd.airtel.com/v1/otp/send_request"
    data = {"phone_number":num,
            "lang":"en","type":"internet_package",
            "plan_type":"internet_package",
            "uid":"b94f4d21-a999-494b-a2cd-752f4af635cd"}
    header = {
        "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmJkLmFpcnRlbC5jb21cL3YxXC90b2tlbiIsImlhdCI6MTY0MzY4NTY1NiwiZXhwIjoxNjQzNzcyMDU2LCJuYmYiOjE2NDM2ODU2NTYsImp0aSI6Im5yeEF0ZnBLZTdEaXZlUjYiLCJzdWIiOiJBaXJ0ZWwifQ.LS25LLrZOE4MeMBWw6T6Hy9_HOBxt1UA7DU2fnuppX0",
        "X-CSRF-TOKEN":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmJkLmFpcnRlbC5jb21cL3YxXC90b2tlbiIsImlhdCI6MTY0MzY4NTY1NiwiZXhwIjoxNjQzNzcyMDU2LCJuYmYiOjE2NDM2ODU2NTYsImp0aSI6Im5yeEF0ZnBLZTdEaXZlUjYiLCJzdWIiOiJBaXJ0ZWwifQ.LS25LLrZOE4MeMBWw6T6Hy9_HOBxt1UA7DU2fnuppX0"
    }
    res = requests.post(url=url , data=data , headers=header)
    if res.status_code == 200:
        return True
    else:
        return False