# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44
quantity_pages = 100
quantity_lines = 50
quantity_symbols = 25
volume_symbols = 4

volume *= 1048576


quantity_symbols_in_book = quantity_pages * quantity_lines * quantity_symbols

quantity_books = volume / (quantity_symbols_in_book * volume_symbols)

print("Количество книг, помещающихся на дискету:", int(quantity_books))
