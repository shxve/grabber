#!python3
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
from time import sleep
import keyboard


url = "https://iplogger.org/logger/cC8J3N1wqeo1"


def main():
    # code

    myips = {}

    while True:
        sleep(0.5)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        temp_ips = soup.find_all(attrs={"class": "ip-address"})
        temp_isps = soup.find_all(attrs={"class": "ip-text"})
        temp_devices = soup.find_all(attrs={"class": "platform"})
        temp_browsers = soup.find_all(attrs={"class": "browser"})
        temp_dates = soup.find_all(attrs={"class": "ip-date"})
        temp_times = soup.find_all(attrs={"class": "ip-time"})

        for i in range(len(temp_ips)):
            temp_list = []
            ip = temp_ips[i].text.strip()
            isp = temp_isps[i].text.strip()
            device = temp_devices[i].text.strip()
            browser = temp_browsers[i].text.strip()
            date = temp_dates[i].text.strip()
            time = temp_times[i].text.strip()

            temp_list.append(ip)
            temp_list.append(isp)
            temp_list.append(device)
            temp_list.append(browser)
            temp_list.append(date)
            temp_list.append(time)

            myips[i] = temp_list

    print(myips)

    return 0


if __name__ == '__main__':
    main()
