import cgi
import os
import http.cookies
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
if cookie.get("counter"):
    visitor_counter = cookie.get("counter").value
    visitor_counter = int(visitor_counter) + 1 if visitor_counter else 0
    print(f"Set-Cookie: counter={visitor_counter}")
else:
    visitor_counter = 1
    print(f"Set-Cookie: counter={visitor_counter}")


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
if type(c) is str:
    print("<p>{}</p>".format(c).__str__())
else:
    for elem in c:
        print("<p>{}</p>".format(elem))

print("Скільки разів було відкрито форму:", visitor_counter)
print("""</body>
        </html>""")

