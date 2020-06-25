from selenium import webdriver
import time
import urllib
import os
import re

def main ():
	#Define the different variables
	page = "https://beta.interieur.gouv.fr/candilib/candidat/93/selection/selection-centre"
	refresh_rate_seconds = 1000
	tel = +1XXXXXXXX
	text_to_send = "A spot is available in the Rhone-Aleps (69) county!"
	
	#Open the webpage using Firefox
	driver = webdriver.Firefox()
	driver.get(page)
	htmlcode = driver.page_source
	#We search in the "69" county, if there is at least 1 available spot (1 to 99)
	x = re.findall('69 ('+'([1-9]|[1-8][0-9]|9[0-9])' + 'places disponibles', htmlcode)
			
	#Always true, unless we reach the "break"
	while True: #Always true, unless we reach the "break"
		#If there is an available place, the x string should not be empty send the text message and exit the program
		if not x:			
			os.system("osascript imessage.scpt %s '%s' " % (tel, text_to_send))
			break
		#If there is no place available, refresh the page (after a while) and repeat.
		time.sleep(int(refresh_rate_seconds))
		driver.refresh()
			
main ()