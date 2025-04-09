from app.io.input import input_text, read_file_builtin, read_file_pandas
from app.io.output import output_text, write_file_builtin


def main():
    input_result = input_text()
    file_result_builtin = read_file_builtin('data/input.txt')
    file_result_pandas = read_file_pandas('data/input.csv')

    output_text(input_result)
    output_text(file_result_builtin)
    output_text(file_result_pandas)

    write_file_builtin('data/output.txt', input_result + '\n' + file_result_builtin + '\n' + file_result_pandas)

if __name__ == "__main__":
    main()
