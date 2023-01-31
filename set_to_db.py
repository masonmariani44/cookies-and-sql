#! /usr/bin/python3

import os
import sys
import cgi
from http import cookies
import pymysql
import requests

if os.environ["REQUEST_METHOD"] != "POST":
	print("Status: 405 Method Not Allowed")
	print("Allow: POST")
	print()
	sys.exit(0)

form = cgi.FieldStorage()
if "username" in form:
	username = form["username"].value
else:
	username = None
if not username:
	print("Status: 400 Bad Request")
	print()
	sys.exit(0)

ID_as_str = form["ID_as_str"].value

print("Status: 200 OK")
print("Content-Type: text/html")
print()

conn = pymysql.connect("proj8.cd3aeashjner.us-east-1.rds.amazonaws.com", "mason_DB", "pass_mason_DB", "proj8")
cursor = conn.cursor()

sql = f"INSERT INTO SESSIONS(SESSION_ID, USERNAME) VALUES ('%s', %s)" %(ID_as_str, username)
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()

conn.close()

print("<html><body>")
print()

print("<h1>Start server</h1>")
print("<a href=\"/cgi-bin/start_server\"; Click here</a>")
	
print("</html></body>")
print()