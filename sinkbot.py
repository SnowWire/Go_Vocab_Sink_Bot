# coding=utf-8
from splinter import Browser
import time
with Browser() as browser:
    url = "https://govocab.com/sink"
# Put your user and pass here
    user = "user"
    passw = "pass"
    browser.visit(url)
    print("signing in")
    browser.find_by_id('user_session_login').fill(user)
    browser.find_by_id('user_session_password').fill(passw)
    button = browser.find_by_value('Sign In')
    button.click()
    time.sleep(2)
# now this is where it gets bad.....
    while True :
		try:
			element = browser.find_by_css('h2').first
			print(element.value)
			ask = element.value.encode('utf-8')
			print(ask)
			if ask == 'die Aktentasche' :
				button = browser.find_by_text('briefcase')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'briefcase' :
				button = browser.find_by_text('die Aktentasche')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'die Brieftasche' :
				button = browser.find_by_text('wallet')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'wallet' :
				button = browser.find_by_text('die Brieftasche')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'die Einkaufstasche' :
				button = browser.find_by_text('shopping bag')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'shopping bag' :
				button = browser.find_by_text('die Einkaufstasche')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'das Gepäck' :
				button = browser.find_by_text("luggage, baggage")
				button.click()
				print("done")
				points =+ 2
			elif ask == 'luggage':
				button = browser.find_by_text("das Gepäck")
				button.click()
				print("done")
				points =+ 2
			elif ask == 'das Gepäckausgabeband':
				button = browser.find_by_text('baggage carousel')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'baggage carousel' :
				button = browser.find_by_text('das Gepäckausgabeband')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'die Handtasche' :
				button = browser.find_by_text('purse')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'purse' :
				button = browser.find_by_text('die Handtasche')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'der Koffer' :
				button = browser.find_by_text('suitcase')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'suitcase' :
				button = browser.find_by_text('der Koffer')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'das Paket' :
				button = browser.find_by_text('package')
				button.click()
				print("done")
			elif ask == 'package' :
				button = browser.find_by_text('das Paket')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'der Rucksack' :
				button = browser.find_by_text('backpack')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'backpack' :
				button = browser.find_by_text('der Rucksack')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'die Schultasche' :
				button = browser.find_by_text('school bag')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'school bag' :
				button = browser.find_by_text('die Schultasche')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'die Tasche' :
				button = browser.find_by_text('bag')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'bag' :
				button = browser.find_by_text('die Tasche')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'leicht' :
				button = browser.find_by_text('lightweight')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'lightweight' :
				button = browser.find_by_text('leicht')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'schwer' :
				button = browser.find_by_text('heavy')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'heavy' :
				button = browser.find_by_text('schwer')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'rollen' :
				button = browser.find_by_text('to roll')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'to roll' :
				button = browser.find_by_text('rollen')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'tragen' :
				button = browser.find_by_text('to carry')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'Was trägst du?' :
				button = browser.find_by_text('What are you carrying?')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'What are you carrying?' :
				button = browser.find_by_text('Was trägst du?')
				button.click()
				print("done")
				points =+ 2
			elif ask == 'Ich trage…' :
				button = browser.find_by_text("I'm carrying…")
				button.click()
				print("done")
				points =+ 2
			elif ask == "I'm carrying…" :
				button = browser.find_by_text('Ich trage…')
				button.click()
				print("done")
				points =+ 2
			elif ask == "durch" :
				button = browser.find_by_text('through')
				button.click()
				print("done")
				points =+ 2
			elif ask == "through" :
				button = browser.find_by_text('durch')
				button.click()
				print("done")
				points =+ 2
			elif ask == "ohne" :
				button = browser.find_by_text('without')
				button.click()
				print("done")
				points =+ 2
			elif ask == "without" :
				button = browser.find_by_text('ohne')
				button.click()
				print("done")
				points =+ 2
			elif ask == "gegen" :
				button = browser.find_by_text('against (around with time)')
				button.click()
				print("done")
				points =+ 2
			elif ask == "against (around with time)" :
				button = browser.find_by_text('gegen')
				button.click()
				print("done")
				points =+ 2
			elif ask == "um" :
				button = browser.find_by_text('around (at with time)')
				button.click()
				print("done")
				points =+ 2
			elif ask == "around (at with time)" :
				button = browser.find_by_text('um')
				button.click()
				print("done")
				points =+ 2
			elif ask == "aus" :
				button = browser.find_by_text('from')
				button.click()
				print("done")
				points =+ 2
				points =+ 2
			elif ask == "out of" :
				button = browser.find_by_text('aus')
				button.click()
				print("done")
				points =+ 2
			elif ask == "from" :
				button = browser.find_by_text('aus')
				button.click()
				print("done")
				points =+ 2
			elif ask == "ausser" :
				button = browser.find_by_text('besides')
				button.click()
				print("done")
				points =+ 2
			elif ask == "besides" :
				button = browser.find_by_text('ausser')
				button.click()
				print("done")
				points =+ 2
			elif ask == "bei" :
				button = browser.find_by_text('at')
				button.click()
				print("done")
				points =+ 2
			elif ask == "at" :
				button = browser.find_by_text('bei')
				button.click()
				print("done")
				points =+ 2
			elif ask == "mit" :
				button = browser.find_by_text('with')
				button.click()
				print("done")
				points =+ 2
			elif ask == "with" :
				button = browser.find_by_text('mit')
				button.click()
				print("done")
				points =+ 2
			elif ask == "seit" :
				button = browser.find_by_text('since when')
				button.click()
				print("done")
				points =+ 2
			elif ask == "von" :
				button = browser.find_by_text('from')
				button.click()
				print("done")
				points =+ 2
			elif ask == "from" :
				button = browser.find_by_text('von')
				button.click()
				print("done")
				points =+ 2
			elif ask == "zu" :
				button = browser.find_by_text('to')
				button.click()
				print("done")
				points =+ 2
			elif ask == "to" :
				button = browser.find_by_text('zu')
				button.click()
				print("done")
				points =+ 2
			elif ask == "seit" :
				button = browser.find_by_text('since when')
				button.click()
				print("done")
				points =+ 2
			elif ask == "gegenüber (von)" :
				button = browser.find_by_text('across (from)')
				button.click()
				print("done")
				points =+ 2
			elif ask == "across (from)" :
				button = browser.find_by_text('gegenüber (von)')
				button.click()
				print("done")
				points =+ 2
			else:
				element = browser.find_by_css('h2').first
				print(element.value)
				test = browser.find_by_xpath('/html/body/div[1]/div[3]/div[4]/div[1]/div[2]/div[1]/a[2]').first.click()
		except:
			pass