#!/usr/bin/python
import os
import csv
import psycopg2
import string
import sys

def import_IP2(conn, files, cur):
    storage_counter = 0
    net_cpu_counter = 0
    
    for f in files:
        if f.startswith("GeoLiteCity-Blocks.csv"):
            with open (f, 'rb') as f1:
                reader = csv.reader(f1, delimiter = ',')
    
                for row in reader:
                    col_count = len(row)
                    #print row
                    if col_count == 3:
                        #print row
                        startIpNum = row[0]
                        endIpNum = row [1]
                        locId = row[2]
                        storage_insert="INSERT INTO geolitecity_blocks (startIpNum,endIpNum,locId) VALUES ('%s', '%s', '%s');" % (startIpNum,endIpNum,locId)
                        cur.execute(storage_insert)
                        #print storage_insert
                        #print "server cpu insert finished"
                        
                        storage_counter+=1
                        sys.stdout.write("\r" + "\x1b7\x1b[%d;%df%s\x1b8" % (61, 0, "geolite city IP2 SQL insert finished on row " + str(storage_counter)))
                        sys.stdout.flush()
                        conn.commit()




