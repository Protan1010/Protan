import requests

def Sent(num):
    url = f"https://www.bioscopelive.com/en/login/send-otp?phone=88{num}&operator=bd-otp"
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x64; rv:96.0) Gecko/20100101 Firefox/96.0"
    }
    res = requests.get(url=url , headers=header)
    if res.status_code == 200:
        return True
    else:
        return False