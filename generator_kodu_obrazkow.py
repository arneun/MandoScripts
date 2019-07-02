year = "2019"
convention = "pyrkon"
data = {
    "arneun" : [23, "Arneun"],
    "dhadral" : [39, "Dhadral"],
    "kiryl" : [39, "Kirył"],
    "mah" : [81, "Mahiyana"],
    "morrigan" : [4, "Morrigan"],
    "nea" : [5, "Aranea"],
    "ryba" : [7, "Ryba"],
    "shehn": [156, "Sh`ehn"],
    "trez" : [6, "T`rez"],
}
str = ""
for (link_name, arr) in data.items():
    for i in range (1,arr[0] + 1): 
        str += ("<a href='/mywakcji/{1}_{0}/{1}_{0}_{4}_{5}.jpg' rel='lightbox[{2}{0}]' title='{2} {0}'><img src='/mywakcji/{1}_{0}/{1}_{0}_{4}_{5}_t.jpg'></a> ".format(year, convention, convention.capitalize(), arr[1], link_name, i))
    str += "\n"

print(str)
