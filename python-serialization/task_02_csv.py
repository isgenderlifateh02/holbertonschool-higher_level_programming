#!/usr/bin/python3
"""
This module contains a function to convert a list of dictionaries
into a CSV file and vice versa.
"""
import csv


def write_data_to_csv(data, filename):
    """
    Writes a list of dictionaries to a CSV file.

    Args:
        data (list): A list of dictionaries.
        filename (str): The name of the CSV file.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        if not data or not isinstance(data, list):
            return False

        # Lüğətin açarlarını (key) sütun adları kimi götürürük
        fieldnames = data[0].keys()

        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()  # Sütun adlarını yazır
            writer.writerows(data)  # Bütün sətirləri yazır
        return True
    except Exception:
        return False
