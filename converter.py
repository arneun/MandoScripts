import re

file = open("input.txt","r")
html = file.read()
file.close()

html = html.replace("<i>","[i]")
html = html.replace("</i>","[/i]")

html = html.replace("<u>","[u]")
html = html.replace("</u>","[/u]")

html = html.replace("<span style='color:green'>","[color=#00BF00]")
html = html.replace("</span>","[/color]")

html = html.replace('<p align="right">',"")
html = html.replace('<p>',"")
html = html.replace('</p>',"")

re1 = re.compile('<img.+>')
image = re1.findall(str(html))

for img in image:
    html = html.replace(img,"")

re2 = re.compile('<.+Temat na forum</a>')
forum = re2.findall(str(html))

for form in forum:
    html = html.replace(form,"")

html = html.replace('http://www.mandayaim.com/',"")
html = html.replace("<a href='/","[url=http://www.mandayaim.com/")
html = html.replace("<a href='","[url=http://www.mandayaim.com/")

html = html.replace('<a href="/',"[url=http://www.mandayaim.com/")
html = html.replace("<a href='","[url=http://www.mandayaim.com/")

html = html.replace("'>","]")
html = html.replace('">',"]")

html = html.replace('<a href="',"[url=http://www.mandayaim.com/")
html = html.replace("'>","]")

html = html.replace("</a>","[/url]")

html = html.replace("czlonek-Sh`ehn","czlonek-Sh%60ehn")
html = html.replace("czlonek-Arakh Ha`an","czlonek-Arakh%20Ha%60an")
html = html.replace("czlonek-Serim`ika","czlonek-Serim%60ika")

html = html.replace("<br>","")
html = html.replace("</br>","")
html = html.replace("<br/>","")
result = str(html)

print(html)

