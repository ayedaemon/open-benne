# Open-benne
* * *
### A python tool which collects Hackerone publically available reports. Allows user to search for reports on the basis of keywords.

* * *

## How To Use
- Download tool
```sh
git clone https://github.com/ayedaemon/open-benne.git
```
- Install
```sh
pip3 install -r requirements.txt
```
- Get help
```
python3 benne.py -h
```
- Refresh Writeup List (Update DB)
```
python3 benne.py -r 10
```

- Search with keywords
```
python3 benne.py -s xss,information,disclosure,google,php,idor
```
