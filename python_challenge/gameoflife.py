class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def getNeighbours(cell, m, n):
    if cell.x > 0:
        yield Cell(cell.x-1, cell.y)
    if cell.x < m:
        yield Cell(cell.x+1, cell.y)
    if cell.y > 0:
        yield Cell(cell.x, cell.y-1)
    if cell.y < n:
        yield Cell(cell.x, cell.y+1)
    if cell.x > 0 and cell.y > 0:
        yield Cell(cell.x-1, cell.y-1)
    if cell.x < m and cell.y < n:
        yield Cell(cell.x+1, cell.y+1)
    if cell.x > 0 and cell.y < n:
        yield Cell(cell.x-1, cell.y+1)
    if cell.x < m and cell.y > 0:
        yield Cell(cell.x+1, cell.y-1)

'''
Get next snapshot of population

Args:
    T: int. Time Step
    pattern: numpy array. 2D numpy array of population information

Returns: numpy array.
'''
def next(T, pattern):
    (m, n) = pattern.shape
    for t in range(T):
        pop = pattern[:]
        for i in range(m):
            for j in range(n):
                life = 0
                for cell in getNeighbours(Cell(i,j), m-1, n-1):
                    life += pattern[cell.x][cell.y]

                if life < 2 or life > 3: #die
                    pop[i][j] = 0
                if pattern[i][j] == 0 and life == 3: #born
                    pop[i][j] = 1

        pattern = pop
        yield pattern