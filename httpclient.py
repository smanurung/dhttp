import urllib

login_data = urllib.urlencode({'email':'sonnyportnoy@yahoo.com','pass':'sonnytheot','login':'Masuk'})
op = urllib.urlopen('https://www.facebook.com/login.php?next=http%3A%2F%2Fwww.facebook.com%2Fhome.php',login_data)