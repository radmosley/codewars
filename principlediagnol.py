def diagonal(matrix):
    secondary = 0
    principle = 0
    ppointer = 0
    spointer = len(matrix)-1

    for x in matrix:
      principle = principle + x[ppointer]
      secondary = secondary + x[spointer]
      ppointer += 1
      spointer -= 1

    if principle > secondary:
      return 'Principal Diagonal win!'

    elif principle < secondary:
      return'Secondary Diagonal win!'

    else:
      return 'Draw!'

problem = [[2,0,0], [0,1,0], [0,0,4]]
problem2 = [[2,2,2], [4,2,6], [8,8,2]]
print(diagonal(problem))
print(diagonal(problem2))