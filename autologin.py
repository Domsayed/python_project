import webbrowser
import datetime
link= input("Enter Link:")
hr=int (input("Enter Hour:"))
min=int (input ("Enter mintute:"))
while True:
    hour=int(datetime.datetime.now().hour)
    minute=int(datetime.datetime.now().minute)
    if hour==hr and minute==min:
        webbrowser.open(link)
        break