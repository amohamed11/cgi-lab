#!/usr/bin/env python3
import sys
import os
import cgi
import cgitb
from templates import login_page, secret_page
from secret import username, password
cgitb.enable()

def login(u, p):
    if u == username and p == password:
        print("Set-Cookie:UserID = %s;" % (u))
        print("Set-Cookie:Password = %s;\r\n" % (p))


def checkCookies():
    user_id = ""
    cookiePass = ""
    if 'HTTP_COOKIE' in os.environ:
        cookies = os.environ['HTTP_COOKIE']
        cookies = cookies.split(';')

        for cookie in cookies:
            keyValue = cookie.split('=')
            if keyValue[0] == "UserID":
                user_id = keyValue[1]
            if keyValue[0] == "Password":
                cookiePass = keyValue[1]
        
    return user_id, cookiePass

u, p = checkCookies()

posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    for line in posted.splitlines():
        lineSplit = line.split('&')
        u = lineSplit[0].split('=')[1]
        p = lineSplit[1].split('=')[1]
        login(u, p)

print("Content-Type: text/html\r\n\r\n")
if u == "":
    print(login_page())
else:
    print(os.environ['HTTP_COOKIE'])
    print(secret_page(u, p))