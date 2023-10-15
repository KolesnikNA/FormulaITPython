# TODO Найдите количество книг, которое можно разместить на дискете

disk_memory_mb = 1.44
pages = 100
lines_on_page = 50
chars_on_page = 25
kb_in_mb = 1024
byte_in_kb = 1024
bytes_in_char = 4

bytes_in_disk = disk_memory_mb * kb_in_mb * byte_in_kb
bytes_in_book = pages * lines_on_page * chars_on_page * bytes_in_char


result = bytes_in_disk // bytes_in_book
print("Количество книг, помещающихся на дискету:", int(result))
