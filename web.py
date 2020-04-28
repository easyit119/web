#!C:\Users\user\AppData\Local\Programs\Python\Python38-32/python.exe

print("Content-Type: text/html")
print()
import cgi          #  cgi 표현식 구문. 밑의 html 구문에 대한 제어를 한다.
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId,'r').read()
else:
    pageId = 'Welcome'
    description = 'hello web'

# 실제 웹페이지에 보여질 부분.
print('''<!doctype html>    
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    <li><a href="index.py?id=HTML">HTML</a></li>
    <li><a href="index.py?id=CSS">CSS</a></li>
    <li><a href="index.py?id=JavaScript">JavaScript</a></li>
  </ol>
  <h2>{title}</h2>
  <p>{desc}</p>
  <p> 본문 텍스트
  </p>
</body>
</html>
'''.format(title=pageId, desc=description) )
# 끝에 보면, <h2> , <p> 의  {} 가 있다. 입력 받을 변수를 말하고,
# 맨 밑에 .format()로 내부 값을 넣어주는 방식이다.
