# TODO Найдите количество книг, которое можно разместить на дискете
space = 1.44
spaceb = space*1024**2
pages = 100
line_ = 50
sim = 25
book = pages*line_*sim*4
print("Количество книг, помещающихся на дискету:", int(spaceb//book))
