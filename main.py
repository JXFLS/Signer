# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import ElementNotVisibleException 
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

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
    work.implicitly_wait(0.2)
    work.find_element_by_id("email").send_keys(user.Username())
    work.implicitly_wait(0.2)
    work.find_element_by_id("passwd").send_keys(user.Password())
    work.implicitly_wait(0.2)
    work.find_element_by_id("login").click()
    return

def main():
    users = get_user()
    var = 0
    bests = []
    res = []
    names = []
    tot = 0
    for user in users:
        login(user)
        try:
            remain = wait.until(EC.visibility_of_element_located((By.ID, 'remain')))
        except TimeoutException:
            with open('error.log','a') as ferr:
                ferr.write("ERROR! " + user.Username() + ":Failed to login\n")
        with open('signer.log', 'a') as l:
            l.write(user.Username() + ':remain: ' + remain.text + '\n')
        try:
            button = work.find_element_by_id('checkin')
            button.click()
            with open('signer.log', 'a') as l:
                l.write(user.Username + ":check in successfully\n")
            tot = tot + 1
            record = work.find_element_by_id('msg').text
            num = str(text[4:-6])
            strnum = text[4:-6]
            with open('signer.log', 'a') as l:
                l.write(user.Username() + ":get " + strnum + '\n')
            res.append(num)
            names.append(user.Username())
            if (var < num):
                 var = num
        except NoSuchElementException:
            with open('error.log','w') as ferr:
                ferr.write("warning:" + user.Username() + ":has checked in\n")
        work.implicitly_wait(0.5)
        work.get(URL + "/user/logout")
        work.implicitly_wait(0.5)
    work.quit()
    for i in range(len(names)):
        if res[i] == var:
            bests.append(names[i])
    with open('signer.log', 'a') as l:
        l.write("Today's best person/people is/are....")
    if tot > 0:
        for best in bests:
            with open('signer.log', 'a') as l:
                l.write(best + " ")
        with open('signer.log', 'a') as l:
            l.write("they got " + str(var) + '\n')
    else:
        with open('signer.log', 'a') as l:
            l.write("No one! Lucky next time~~")
    return

ff_options = webdriver.firefox.options.Options()
ff_options.add_argument('--headless')
work = webdriver.Firefox(options=ff_options)
#work = webdriver.Firefox()
wait = WebDriverWait(work, 20)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        with open('error.log','w') as ferr:
            ferr.write(str(e))
    finally:
        work.quit()
