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


