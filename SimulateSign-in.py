# -*- coding: utf-8 -*-
from selenium import webdriver
import time


def get_sub_str(_str, left, right):
    str_left = _str.find(left)
    str_right = _str.find(right, str_left + len(left))
    _sub_str = _str[str_left + len(left):str_right]
    return str_left + len(left), _sub_str


def is_element_exist(_driver, element):
    flag = True
    try:
        _driver.find_element_by_class_name(element)
        return flag
    except:
        flag = False
        return flag


driver = webdriver.Chrome()

try:
    driver.get("https://www.douyu.com/directory/myFollow")
    time.sleep(2)
    f = True
    while f:
        try:
            driver.find_element_by_class_name('UnLogin-icon').click()
            f = False
        except:
            time.sleep(0.5)
    time.sleep(15)  # 等待登陆成功
    '''
    # 斗鱼真牛逼，人机检测要是机器人验证码都不刷新出来！！牛逼，我服了
    driver.switch_to.frame('login-passport-frame')
    driver.find_element_by_class_name('js-qrcode-switch').click()
    time.sleep(1)
    driver.find_element_by_name('phoneNum').clear()
    driver.find_element_by_name('phoneNum').send_keys('19801231323')  # 手机号
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys('shuo1092')  # 斗鱼密码
    driver.find_element_by_class_name('loginbox-sbt').click()  # 点击登陆按键
    '''
    page = driver.page_source
    index, page = get_sub_str(page, '<ul class="layout-Cover-list">', '</ul>')
    room_num = []
    while True:
        index = page.find('" target="_blank"></a>')
        if index < 0:
            break
        sub_str = page[index - 10:index]
        room_num.append(sub_str[sub_str.find('/') + 1:])
        page = page[index + 10:]
    while True:
        index, sub_str = get_sub_str(page, 'href="/', '"')
        if index - len('href="/') < 0:
            break
        page = page[index:]
        room_num.append(sub_str)

    room_del = ['5681010', '4818868', '6263488', '5040227']

    for i in range(len(room_del)):
        room_num.remove(room_del[i])

    print(len(room_num))
    print(room_num)

    # 5681010, 4818868, 6263488
    i = 0
    while i < len(room_num):
        print(i, room_num[i])
        driver.get("https://www.douyu.com/" + room_num[i])
        time.sleep(3)
        f = True
        while f:
            try:
                driver.find_element_by_class_name('ChatSend-txt')
                f = False
            except:
                time.sleep(0.5)
        driver.find_element_by_class_name('ChatSend-txt').send_keys('1')

        # 把侧边广告关了
        try:
            if is_element_exist(driver, 'ActBase-switch'):
                driver.find_element_by_class_name('ActBase-switch').click()
            if is_element_exist(driver, 'wm-universal-close'):
                driver.find_element_by_class_name('wm-universal-close').click()
            if is_element_exist(driver, 'BargainingKit-closeBtn'):
                driver.find_element_by_class_name('BargainingKit-closeBtn').click()
        except:
            print('关闭广告栏失败，正在重试...')
            continue

        f = True
        while f:
            try:
                driver.find_element_by_class_name('ChatSend-button').click()
                f = False
            except:
                time.sleep(0.5)
        if is_element_exist(driver, 'ActiviesExpanel-ExpandBtn'):
            f = True
            while f:
                try:
                    driver.find_element_by_class_name('ActiviesExpanel-ExpandBtn').click()
                    f = False
                except:
                    time.sleep(0.5)
            time.sleep(0.5)
        else:
            time.sleep(2)
            if is_element_exist(driver, 'ActiviesExpanel-ExpandBtn'):
                try:
                    driver.find_element_by_class_name('ActiviesExpanel-ExpandBtn').click()
                except:
                    print('点击ActiviesExpanel-ExpandBtn失败，正在重试...')
                    continue

        if is_element_exist(driver, 'RoomLevelDetail-icon'):
            f = True
            while f:
                try:
                    driver.find_element_by_class_name('RoomLevelDetail-icon').click()
                    f = False
                except:
                    time.sleep(0.5)
            time.sleep(0.5)
        else:
            print(room_num[i], '未签到成功')
            continue
        if is_element_exist(driver, 'Autograph-grayTip'):
            try:
                driver.find_element_by_class_name('Autograph-grayTip').click()
            except:
                print('点击Autograph-grayTip失败，正在重试...')
                continue
        if is_element_exist(driver, 'is-sign'):
            f = True
            while f:
                try:
                    driver.find_element_by_class_name('is-sign').click()
                    f = False
                except:
                    time.sleep(0.5)
        time.sleep(0.5)
        # driver.find_element_by_class_name('RoomLevelDetail-level--no').click()

        i = i + 1

    # print(room_num)

    # print(page)
    # driver.get("https://www.douyu.com/1557274")
    print('end')
    time.sleep(5)

finally:
    driver.close()  # 关闭浏览器

    '''
        driver.switch_to.frame('login_frame')  # 切换到登陆界面
        driver.find_element_by_id('switcher_plogin').click()  # 选择帐号密码登陆
        driver.find_element_by_name('u').send_keys('2395967268')  # QQ号
        driver.find_element_by_name('p').clear()
        driver.find_element_by_name('p').send_keys('Shuo@1092')  # QQ密码
        driver.find_element_by_id('login_button').click()  # 点击登陆按键
        time.sleep(2)

    '''
