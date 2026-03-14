#!/usr/bin/python3
"""
This module provides functions for XML serialization and deserialization.
It allows converting a Python dictionary into an XML file and back.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to an XML file.

    The function creates a root element named 'data' and adds each
    dictionary key-value pair as a sub-element.

    Args:
        dictionary (dict): The dictionary containing data to serialize.
        filename (str): The name of the output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file back into a Python dictionary.

    The function parses the XML file, iterates through the children
    of the root element, and reconstructs the dictionary.

    Args:
        filename (str): The name of the XML file to read.

    Returns:
        dict: A dictionary representation of the XML data, or None if error.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        return {child.tag: child.text for child in root}
    except Exception:
        return None
