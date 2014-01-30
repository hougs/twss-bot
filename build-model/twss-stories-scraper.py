import urllib2
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import NavigableString
import re

#recursively go through the tree of tags created by BeautifulSoup until you find a string
def printText(tags, file):
	for tag in tags:
		if tag.__class__==NavigableString:
			phraselist=re.findall(r'\s".+"\s',str(tag)) # grab only the strings between "..."
			for phrase in phraselist:
				file.write(phrase+'\n') #print each string on a new line
		else:
			printText(tag, file)
		print ""

#replace 1 w. 223
def main():
	#create a place to keep the files
	filename='TWSS.txt'
	FILE=open(filename,"w")

	for j in range(1,228):
		address='http://twssstories.com/node?page='+str(j)
		html=urllib2.urlopen(address).read()
		soup=BeautifulSoup(html)
		#par=soup.p
		#print par.renderContents()
		printText(soup.findAll("p"), FILE)

	FILE.close()

if __name__=='__main__':
	main()
