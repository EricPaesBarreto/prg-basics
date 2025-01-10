names = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

format = lambda list : [list[0].upper(), list[1]]

print(list(map(format, names)))