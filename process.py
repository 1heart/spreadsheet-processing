#!/usr/bin/python

import sys
import os
import csv


alphabet = 'abcdefghijklmnopqrstuvwxyz'

def get_indices_from_cell(cell):
    assert type(cell) == str and len(cell) == 2
    cell = cell.lower()
    row_idx = alphabet.find(cell[0])
    col_idx = int(cell[1]) - 1
    return row_idx, col_idx

if __name__ == '__main__':
    filename = sys.argv[1]

    print('Opening {}'.format(filename))
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    colnames_start = raw_input('Which cell do column names start? (e.g. C3)\n')
    row_idx, col_idx = get_indices_from_cell(colnames_start)
    print('Assuming column names start at {}'.format(colnames_start))
    col_names = [x for x in data[row_idx][col_idx:] if x != '']
    print('Column names: {}'.format(col_names))

    rowname_start = raw_input('Which cell do row names start? (e.g. B4)\n')
    row_idx, col_idx = get_indices_from_cell(rowname_start)
    print('Assuming row names start at {}'.format(rowname_start))
    row_names = [row[row_idx] for row in data[col_idx:] if row[row_idx] != '']
    print('Row names: {}'.format(row_names))

    yn = raw_input('Do these column and row names look good? [yes/no]\n')
    if 'n' in yn:
        print('Exiting.')
        sys.exit()

    example_rowfirst = [row_names[0] + col_name for col_name in col_names]
    example_colfirst = [col_names[0] + row_name for row_name in row_names]
    while True:
        user_input = raw_input('Loop over rows first (e.g. {}), or columns first (e.g. {})? [row/col/exit]\n'.format(example_rowfirst, example_colfirst))
        if 'row' in user_input or 'col' in user_input:
            break
        elif 'exit' in user_input:
            sys.exit()

    result_data = []

    if 'row' in user_input:
        for row_name in row_names:
            for col_name in col_names:
                result_data.append([row_name, col_name])
    else:
        for col_name in col_names:
            for row_name in row_names:
                result_data.append([col_name, row_name])

    print('=== result: ===')
    for row in result_data:
        print(row)
    print('===')

    new_filename = '{}_result.csv'.format(os.path.splitext(filename)[0])
    print('saving result to {}'.format(new_filename))

    with open(new_filename, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in result_data:
            writer.writerow(row)

