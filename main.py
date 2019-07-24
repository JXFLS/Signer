# -*- coding:utf-8 -*-

from signer.pre import getYaml
from signer.notice import notice

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

Config = getYaml()
URL = "https://www.10ms.ml"


def login(user):
    print(user['email'])
    work.get(URL + "/auth/login")
    work.implicitly_wait(0.2)
    work.find_element_by_id("email").send_keys(user['email'])
    work.implicitly_wait(0.2)
    work.find_element_by_id("passwd").send_keys(user['password'])
    work.implicitly_wait(0.2)
    work.find_element_by_id("login").click()
    return


def sendNotice(title, text):
    key = Config['sendkey']
    notice(key, title, text)


def main():
    users = Config['users']
    var = 0
    bests = []
    res = []
    names = []
    tot = 0
    for user in users:
        login(user)
        try:
            remain = wait.until(
                EC.visibility_of_element_located((By.ID, 'remain')))
        except TimeoutException:
            sendNotice("ERROR!", user['email'] + ": failed to login\n")
            with open('error.log', 'a') as ferr:
                ferr.write("ERROR! " + user['email'] + ": failed to login\n")
        with open('signer.log', 'a') as l:
            l.write(user['email'] + ':remain: ' + remain.text + '\n')
        try:
            button = work.find_element_by_id('checkin')
            button.click()
            with open('signer.log', 'a') as l:
                l.write(user.Username + ":check in successfully\n")
            tot = tot + 1
            record = work.find_element_by_id('msg').text
            num = str(record[4:-6])
            strnum = record[4:-6]
            with open('signer.log', 'a') as l:
                l.write(user['email'] + ":get " + strnum + '\n')
            res.append(num)
            names.append(user['email'])
            if (var < num):
                var = num
        except NoSuchElementException:
            sendNotice("warning:", user['email'] + ": has checked in\n")
            with open('error.log', 'w') as ferr:
                ferr.write("warning:" + user['email'] + ": has checked in\n")
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
wait = WebDriverWait(work, 20)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        with open('error.log', 'w') as ferr:
            ferr.write(str(e))
    finally:
        work.quit()
