def write_console(text):
    """
    Outputs text to the console.

    Args:
        text (str): Text for output
    """
    print(text)


def write_file_builtin(filename, text):
    """
    Outputs text to the file.

    Args:
        filename (str): path to file
        text (str): Text for output
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)