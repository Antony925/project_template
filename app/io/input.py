def read_console():
    """
    Reads text from console.

    Returns:
        str: user's input text
    """
    return input("Input text: ")


def read_file_builtin(filename):
    """
    Reads text from file

    Args:
        filename (str): path to file

    Returns:
        str: file content
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def read_file_pandas(filename):
    """
    Reads file's data using pandas.

    Args:
        filename (str): path to file

    Returns:
        pandas.DataFrame: File's data as pandas's DataFrame
    """
    import pandas as pd
    return pd.read_csv(filename)