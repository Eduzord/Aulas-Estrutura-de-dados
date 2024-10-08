def fat(n):
    #caso base
    if n == 0:
        return 1
    # caso recursivo
    else:
        return n * fat(n-1)
