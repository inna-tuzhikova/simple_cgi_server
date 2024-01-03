#! /usr/bin/env python3
import cgi

form = cgi.FieldStorage()

subj = form.getvalue('dropdown', 'Not entered')

print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<head>')
print('<title>Dropdown - Sixth CGI Program</title>')
print('</head>')
print('<body>')
print(f'<h2> Selected Subject is {subj}</h2>')
print('</body>')
print('</html>')