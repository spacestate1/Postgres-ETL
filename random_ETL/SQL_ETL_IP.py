#!/usr/bin/python
import os
import csv
import psycopg2
import string
import sys

def import_IP(conn, files, cur):
    storage_counter = 0
    net_cpu_counter = 0
    
    for f in files:
        if f.startswith("GeoLiteCity-Location.csv"):
            with open (f, 'rb') as f1:
                reader = csv.reader(f1, delimiter = ',')
    
                for row in reader:
                    col_count = len(row)
                    #print row
                    if col_count == 9:
                        #print row
                        
                        locId = row[0]
                        country = row[1]
                        region = row[2]
                        city = row[3]
                        postalCode= row[4]
                        latitude= row[5]
                        longitude= row[6]
			metroCode= row[7]
                        areaCode= row[8]
                        storage_insert="INSERT INTO geolitecity_location (locId,country,region,city,postalCode,latitude,longitude,metroCode,areaCode) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (locId,country,region,city,postalCode,latitude,longitude,metroCode,areaCode)
                        cur.execute(storage_insert)
                        #print storage_insert
                        #print "server cpu insert finished"
                        
                        storage_counter+=1
                        sys.stdout.write("\r" + "\x1b7\x1b[%d;%df%s\x1b8" % (61, 0, "geolite city SQL insert finished on row " + str(storage_counter)))
                        sys.stdout.flush()
                        conn.commit()
                    if "hrStorageTable" in row and col_count != 12 and "hrStorageTable: No entries" not in row:
                        print col_count
                        print "============", row




