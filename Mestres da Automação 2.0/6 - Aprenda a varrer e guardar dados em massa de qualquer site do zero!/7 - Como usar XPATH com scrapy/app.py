# XPATH
# //tag[@atributo='valor']

# Filho do filho - 1 só filho
# //div//fieldset/h4

# Filho do filho com mais xpath
# //div[@id='select-class-example']//fieldset/h4

# Filho do filho - mais de 1 filho
# //div[@id='select-class-example']//fieldset/h4

# Achar o texto dentro de um atributo
# //span[@class='text']/text()

# Extrair itemtype (texto dentro)
# //div[@class='quote']/@itemtype

# Extrair texto dentro do href
# //li[@class='next']//a/@href