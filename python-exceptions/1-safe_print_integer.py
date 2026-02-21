#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # 1. ADDIM: Sınama
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # 2. ADDIM: Xətanı tutma
        return False
