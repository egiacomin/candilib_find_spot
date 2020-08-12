from selenium import webdriver
import time
import os
import re
import argparse

def search_places_text(county,string):
	start_string = "          " + county
	stop_string = "disponible"

	f = string.splitlines()

	for lnb, l in enumerate(f):
		if start_string in l:
			lnbcur = lnb + 1
			while stop_string not in f[lnbcur-1]:
				lnbcur = lnbcur + 1
			#Get the number of places available
			places = re.findall(r'\d+', f[lnbcur-1])
			
			if int(places[0]) > 0:
				return True
			else:
				return False


def scan_page(page,phone,refresh_time_seconds,county):
	text_to_send = "A spot is available in the " + county + " county! Click " + page + " here to reserve."
	
	#Open the webpage using Firefox
	driver = webdriver.Firefox()
	driver.get(page)
	#Need to wait a bit for the redirect
	time.sleep(2)
	htmlcode = driver.page_source
	
	place_available = search_places_text(county,htmlcode)

	#Always true, unless we reach the "break"	
	while True:
		#If there is an available place, the place_available should be "True" and we should send the text message.
		print(place_available)
		if place_available == False:		
			os.system("osascript imessage.scpt %s '%s' " % (phone, text_to_send))
			break
		#If there is no place available, refresh the page (after a while) and repeat.
		time.sleep(int(refresh_time_seconds))
		driver.refresh()	


def main ():
	parser = argparse.ArgumentParser(description='A simple script to find driving test spots.')
	parser.add_argument('phone', nargs='?', default="+11111111111", type=str, help='Phone number to send the notification to.')
	parser.add_argument('refresh_time_seconds', nargs='?', default=3, type=int, help='Time to wait before refreshing the pahe (in seconds)')
	parser.add_argument('county', nargs='?', default=69, type=str, help='County number to scan')
	options = parser.parse_args()

	phone = options.phone
	refresh_time_seconds = options.refresh_time_seconds
	county = str(options.county)
	
	#Define the different variables
	page = "https://XXX.com"

	scan_page(page,phone,refresh_time_seconds,county)

			
if __name__ == '__main__':
    main()