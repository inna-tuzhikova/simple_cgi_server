#! /usr/bin/env python3
import cgi

form = cgi.FieldStorage()

text = form.getvalue('text', 'Not entered')

print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<head>')
print('<title>Text area - Fifth CGI Program</title>')
print('</head>')
print('<body>')
print(f'<h2>Entered text is {text}</h2>')
print('</body>')
print('</html>')