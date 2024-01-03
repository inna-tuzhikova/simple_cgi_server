#! /usr/bin/env python3
import os

print('Content-type: text/html\r\n\r\n')
print('<font size=+10>Environment</font><br>')

for k, v in os.environ.items():
    print(f'<b>{k}</b>: {v}<br>')
