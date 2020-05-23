import requests
import json


url = "https://hackerone.com/reports/{}.json"


def hunter(keywords=[]):
    with open("eggs.csv") as eggs:
        reports = eggs.readlines()
    for each_report in reports:
        # print(each_report,end="\n")
        try:
            URL = url.format(each_report.replace("\n",''))
            page = requests.get(URL)
            data = json.loads(page.text)
            if any(x in data['vulnerability_information'].lower() for x in keywords):
                print("\n\n"+"="*10+"\n")
                print("\n"+"\t"*2+data['url'])
                print("\n"+data['title'])
                print("\n", data['severity'])
            else:
                print(".", end=''   )
        except KeyboardInterrupt:
            print("\n[+] Terminating")
            exit()
        except Exception as e:
            print(f"\n{each_report}[-] Skipping Something ({e}) ==> Probably report is not public")






def my_parser(mylist):
    keywords = list(filter(None, mylist.split(",")))
    hunter(keywords)
