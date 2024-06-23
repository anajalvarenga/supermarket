from typing import List

def format_list(elements: List):
    return [element.as_dict() for element in elements]

def format_single(element):
    return element.as_dict()