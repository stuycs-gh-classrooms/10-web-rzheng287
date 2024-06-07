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
<title>Dungeon Demise</title>
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
def gen_rad(x):
    radio = ''
    for e,i in x:
        radio += f'<input type="radio" name="path" value="{e}"> {i}<br>'
    return radio

def path_gen(path=None):
    possiblePaths = {
            'Begin': {
                'description': 'You wake up in a dark room. As your eyes slowly acustom to the dark, you notice 3 paths. Which one will you go towards?',
                'options': [
                    ('left', 'Go left'),
                    ('straight', 'Go straight'),
                    ('right', 'Go right')
                ]
            },
            'left': {
                'description': 'You decide to walk on the left path, suddenly a giant boulder breaks lose and starts rolling towards you! What will you do?',
                'options': [
                    ('Run', 'Run for it'),
                    ('Wall', 'Press yourself against the wall'),
                    ('Back', 'Run back to the start')]
                
            },
            'straight': {
                'description': 'You decide to walk on the straight path, you walk and walk until you see giant trees looming over you. What will you do?',
                'options': [
                    ('In', 'Walk into the forest'),
                    ('Around', 'Walk around its perimeter'),
                    ('Tree', 'Climb a tree')]
            },
            'right': {
                'description': 'You decide to walk on the right path. As you walk you hear many sounds coming from a small opening. What will you do?',
                'options': [
                    ('Walk', 'Keep walking'),
                    ('Hole', 'Explore the hole'),
                    ('Yell', 'Yell Back')]
           },
            'Run': {
                'description': 'You decide to try and out run the rolling boulder. However it is much faster than you and crushes you.',
                'options': [('Begin', 'Restart')
                    
                    ]
           },
            'Wall': {
                'description': 'You decide to press yourself along the wall and just manage to dodge the rolling boulder. You then run to the end and exit the dungeon. ',
                'options': [('Begin', 'Restart')
                    ]
           },
            'Back': {
                'description': 'You decide to run back to the dark room before the boulder reaches you. ',
                'options': [('Begin', 'Restart')
                    ]
           },
        
            'In': {
                'description': 'You decide to walk into the forest when suddenly, a large monster appears. You try to run but it grabs you and eats you.',
                'options': [('Begin', 'Restart')
                    ]
            },
            
            'Around': {
                'description': 'You decide to walk around the trees and discover a ladder to the exit. You excape the dungeon. ',
                'options': [('Begin', 'Restart')
                    ]
            },
            
            'Tree': {
                'description': 'You decide to climb one of the largre trees, but a sudden gust of wind knocks you down and you die. ',
                'options': [('Begin', 'Restart')
                    ]
           },
            'Walk': {
                'description': 'You decide to ignore the sounds coming out of the hole, and find an exit at the very end. You escape the dungeon. ',
                'options': [('Begin', 'Restart')
                    ]
           },
            'Hole': {
                'description': 'You decide to crawl into the hole and explore. However, venomous snakes bite at your head and you die.',
                'options': [('Begin', 'Restart')
                    ]
           },
            'Yell': {
                'description': 'You decide to yell into the hole. However, you are met with a deep growl. Scared out of your mind you run and find an exit. You escape the dungeon.',
                'options': [('Begin', 'Restart')
                    ]
           }
           
           }
    

    if path and path in possiblePaths:
        current = path
    else:
        current = 'Begin'
    return current, possiblePaths[current]['description'], possiblePaths[current]['options']
   



form = cgi.FieldStorage()
path = form.getvalue('path')
Now, description, paths = path_gen(path)

html=HTML_head
html += f'<body>'
html += f'<h1> Dungeon Demise</h1>'
html += f'<p>{description}</p>'
html += f'''<form method="post" action="final02.py">
<input type="hidden" name="Now" value="{Now}">
'''
html+= gen_rad(paths)
html += '<input type="submit" value="Submit">'
html += '</form>'
html += HTML_foot
print(html)

path_gen()



