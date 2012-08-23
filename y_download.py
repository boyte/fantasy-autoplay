#!/usr/bin/env python
# encoding: utf-8
"""
y_download.py

Created by Cody Boyte on 2012-08-21.
"""

import sys
import os
import requests
import json
import sqlite3 as lite
from urlparse import parse_qs
import time
from bs4 import BeautifulSoup
from oauth_hook.hook import OAuthHook

auth_file = 'client_secrets.json'

with open(auth_file, 'r') as f:
	a_vars = f.read()
	saved_vars = json.loads(a_vars)
	key = saved_vars['consumer_key']
	secret = saved_vars['consumer_secret']

def main(league,team):
	#collect data
	standings = yahoo_cycle('http://fantasysports.yahooapis.com/fantasy/v2/league/mlb.l.%d/standings'%league)
	roster = yahoo_cycle('http://fantasysports.yahooapis.com/fantasy/v2/team/mlb.l.%d.t.%d/roster'%(league,team))
	roster_stats = yahoo_cycle('http://fantasysports.yahooapis.com/fantasy/v2/team/mlb.l.%d.t.%d/stats'%(league,team))
	#save data to files
	to_file('standings.txt',standings)
	to_file('roster.txt',roster)
	to_file('roster_stats.txt',roster_stats)
	pass

#query yahoo for relevant data
def yahoo_cycle(url):
	token = saved_vars['token']
	secret = saved_vars['secret']
	oauth_hook = OAuthHook(token,secret,header_auth=True)
	#create session
	client = requests.session(hooks={'pre_request':oauth_hook})
	#get all teams from league
	y_data = client.get(url)
	print "hit yahoo"
	return y_data.content

#save each query to a file to be manipulated later
def to_file(file_name,input_data):
	try:
		with open(file_name,'a') as f:
			f.write(input_data)
	except:
		print "problem with file writing for:",file_name
		raise
	pass

# main authorization function
def auth_cycle(key,secret):
	try:
		yahoo_oauth_hook = OAuthHook(consumer_key = key ,consumer_secret = secret)
		#step 1 - get initial token and secret
		response = requests.post('https://api.login.yahoo.com/oauth/v2/get_request_token', hooks={'pre_request': yahoo_oauth_hook}, data={'oauth_callback': 'oob'})
		response = parse_qs(response.content)
		oauth_token = response['oauth_token'][0]
		oauth_secret = response['oauth_token_secret'][0]
		#special auth url from yahoo
		o_url = response['xoauth_request_auth_url'][0]

		#step 2, redirect the user
		print "Go to %s and sign in before returning the pin."%o_url
		oauth_verifier = raw_input('Please enter your PIN: ')

		#step 3, authenticate and get token secret
		new_oauth_hook = OAuthHook(oauth_token,oauth_secret,consumer_key = key ,consumer_secret = secret)
		response = requests.post('https://api.login.yahoo.com/oauth/v2/get_token', {'oauth_verifier': oauth_verifier},hooks={'pre_request':new_oauth_hook})
		response = parse_qs(response.content)
		saved_vars["token"] = response['oauth_token'][0]
		saved_vars["secret"] = response['oauth_token_secret'][0]
		saved_vars["time"] = time.time()
		j = json.dumps(saved_vars)
		with open(auth_file, 'w') as f:
			f.write(j + "\n")
		print"authed"
		pass
	except: 
		print "auth issue"
		raise

