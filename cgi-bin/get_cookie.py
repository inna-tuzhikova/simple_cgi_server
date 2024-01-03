#! /usr/bin/env python3

import os

print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<head>')
print('<title>Get Cookie</title>')
print('</head>')
print('<body>')

if 'HTTP_COOKIE' in os.environ:

    for cookie in os.environ['HTTP_COOKIE'].split(';'):
        k, v = cookie.split('=')
        print(f'{k}: {v}<br/>')

print('</body>')
print('</html>')
