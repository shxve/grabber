#!python3
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
from time import sleep


url = "https://iplogger.org/logger/cC8J3N1wqeo1"


def main():
    # code

    myips = {}
    mydevices = {}
    mytimes = {}
    
    for x in range(0, 3):
        sleep(1)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        temp_ips = soup.find_all(attrs={"class": "ip-address"})
        temp_isps = soup.find_all(attrs={"class": "ip-text"})
        temp_devices = soup.find_all(attrs={"class": "platform"})
        temp_browsers = soup.find_all(attrs={"class": "browser"})
        temp_dates = soup.find_all(attrs={"class": "ip-date"})
        temp_times = soup.find_all(attrs={"class": "ip-time"})

        for i in range(len(temp_ips)):
            ip = temp_ips[i].text.strip()
            isp = temp_isps[i].text.strip()
            device = temp_devices[i].text.strip()
            browser = temp_browsers[i].text.strip()
            date = temp_dates[i].text.strip()
            time = temp_times[i].text.strip()
            myips[ip] = isp
            mydevices[device] = browser
            mytimes[time] = date
    
    print(myips)
    print(mydevices)
    print(mytimes)
    
    return 0


if __name__ == '__main__':
    main()
