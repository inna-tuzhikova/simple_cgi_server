#! /usr/bin/env python3
import cgi


form = cgi.FieldStorage()

first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')

print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<head>')
print('<title>Hello - Second CGI Program</title>')
print('</head>')
print('<body>')
print(f'<h2>Hello {first_name} {last_name}</h2>')
print('</body>')
print('</html>')
