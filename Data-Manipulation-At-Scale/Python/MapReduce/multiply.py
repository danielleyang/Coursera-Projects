import MapReduce
import sys

# Problem 6 Design a MapReduce algorithm to compute the matrix multiplication A x B

mr = MapReduce.MapReduce()

# Part 1 Mapper
def mapper(record):
    # record is a line of matrix.json
    # key: matrix_a or matrix_b
    key = record[0]
    value = []
    if key == "a": # if it's from matrix a, then we return (key, [matrix_a_row, matrix_a_col, value])
        value.append(record[1])
        value.append(record[2])
        value.append(record[3])
        mr.emit_intermediate(key,value)
    elif key == "b": # if it's from matrix b, then we return (key, [matrix_b_col, matrix_b_row, value])
        value.append(record[2])
        value.append(record[1])
        value.append(record[3])
        mr.emit_intermediate(key,value)

# Part 2 Reducer
def reducer(key, list_of_values):
    # key: from matrix a or matrix b
    # list_of_values
    matrix_multi_A = {}
    matrix_multi_B = {}
    result = []

    # create two dictionaries which has the key as their matrix position and value as corresponding values
    for matrix_a_points in mr.intermediate["a"]:
        matrix_multi_A[(matrix_a_points[0],matrix_a_points[1])] = matrix_a_points[2]
    for matrix_b_points in mr.intermediate["b"]:
        matrix_multi_B[(matrix_b_points[0],matrix_b_points[1])] = matrix_b_points[2]

    # fill in the zero
    for key_A in matrix_multi_A.keys():
        if key_A not in matrix_multi_B.keys():
            matrix_multi_B[key_A] = 0
    for key_B in matrix_multi_B.keys():
        if key_B not in matrix_multi_A.keys():
            matrix_multi_A[key_B] = 0

    # figure out the matrix dimension
    dim = []
    row = []
    col = []
    for keys in matrix_multi_A.keys():
        dim.append(list(keys))
    for keys in dim:
        row.append(keys[0])
        col.append(keys[1])
    row = max(row)
    col = max(col)

    # do the multiplications
    for i in range(0,row+1):
        for j in range(0,col+1):
            result = 0
            for k in range(0,col+1):
                result += matrix_multi_A[(i,k)] * matrix_multi_B[(j,k)]
            mr.emit((i,j,result))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
