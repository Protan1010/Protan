import requests
def Sent(num):
        url = "https://webapi.robi.com.bd/v1/send-otp"
        data = {"phone_number":num}
        header={"X-CSRF-TOKEN":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3dlYmFwaS5yb2JpLmNvbS5iZC92MS90b2tlbiIsImlhdCI6MTY0MzY1MTE2MCwiZXhwIjoxNjQzNzM3NTYwLCJuYmYiOjE2NDM2NTExNjAsImp0aSI6ImdNS2NhRDNJbFhORVo3TXEiLCJzdWIiOiJSb2JpV2ViU2l0ZSJ9.lgkinVsf7ZIATUyk43nzTzwFpQMqM4Fz0s-fHT936cU",
                "Authorization":
                "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3dlYmFwaS5yb2JpLmNvbS5iZC92MS90b2tlbiIsImlhdCI6MTY0MzY1MTE2MCwiZXhwIjoxNjQzNzM3NTYwLCJuYmYiOjE2NDM2NTExNjAsImp0aSI6ImdNS2NhRDNJbFhORVo3TXEiLCJzdWIiOiJSb2JpV2ViU2l0ZSJ9.lgkinVsf7ZIATUyk43nzTzwFpQMqM4Fz0s-fHT936cU"}
        response = requests.post(url=url,headers=header , data=data)
        if response.status_code == 200:
                return True
        else:
                return False