#!/usr/bin/python-3.9.1
# -*- coding: utf-8 -*-
# auto douyu check in

import os
import urllib.request
from io import BytesIO
import gzip
import time
import os
import csv
import datetime
import re

login_url = "https://www.douyu.com/directory/myfollow"


def get_response_html(u, h):
    request = urllib.request.Request(u, headers=h)
    response = urllib.request.urlopen(request)
    _html = response.read()
    buff = BytesIO(_html)
    f = gzip.GzipFile(fileobj=buff)
    _html = f.read().decode('utf-8')
    return _html

"""
cookie = input("请输入您斗鱼账户的cookie值：")
headers = {
    "authority": "www.douyu.com",
    "method": "GET",
    "path": "/directory/myFollow",
    "scheme": "https",
    "accept": "text/html, application/xhtml+xml,application/xml;q = 0.9,image/webp,image/apng,*/*;q = 0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "max-age=0",
    "cookie": cookie,
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) Applewebkit/537.36(KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68"
}
"""
# html = get_response_html(login_url, headers)
# print(html)

# dy_did=bfba81e3e6c6f879cc2ceee500011601; acf_did=bfba81e3e6c6f879cc2ceee500011601; acf_auth=5809jjgwpqti3w16mks+ru5faeimfsirbiko7c+qfao2hso3t38fsazp0dgezavgma8hornrlbxcgausggiovmm7c8vnipjhjbbqrifisqknrgmm+hhwqds; dy_auth=1fbbeioxuwkfp2aturk7a/fdqxsqzqy/2mgdiyczzsulzuo2uifyhkllooc1vvfq+yusiuiacrurls22qbh52xmzapklozewztur980dp569buzzukv1iok; wan_auth37wan=8fbd233731e4xb/akuldc902fwnfsbzzf+dzyjfeuvitubjesjvcgv5zqopoavd4csoyvmpp83wjo9iwptmktqw+jenswjajego2vrveawxkmtqv3gm; acf_uid=260012884; acf_username=260012884; acf_nickname=bupt硕硕; acf_own_room=1; acf_groupid=1; acf_phonestatus=1; acf_ct=0; acf_ltkid=45585638; acf_biz=1; acf_stk=99c2c257660f1980; acf_avatar=//apic.douyucdn.cn/upload/avatar_v3/202005/715bc903193b4d4a9aabdd8442e5758c_; hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1613131837,1613132448,1613285858; hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1613285871

str = "1886240', '5070576', '3168536', '290935', '2267291', '5182506', '6503272', '3284257', '3346900', '4782429', '5093994', '6872425', '9134908', '4328643', '3153272', '4195141', '718393', '1554170', '5639270', '1557274', '5047677', '533493', '5092355', '3857053', '4372875', '1943111', '138175', '606118', '4494106', '5878647', '3794905', '4615502', '3219235', '6550676', '101', '134000', '664668', '2947432', '574613', '3984748', '614786', '952595', '6495582', '99999', '4679086', '3767050', '52004', '6868395', '3733001', '592619', '4650531', '5551871', '4775361', '8090190', '1010383', '1966130', '4298793', '1149639', '7675562', '1858782', '9130913', '5045761', '5019555', '553338', '5243442', '3276456', '1139347', '7681886', '6852825', '5048676', '5140196', '3917746', '2282201', '1769784', '8042299', '7837174', '591080', '5243462', '5946317', '8738510', '5100055', '9034792', '8696437', '6857735', '5078723', '3656383', '9129370', '9217169"
arr = str.split("', '")

timestr = time.strftime("%Y%m%d")

outFilePath = "D:\\Workspace\\workspace_PyCharm\\DouyuCheckin\\outFile"
if not os.path.exists(outFilePath):
    try:
        os.makedirs(outFilePath)
    except OSError as err:
        raise err
outFilePath = outFilePath + '\\' + timestr + '.txt'
"""
with open(outFilePath, 'w+') as outfile:
    for i in range(len(arr)):
        outfile.write(arr[i] + '\n0' + '\n')
"""

i = 0
while i <= 10:
    print(i)
    if i == 5:
        i = i + 1
    i = i + 1





