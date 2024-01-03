#! /usr/bin/env python3
import cgi


form = cgi.FieldStorage()

maths = form.getvalue('maths')
physics = form.getvalue('physics')

print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<head>')
print('<title>Checkbox - Third CGI Program</title>')
print('</head>')
print('<body>')

if maths:
    print('Maths Flag: ON')
else:
    print('Maths Flag: OFF')

print('<br>')

if physics:
    print('Physics Flag: ON')
else:
    print('Physics Flag: OFF')

print('</body>')
print('</html>')
