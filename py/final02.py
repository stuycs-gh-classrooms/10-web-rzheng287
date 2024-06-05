#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb 
cgitb.enable()

import cgi

HTML_head = """
<!DOCTYPE html>
<html lang="en">


<head>
<link href="final02.css" rel="stylesheet">
<meta charset="utf-8">
<title>Hello</title>
</head>
"""

HTML_link = '''
<a href="temp_url">temp_text</a>'''
    

HTML_foot = """
</body>
</html>
"""

HTML_list ='''
<li>temp_list</li>
'''

def add_link(s,url,text):
    new = ''
    link = s.replace('temp_url',url)
    add_text = link.replace('temp_text',text)
    new += add_text
    return new



data = cgi.FieldStorage()
name = 'Goober'
if ('name' in data):
    name = data['name'].value
bgcolor = 'Blue'
if ('bgcolor' in data):
    bgcolor = data['bgcolor'].value
    



html= HTML_head
html+= '<body style="background-color: '
html+= bgcolor + ';">'
html+= '<h1>Hello ' + name + '</h1>'
html+= '<br><a href="index.html">Change your name?</a>'
html+= HTML_foot
print(html)



