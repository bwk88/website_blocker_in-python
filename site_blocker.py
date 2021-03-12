import time
from datetime import datetime as dt


print("hello world")

website_temp="hosts"
website_host=r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list=["www.youtube.com","youtube.com"]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("work time")
        with open(website_temp,'r+') as file:
            content=file.read()
            for website in website_list :
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect + "   " + website +"\n")
    else:
        with open (website_temp,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                    file.truncate()
                    print("fun time")
                    time.sleep(5)
