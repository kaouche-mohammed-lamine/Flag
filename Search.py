#!/usr/bin/env python 
# this is a Program simple in python language to translate a Flag you search to symbole in #terminal 

from Flag import Flag



def menu():
	print "*********************** Welcome ***********************"
	print "\n"

def menu_reset():
	print "\n"
	print "*********************** ------- ***********************"
	print "\n"

def main():
	menu()
	i = 0
	while(i == 0):
		Name_country = raw_input("please write your Name Country : ")
		image1 = Flag(Name_country)
		image1.getImage()
		image1.convertData()
		menu_reset()
		
		

if __name__ == "__main__":
	main()
