# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    time.sleep(0.2)
    work.find_element_by_id("email").send_keys(user.Username())
    time.sleep(0.2)
    work.find_element_by_id("passwd").send_keys(user.Password())
    time.sleep(0.2)
    work.find_element_by_id("login").click()
    return

def main():
    users = get_user()
    var = 0; bests = []; res = []; names = []; tot = 0
    for user in users:
        login(user)
        try:
            remain = wait.until(EC.visibility_of_element_located((By.ID, 'remain')))
        except:
            with open('error.log','w') as ferr:
                ferr.write("ERROR! " + user.Username() + ":Failed to login")
            continue
        names.append(user.Username())
        print(user.Username() + ':remain: ' + remain.text)
        try:
            work.find_element_by_id("checkin").click()
            print(user.Username() + ":check in successfully")
            tot = tot + 1
            record = work.switch_to_alert().text[4:9]
            print(user.Username() + ":get: " + record)
            res.append(int(record))
            if (var < int(record)):
                 var = int(record)
        except:
            with open('error.log','w') as ferr:
                ferr.write("warning:" + user.Username() + ":has checked in")
        time.sleep(1)
        work.get(URL + "/user/logout")
        time.sleep(1)
    work.quit()
    i = 0
    for name in names:
        i = i + 1
        if i > tot:
            break
        if res[i] == var:
            bests.append(names[i])

    print("Today's best person/people is/are....", end = " ")
    for best in bests:
        print(best,end = " ")
    if tot == 0:
        print("No one! = =")
    return

ff_options = webdriver.firefox.options.Options()
ff_options.add_argument('--headless')
work = webdriver.Firefox(options=ff_options)
wait = WebDriverWait(work, 5)
#work = webdriver.Firefox()


if __name__ == '__main__':
    main()
