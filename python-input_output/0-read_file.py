#!/usr/bin/python3
"""
Bu modul mətn fayllarını oxumaq üçün funksiya təqdim edir.
"""


def read_file(filename=""):
    """
    UTF8 formatında olan mətn faylını oxuyur və çap edir.
    
    Args:
        filename (str): Oxunacaq faylın adı.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
