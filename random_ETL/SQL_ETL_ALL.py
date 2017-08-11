#!/usr/bin/python

import os
import csv
import psycopg2
import string
import sys
import SQL_ETL_IP
import SQL_ETL_IP2


conn = psycopg2.connect(database="DATABASENAME", user="USERNAME", password="PASSWORD", host="IP", port="PORTNUM")
cur = conn.cursor()
conn.set_client_encoding('Latin1')
path = 'PATH TO DIRECTORY'
os.chdir(path)
files = [f for f in os.listdir('.') if os.path.isfile(f)]



print "\n"
print "==== SQL import start ===="
print "\n"

SQL_ETL_IP.import_IP(conn, files, cur)
print "\n"
print "IP complete\n"

#SQL_ETL_IP2.import_IP2(conn, files, cur)
print "\n"
print "IP2 complete\n"

conn.close()
print "\n"
print "==== Database connection closed ===="
print "\n"
#for f6 in files:
#    os.remove(f6)

