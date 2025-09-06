# this file contains an external python api for nimmedPy
import nimporter
import nimmedPy 

def parse_classifier_output(classifier_output: list[tuple[int, float]]) -> tuple[int, float]:
    """
    Parses raw output of text or token classification models

    Args:
        classifier_output (list[tuple[int, float]]): List of tuples containing label id's and their respective values

    Returns:
        tuple[int, float]: id with highest value along with (highest value - lowest value) useful as a rough certainty score
    """   
    return nimmedPy.parse_labels(classifier_output)

def get_dir_docs(doc_dir_paths: list[str], include_links: bool) -> str:
    """
    gets files from list of directory paths, with the option of including textfiles with urls

    Args:
        doc_dir_paths (list[str]): directories to search
        include_links (bool): includes urls in "links.txt" if found in directory

    Returns:
        str: list of document paths and urls if link is included
    """    
    return nimmedPy.doc_sort(doc_dir_paths, include_links)

def clean_string(dirty_string: str) -> str:
    """
    Goes through entire string and removes unwanted symbols

    Args:
        dirty_string (str): string to clean

    Returns:
        str: cleaned string
    """
    return nimmedPy.clean_string(dirty_string)