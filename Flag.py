#!/usr/bin/env python 
# this is a Program simple in python language to translate a Flag you search to symbole in #terminal 

import Image


class Flag(object):
	
	#constractor
	def __init__(self,theName):
		self.name = theName
		self.ImageData = []
		self.size = 0
		self.width = 0 
		self.height = 0 
	

	#Get Data Image Function
	def getImage(self):
		im = Image.open("flags-normal/"+self.name+".png")
		img = im.convert("L")
		img.thumbnail((40,25))
		self.size = self.width , self.height = img.size
		print self.width , self.height
		for x in range(self.width) :
			for y in range(self.height):
				self.ImageData.append(img.getpixel((x,y)))
		del img
		

	# Convert Data Image Function
	def convertData(self):
		
		i = 0
		image = "   "
		for item in self.ImageData:
			if i <= 24 :
				if item > 0 and item <= 10 :
					image = image + "a"
				if item > 10 and item <= 20 :
					image = image + "b"
				if item > 20 and item <= 30 :
					image = image + "c"
				if item > 30 and item <= 40 :
					image = image + "d"				
				if item > 40 and item <= 50 :
					image = image + "e"
				if item > 50 and item <= 60 :
					image = image + "f"
				if item > 60 and item <= 70 :
					image = image + "g"
				if item > 70 and item <= 80 :
					image = image + "h"
				if item > 80 and item <= 90 :
					image = image + "i"
				if item > 90 and item <= 100 :
					image = image + "j"
				if item > 100 and item <= 110 :
					image = image + "k"
				if item > 110 and item <= 120 :
					image = image + "l"
				if item > 120 and item <= 130 :
					image = image + "m"
				if item > 130 and item <= 140 :
					image = image + "n"
				if item > 140 and item <= 150 :
					image = image + "o"
				if item > 150 and item <= 160 :
					image = image + "p"
				if item > 160 and item <= 170 :
					image = image + "q"
				if item > 170 and item <= 180 :
					image = image + "r"
				if item > 180 and item <= 190 :
					image = image + "s"
				if item > 190 and item <= 200 :
					image = image + "t"
				if item > 200 and item <= 210 :
					image = image + "u"
				if item > 210 and item <= 220 :
					image = image + "w"
				if item > 220 and item <= 230 :
					image = image + "x"
				if item > 230 and item <= 240 :
					image = image + "y"
				if item > 240 and item <= 255 :
					image = image + "z"
			else :
				print image
				i = 0
				image = "   "
			i +=1
				
		


