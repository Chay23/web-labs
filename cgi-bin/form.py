import cgi
#!/usr/bin/env python3
import os
import http.cookies
count = 0
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")
if name:
    count = int(name.value) + 1
print("Content-type: text/html\n")
print("Set-cookie: name={}" .format(count))

print(count)
form = cgi.FieldStorage()
text1 = form.getfirst("name", "Не задано")
text2 = form.getfirst("surname", "Не задано")

age = form.getvalue('age','Не задано')

c = form.getvalue("option")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>form.py</title>
        </head>
        <body>""")

print("<h1>Result</h1>")
print("<p>Name: {}</p>".format(text1))
print("<p>Surname: {}</p>".format(text2))
print("<p>Age: {}</p>".format(age))
# print("<p>Age: {}</p>".format(c))
print("<p>CheckBox res:</p>")
for elem in c:
    print("<p>{}</p>".format(elem))

print("Скільки разів було відкрито форму: 11")
print("""</body>
        </html>""")

