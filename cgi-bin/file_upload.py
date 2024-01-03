#! /usr/bin/env python3
import cgi
import os


form = cgi.FieldStorage()

file_item = form['filename']

if file_item.filename:
    file_name = os.path.basename(file_item.filename)
    with open(f'/tmp/{file_name}', 'wb') as f:
        f.write(file_item.file.read())
    msg = f'The file {file_name} was uploaded successfully'
else:
    msg = 'No file was uploaded'

print('Content-type: text/html\r\n\r\n')
print('<html>')
print('<body>')
print(f'<p>{msg}</p>')
print('</body>')
print('</html>')
