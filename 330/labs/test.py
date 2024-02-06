def matrixMult(m1, m2, sol, n, x, y, z):
    if n == 1:
        sol[x][y] += m1[x][z] * m2[z][y] 
        return sol 

    mid = n / 2 

    matrixMult(m1, m2, sol, mid, x, y, z) 
    matrixMult(m1, m2, sol, mid, x, y + mid, z) 
    matrixMult(m1, m2, sol, mid, x, y, z + mid) 
    matrixMult(m1, m2, sol, mid, x, y + mid, z + mid) 
    matrixMult(m1, m2, sol, mid, x + mid, y, z) 
    matrixMult(m1, m2, sol, mid, x + mid, y + mid, z) 
    matrixMult(m1, m2, sol, mid, x + mid, y, z + mid)
    matrixMult(m1, m2, sol, mid, x + mid, y + mid, z + mid) 

    return sol 