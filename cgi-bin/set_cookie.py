#! /usr/bin/env python3

print('Set-Cookie:UserID=XYZ;')
print('Set-Cookie:Password=XYZ123;')
print('Set-Cookie:Expires=Tuesday, 31-Dec-2007 23:12:40 GMT;')
print('Set-Cookie:Domain=www.tutorialspoint.com;')
print('Set-Cookie:Path=/perl;')
print('Content-type:text/html\r\n')

print('<html>')
print('<head>')
print('<title>Cookies in CGI</title>')
print('</head>')
print('<body>')
print('Setting cookies')
print('<br/>')
print('</body>')
print('</html>')
