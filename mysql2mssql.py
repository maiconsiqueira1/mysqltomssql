#!/usr/bin/python
import sys
import csv
import pymysql
import pymssql
from os import getenv

# Set Vars to Microsoft SQL database connection
mssqlserver = ("database1.address.local")
mssqluser = ("sa")
mssqlpwd = ("password")
mssqldbname = ("DATABASENAME")
skadb = pymssql.connect(mssqlserver, mssqluser, mssqlpwd, mssqldbname)

#Set Vars to MySQL database connection
mysqlserver = ("database2.address.local")
mysqluser = ("root")
mysqlpwd = ("password")
mysqldbname = ("DATABSENAME") 

# Open MySQL database connection
ocsdb = pymysql.connect(mysqlserver, mysqluser, mysqlpwd, mysqldbname)

# prepare a cursor object using cursor() method
cursormysql = ocsdb.cursor()

# execute SQL query using execute() method.
cursormysql.execute("select distinct accountinfo.TAG , hardware.NAME ,hardware.USERID, hardware.OSNAME , networks.MACADDR, accountinfo.HARDWARE_ID \
	from ocsweb.accountinfo inner join hardware on accountinfo.HARDWARE_ID = hardware.ID inner join networks on accountinfo.HARDWARE_ID = networks.HARDWARE_ID;")

resultmysql = cursormysql.fetchall()

# prepare a cursor object using cursor() method
cursormssql = skadb.cursor()

# Fetch all rows using cursor() method.
for row in resultmysql:
	 cursormssql.execute("INSERT INTO OCSINVENTORY_MYTRANSC01(TAG,NAME,USERID,OSNAME,MACADDR,HARDWARE_ID) VALUES(%s, %s, %s, %s, %s, %s)",(row))

# Commit MicrosoftSQL
skadb.commit()

# disconnect from server
ocsdb.close()
skadb.close()