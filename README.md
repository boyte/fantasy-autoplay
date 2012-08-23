fantasy-autoplay
================

This program is currently being developed as the interface between a predictive baseball
program and the Yahoo Fantasy Sports API. As I started my predictive analytics program I 
found that there wasn't an easy way to get the fantasy baseball data from my current league
into a format I could play with, without hitting the API repeatedly. 

The current functionality pulls down standings, roster and roster stats from Yahoo.

Currently Required Modules:
- requests (https://github.com/kennethreitz/requests)
- request-oauth (https://github.com/maraujop/requests-oauth)
- beautifulsoup (http://www.crummy.com/software/BeautifulSoup/)

INSTRUCTIONS
============

1) Fill out the client_secrets.json file with the client key and client secret provided by Yahoo

2) Run the program from the terminal. Follow the instructions.

3) The program results in three text files and a database with the data parsed into it. 



Next Steps
==========

Importing data into sqlite database for modifying later, setting ordering variables, etc.