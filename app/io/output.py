def output_text(text):
    """
    Prints the given text to the console.

    Args:
        text (str): The text to print.
    """
    print(text)

def write_file_builtin(file_path, text):
    """
    Writes the given text to a file using built-in Python functionality.

    Args:
        file_path (str): The path to the file.
        text (str): The content to write.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)
