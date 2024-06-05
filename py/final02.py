#!/usr/bin/python
print('Content-type: text/html\n')


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

if __name__ == "__main__":
  while True:
    print("YOU HAVE ENTERTED THE DUNGEON!")
    print("What is your name travler?: ")
    name = input()
    print("Hello, " + name + " will you take on this quest to save your life?")
    anwser = input()
    if (anwser.lower() == 'yes'):
       print ("Great, now scram!")
    else:
        print("Wrong anwser, GO")
    start()

data = cgi.FieldStorage()
name = 'Goober'
if ('name' in data):
    name = data['name'].value
bgcolor = 'Blue'
if ('bgcolor' in data):
    bgcolor = data['bgcolor'].value
    
#def start():
    #movement = ['go left','go straight','go right','go back']


html= HTML_head
html+= '<body style="background-color: '
html+= bgcolor + ';">'
html+= '<h1>Hello ' + name + '</h1>'
html+= '<br><a href="hello.html">Try Again</a>'
html+= HTML_foot
print(html)



