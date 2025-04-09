import pandas as pd


def input_text():
    """
    Reads text input from the console.

    Returns:
        str: The input text entered by the user.
    """
    return input("Введіть текст: ")


def read_file_builtin(file_path):
    """
    Reads the content of a file using built-in Python functionality.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The contents of the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def read_file_pandas(file_path):
    """
    Reads the content of a file using the pandas library.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The contents of the file as a string.
    """
    df = pd.read_csv(file_path, header=None)
    return df.to_string(index=False, header=False)
