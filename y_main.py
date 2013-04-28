#!/usr/bin/env python
# encoding: utf-8
"""
y_main.py

Created by Cody Boyte on 2012-08-22.
"""

import sys
import os
import y_download
import y_parse
import y_intodb

def main():
	league = int(raw_input("League Number: "))
	team = int(raw_input("Team Number: "))
	try:
		print "starting downloads"
		y_download.main(league,team)
		print "starting parsing"
		y_parse.main()
		print "pushing data into database"
		y_intodb.main()
	except:
		print "problems with program"
		raise
	print "done"
	pass

if __name__ == '__main__':
	main()

