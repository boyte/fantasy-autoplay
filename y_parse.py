#!/usr/bin/env python
# encoding: utf-8
"""
y_parse.py

Created by Cody Boyte on 2012-08-21.
"""

import sys
import os
from bs4 import BeautifulSoup

def main():
	roster = file_parse('roster.txt')
	print roster_parse(roster)
	pass

def roster_parse(roster):
	#players list to be returned
	players = list()
	print roster
	soup = BeautifulSoup(roster)
	try:
		for player in soup.findAll('player'):
			#set variables for each player
			p_key = player.player_key.string
			p_name = player.full.string
			p_pos = player.selected_position.position.string
			#create player tuple
			data = (p_key,p_name,p_pos)
			#append player to list of players
			players.append(data)
	except TypeError:
		pass
	return players
		
def file_parse(file_name):
	with open(file_name,'r') as f:
		the_file = f.read()
	return the_file
		
		
if __name__ == '__main__':
	main()

