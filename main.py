from app.io.input import read_console, read_file_builtin, read_file_pandas
from app.io.output import write_console, write_file_builtin


def main():
    # Console
    console_text = read_console()
    write_console(f"Text from console: {console_text}")
    write_file_builtin('data/console_output.txt', console_text)

    # file
    file_content = read_file_builtin('data/input.txt')
    write_console(f"Text from file: {file_content}")
    write_file_builtin('data/builtin_output.txt', file_content)

    # file with pandas
    try:
        df = read_file_pandas('data/input.csv')
        spaces40()
        write_console(f"Data from .csv:\n{df.to_string()}")
        spaces40()
        write_file_builtin('data/pandas_output.txt', df.to_string())
    except FileNotFoundError:
        write_console("File input.csv not found!")


def spaces40():
    print('*'*40)

if __name__ == "__main__":
    main()


