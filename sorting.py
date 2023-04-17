import os


def read_data(file_name):
    """
     Reads csv file and returns numeric data.

     :param file_name: (str), name of CSV file
     :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
     """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open("numbers.csv", mode="r") as f:
        reader = csv.reader(f)  # v row jsou nazvy klicu
        for row_num, row in enumerate(
                reader):  # potoze chceme ke kazde promenne ziskat indexy a prvni radek budeme brat jako klic
            if row_num == 0:  # pro prvni radek
                output = dict()
                keys = row
                for key in row:
                    output[key] = []  # poprve se ulozi series1, pak series2, hodnota [] vytvori prazdny seznam
            else:
                for key_num, key in enumerate(keys):  # druha moznost zip key a row
                    output[key].append(int(row[key_num]))

    return output

def main():
    pass


if __name__ == '__main__':
    main()
