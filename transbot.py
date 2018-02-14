# -*- coding: utf-8 -*-
from googletrans import Translator
from splinter import Browser
import time
from collections import OrderedDict


# Put your user and pass here
user = ""
passw = ""




def string(string1,string2,string3,string4):
#	string1 = "test"
#	string2 = "testing"
#	string3 = "tted"
	string1 = string1.encode("utf-8")
	string2 = string2.encode("utf-8")
	string3 = string3.encode("utf-8")
	lengs = []
	counts = []
	count1 = 0
	count2 = 0
	count3 = 0
	s2 = 0
	s3 = 0
	s4 = 0
	winner = []
	lengs.append(len(string1) - len(string2))
	for i in range(min(len(string1), len(string2))):
		if string1[i] == string2[i]:
			count1 = count1 + 1

	lengs.append(len(string1) - len(string3))
	for i in range(min(len(string1), len(string3))):
		if string1[i] == string3[i]:
			count2 = count2 + 1

	lengs.append(len(string1) - len(string4))
	for i in range(min(len(string1), len(string4))):
		if string1[i] == string4[i]:
			count3 = count3 + 1
	counts.append(count1)
	counts.append(count2)
	counts.append(count3)
	mins = min(lengs, key=abs)
	if lengs[0] == mins:
		s2 += 1
	if lengs[1] == mins:
		s3 += 1
	if lengs[2] == mins:
		s4 += 1
	max1 = max(counts, key=abs)
	if counts[0] == max1:
		s2 += 1
	if counts[1] == max1:
		s3 += 1
	if counts[2] == max1:
		s4 += 1
	winner.append(s2)
	winner.append(s3)
	winner.append(s4)
	max2 = max(winner)
	OrderedDict((x, True) for x in winner).keys()
	if winner[0] == max2:
		win = string2
	elif winner[1] == max2:
		win = string3
	elif winner[2] == max2:
		win = string4
	return win
with Browser() as browser:
    url = "https://govocab.com/sink"
    browser.visit(url)
    print("signing in")
    browser.find_by_id('user_session_login').fill(user)
    browser.find_by_id('user_session_password').fill(passw)
    button = browser.find_by_value('Sign In')
    button.click()
    time.sleep(2)
	
	


    while True :
		try:
			match = None
			string1 = None
			string2 = None
			string3 = None
			translated = None
			string1 = browser.find_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[1]').text
			if string1 == "":
				score = browser.find_by_xpath('/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[2]/h1').text
				print(score)
				print("Game Over, Reloading!")
				browser.visit(url)
			else :
				element = browser.find_by_css('h2').first
				translator = Translator()
				translated = translator.translate(element.value)
				print("Translated " + translated.text.encode("utf-8"))
				string1 = browser.find_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[1]').text
				print(string1.encode("utf-8"))
				string2 = browser.find_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[2]').text
				print(string2.encode("utf-8"))
				string3 = browser.find_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[3]').text
				print(string3.encode("utf-8"))
				print("next")
				match = string(translated.text, string1, string2, string3)
				print(match)
				browser.find_by_text(match).first.click()
				print("done")
		except:
			pass
