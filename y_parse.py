#!/usr/bin/env python
# encoding: utf-8
"""
y_parse.py

Created by Cody Boyte on 2012-08-21.
"""

import sys
import os
from bs4 import BeautifulSoup as Soup

def main():
	roster = file_parse('roster.txt')
	standings = file_parse('standings.txt')
	print roster_parse(roster)
	print standings_parse(standings)
	
	pass

def standings_parse(standings):
	stands = list()
	soup = Soup(standings)
	try:
		for team in soup.findAll('team'):
			#set variables for each team
			t_key = team.team_key.string
			t_name = team.findAll('name')[0].string
			t_manager = team.nickname.string
			t_pos = team.rank.string
			t_wins = team.wins.string
			t_losses = team.losses.string
			t_ties = team.ties.string
			t_gb = team.games_back.string
			#create standings tuple
			data = (t_key,t_name,t_manager,t_pos,t_wins,t_losses,t_ties,t_gb)
			#append to standings list
			stands.append(data)
	except TypeError:
		print "standings type error"
		pass
	return stands
	
def roster_parse(roster):
	#players list to be returned
	players = list()
	soup = Soup(roster)
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
		print "roster type error"
		pass
	return players
		
def file_parse(file_name):
	with open(file_name,'r') as f:
		the_file = f.read()
	return the_file
		
		
if __name__ == '__main__':
	main()

