"""
Search google using firefox browser using cli
Run this script with few default options to achieve better results
Default options :
1. use 1 as arguments to open google.co.in
2. use 2 (space) string to search as arguments to google it

More variations to add soon 

"""

import sys
import webbrowser
var = sys.argv[1]
url = 'www.google.co.in'
if int(var) == 1 :
	webbrowser.get('firefox').open_new(url)	
elif int(var) == 2 :
	var = sys.argv[2:]
	var = ('+').join(var)
	url = 'www.google.co.in?q='+var
	webbrowser.get('firefox').open_new(url)


