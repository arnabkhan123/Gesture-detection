import webbrowser
#webbrowser.open('http://google.co.kr', new=2)
def fun():
    
    url = 'http://www.python.org/'

# Open URL in a new tab, if a browser window is already open.
    webbrowser.open_new_tab(url + 'doc/')

# Open URL in new window, raising the window if possible.
    webbrowser.open_new(url)
