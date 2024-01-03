#! /usr/bin/env python3
import cgi

form = cgi.FieldStorage()

subj = form.getvalue('subject', 'Not set')

print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<head>')
print('<title>Radio - Fourth CGI Program</title>')
print('</head>')
print('<body>')
print(f'<h2> Selected Subject is {subj}</h2>')
print('</body>')
print('</html>')