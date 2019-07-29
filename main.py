# -*- coding:utf-8 -*-

from sys import argv,exc_info
from time import asctime,sleep
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
msg = list()


def login(user):
    work.get(URL + "/user/logout")
    work.get(URL + "/auth/login")
    sleep(0.2)
    work.find_element_by_id("email").send_keys(user['email'])
    sleep(0.2)
    work.find_element_by_id("passwd").send_keys(user['password'])
    sleep(0.2)
    work.find_element_by_id("login").click()
    return


def errorToken(title, text):
    global msg
    with open('error.log', 'a') as ferr:
        ferr.write(asctime())
        ferr.write('\n')
        ferr.write(title)
        ferr.write(text)
        ferr.write('\n')
    for key in Config['sendkey']:
        msg.append(text + "    sending notice -> " + notice(key, title, text).decode())
    return

def main():
    global msg
    users = Config['users']
    var = int()
    bests = list()
    res = list()
    names = list()
    lucky = list()
    msg.append('-------' + asctime() + '-------')
    for user in users:
        login(user)
        try:
            remain = wait.until(EC.visibility_of_element_located((By.ID, 'remain')))
        except TimeoutException:
            errorToken("ERROR! ", user['email'] + " failed to login\n")
            continue
        sleep(1)
        try:
            # button = wait.until(EC.visibility_of_element_located((By.ID, 'checkin')))
            button = work.find_element_by_id('checkin')
            button.click()
            record = wait.until(EC.visibility_of_element_located((By.ID, 'msg'))).text
            strnum = record[4:-6]
            num = int(strnum)
            res.append(num)
            names.append(user['email'])
            if var < num:
                var = num
        except NoSuchElementException:
            msg.append(user['email'] + " has checked in, remain " + remain.text)
            continue
        wait.until(EC.visibility_of_element_located((By.ID, 'result_ok'))).click()
        remain = wait.until(EC.visibility_of_element_located((By.ID, 'remain')))
        msg.append(user['email'] + " check in successfully, get " + strnum + "MB, remain " + remain.text)
    for i in range(len(names)):
        if res[i] == var:
            bests.append(names[i])
    if len(bests)==1:
        lucky.append("Today's best person is... ")
        lucky.append(bests[0])
        lucky.append(" got ")
        lucky.append(str(var))
        lucky.append("MB!")
    elif len(bests)==0:
        lucky.append("Today's best person is... Nobody! Lucky next time~~")
    else:
        lucky.append("Today's best people are... ")
        lucky.append(' '.join(bests))
        lucky.append(" got ")
        lucky.append(str(var))
        lucky.append("MB!")
    msg.append(''.join(lucky))
    return


ff_options = webdriver.firefox.options.Options()
ff_options.add_argument('--headless')
work = webdriver.Firefox(options=ff_options)
wait = WebDriverWait(work, 20)
work.implicitly_wait(1)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        err = "Exception: { " + str(e) + " } Details: { " + str(exc_info()) + " }"
        msg.append(err)
        errorToken("ERROR! ", err)
    finally:
        output = '\n'.join(msg) + '\n'
        with open('signer.log','a') as fout:
            fout.write(output)
        work.quit()
        print(output)
