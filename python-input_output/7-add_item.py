#!/usr/bin/python3
"""
Adds all arguments to a Python list, and then save them to a file.
"""
import sys
import os


# Əvvəlki tapşırıqlardan funksiyaları import edirik
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# 1. Fayl mövcuddursa, daxilini oxuyuruq, yoxdursa boş siyahı yaradırıq
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# 2. Command line arqumentlərini (skriptin adından başqa) siyahıya əlavə edirik
# sys.argv[0] skriptin öz adıdır, ona görə [1:] istifadə edirik
items.extend(sys.argv[1:])

# 3. Yenilənmiş siyahını fayla yazırıq
save_to_json_file(items, filename)
