#!/usr/bin/env python
# encoding: utf-8
"""
y_intodb.py

Created by Cody Boyte on 2012-08-22.
"""

import sys
import os
import sqlite3 as lite

database = 'y_baseball.db'

def main():
	create_database()
	pass

def create_databases():
	con = lite.connect(database)
	with con:
		cur = con.cursor()
		#create the databases
		cur.execute('CREATE IF NOT EXISTS my_roster("ID","Player","Position","Starting")')
		cur.execute('CREATE IF NOT EXISTS standings("Key","Team","Manager","Standing","Wins","Losses","Ties","Games Back")')
		con.commit()	
	
if __name__ == '__main__':
	main()

