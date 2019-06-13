# Spreadsheet processor

Turns a spreadsheet of row and column names into the Cartesian product, i.e.:

```
row_names = ['a', 'b', 'c']
col_names = ['1', '2', '3']
result = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
```

Operates on csv files:

```
./process.py test_data.csv
# output: test_data_result.csv
```

