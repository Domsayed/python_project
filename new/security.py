from datetime import datetime as dt 
import time 
tem_hosts="hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]
while True:
    today=dt.now()

    if (dt(dt.now().year,dt.now().month,dt.now().day,7)<today<dt(dt.now().year,dt.now().month,dt.now().day,8)):
        print('no means no',dt.now())
        with open(tem_hosts,'r+')as file:
            content=file.read()
            for website in website_list:
                if(website in content):
                    pass
                else:
                    file.write(redirect+" "+ website +"\n")    
        
    else:
        print('yes',dt.now())
        with open(tem_hosts,'r+')as file:
            content=file.read()
            for website in website_list:
                if(website in content):
                    pass
                else:
                    file.write(" "+ website +"\n")    
        
    time.sleep(1)    
# print(dt(dt.now().year,dt.now().month,dt.now().day))