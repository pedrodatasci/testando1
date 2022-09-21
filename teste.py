def soma(n1: int, n2: int) -> int:
    return n1 + n2

def subtrai(n1: int, n2: int, ordem:int) -> int:
    n = [n1, n2]
    return max(n1) - min(n2)

if __name__ == '__main__':
    print(soma(1,1))