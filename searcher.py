import requests
import json


url = "https://hackerone.com/reports/{}.json"


def hunter(keywords=[]):
    with open("eggs.csv") as eggs:
        reports = eggs.readlines()
    for each_report in reports:
        print(".",end='')
        try:
            URL = url.format(each_report.replace("\n",''))
            page = requests.get(URL)
            data = json.loads(page.text)
            if any(x in data['vulnerability_information'].lower() for x in keywords):
                print("\n"+data['url'])
                print("\n"+data['title'])
        except KeyboardInterrupt:
            print("[+] Terminating")
            exit()
        except Exception as e:
            print(f"[-] Skipping Something ({e})")






def my_parser(mylist):
    keywords = list(filter(None, mylist.split(",")))
    hunter(keywords)
