def getFactors(n):
    return [factor for factor in range(1, n+1) if n % factor == 0]

print(f'name is factors is {__name__}')