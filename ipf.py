import requests as rq
from bs4 import BeautifulSoup as bs
import lxml
import sys
ags = sys.argv
agsc = len(ags)

link = ""

def main():
	
	s = rq.get("https://tools.keycdn.com/geo?host=" + link).text
	so = bs(s, "lxml")
	art = so.findAll("dd", class_="col-8 text-monospace")
	art2 = so.findAll("dt", class_="col-4")

	for i in range(len(art)):
		print(art2[i].text, (15 - len(art2[i].text)) * ' ', art[i].text)



if "--help" in ags or "-help" in ags:
	print("ddmoIPF:")
	print("    Uses:")
	print("        (ddmoWIMG google.com) - show infomation about google.com")
	print("        (ddmoWIMG 74.125.21.138) - show infomation about the ip address")
	pass
elif agsc == 1:
	link = ""
	main()
else:
	link = ags[1]
	main()
