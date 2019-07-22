# -*- coding:utf-8 -*-

from selenium import webdriver
import time

Source = "users.inf"
URL = "https://www.10ms.ml"

class User(object):
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def Username(self, name=None):
        if name is not None:
            self.username = name
        return self.username
    
    def Password(self, word=None):
        if word is not None:
            self.password = word
        return self.password


def get_user():
    file = open(Source, 'r')
    datas = file.readlines()
    file.close()
    users = [User(datas[i*2][:-1],datas[i*2+1][:-1]) for i in range(len(datas)//2)]
    return users

def login(user):
    work.get(URL + "/auth/login")
    time.sleep(1)
    work.find_element_by_id("email").send_keys(user.Username())
    # time.sleep(1)
    work.find_element_by_id("passwd").send_keys(user.Password())
    # time.sleep(1)
    work.find_element_by_id("login").click()
    time.sleep(1)
    return

def main():
    users = get_user()
    for user in users:
        login(user)
        try:
            work.find_element_by_id("checkin").click()
        except:
            print(user.Username(), "has checked in.")
        time.sleep(1)
        work.get(URL + "/user/logout")
        time.sleep(1)
    time.sleep(1)
    return

ff_options = webdriver.firefox.options.Options()
ff_options.add_argument('--headless')
work = webdriver.Firefox(options=ff_options)

if __name__ == '__main__':
    main()
    work.quit()