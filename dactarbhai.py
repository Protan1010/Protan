import requests
def Sent(num):
    url = "https://daktarbhai.com/login/mobile"
    data ={"mobile":num}
    header={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",
        "Cookie":"XSRF-TOKEN=eyJpdiI6ImpLdkFLUGYxclNEQnZ4YWNXV25CclE9PSIsInZhbHVlIjoia1ZMMDFrTVRDRGRVbkRGNloxTmJrZldZczQ0VWhKTXhhRlQ5SlwvMThUcmY5bTBqakJGcWVGNUFNNzJcL1h0djhRIiwibWFjIjoiYWY4NGI2M2YzZTU2M2UzOGUzMjRhMTYwYzBkY2U3ZTE2MDkyYTU5YjA3N2Q0NTc3Y2JkYzM3ZWM0ZmE1MjRiNSJ9; daktarbhai_web_session=eyJpdiI6Ik4xUzBlWmRnc0JVTUR3N1VIa2R1OVE9PSIsInZhbHVlIjoibGlCbllLanEzdnBDUnNqTnJlTXBcL1N6QXlkXC9EN0RjUWw5Ulh4d1BycXIreTI3MklkMVQzN2VieG1UXC8yVXhZdCIsIm1hYyI6ImJlZjI0M2QyNWIzYTA3ZDYwOTgzMThhMjQzYTdhMDZkZDUzZWI5ZjU1Y2UxOWM5ZjM1MmI5MjdhMzY3YzMyMGMifQ%3D%3D",
        "X-CSRF-TOKEN":"0BeH7fdnxb8yQPWep081l8mJinKmrSGeEtt5IXy1",
        "X-Requested-With":"XMLHttpRequest"
    }
    res = requests.post(url=url , headers=header,data=data)
    if res.status_code == 200:
        return True
    else:
        return False