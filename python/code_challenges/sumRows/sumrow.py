def sum_rows(matrix):
    totals = []
    for row in matrix:
        sum_row = sum(row)
        totals.append(sum_row)
    return totals
