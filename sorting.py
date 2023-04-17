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

def selection_sort(num_array): #najde vzdy nejmensi, ve zbytku hleda zase nejmensi, da na zacatek atd
    #jak najde to potencialne nejmensi, posouva se minimum doprava a se sousedem se porovnava kdo je vetsi
    #z netu
    """
    for i in range(len(output)):
        minimum = i
        for j in range(i+1, len(output)):
            if output[minimum] > output[j]:
                minimum = j
    output[i], output[minimum] = output[minimum], output[i]
    """
    for i in range(len(num_array)): #narocnost: nkrat
        maybe_min = i #nkrat
        for j in range(i+1, len(num_array)):
            if num_array[maybe_min] > num_array[j]:
                maybe_min = j #3*[(n-1)+(n-2)...] --> 3*[k*(k+1)/2]
        num_array[i], num_array[maybe_min] = num_array[maybe_min], num_array[i] #nkrat
        # vystup +1
        #celkove 3n + 1 + 3*[(n-1)*n/2] = 3n + 1 + 3/2*(n^2 - n) = nejvyssi n^2 --> O(n^2) i nejlepsi i nejhorsi pripad je n^2

        return num_array

def main():
    data = read_data('numbers.csv')
    print(data['series_2'])
    print(selection_sort(data['series_2']))

if __name__ == '__main__':
    main()
