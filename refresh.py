import requests
from bs4 import BeautifulSoup


def refresh_list(count=5):
    no=0
    reports=[]
    url="https://hackerone.com/reports/"
    try:
        for i in range(0,count):
            print("\nCollecting page "+str(i+1))
            URL = 'http://h1.nobbd.de/index.php?start='+str(no)
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            results=soup.find(id='reports-all').find_all(class_='title')
            for n in results:
                s=n['href'].split("/")[-1]
                print(s, end=', ')
                reports.append(s)
            else:
                print("\b\b ") # removes last , char and overwrites with space char
            no+=20
    except:
        pass
    finally:
        print("\n\n[+] Total fetched: ", len(reports))


def save_to_db(reports):
    with open('eggs.csv', 'a') as eggs:
        for each_report in reports:
            eggs.write(each_report+'\n')
