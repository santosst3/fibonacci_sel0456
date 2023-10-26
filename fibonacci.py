def calc_fibo(obj_fibo):
    obj_fibo.n_current = obj_fibo.calc_fibo_recursive(obj_fibo.n_max)


def calc_fibo_fallback(obj_fibo):
    n = 1
    n_ant = 0
    n_current = 1
    while n < obj_fibo.n_max:
        aux = n_current
        n_current += n_ant
        n_ant = aux
        n += 1
    return n_current


class fibonacci_number:
    def __init__(self,nmax):
        self.n_ant = 0
        self.n_current = 1
        self.n_max = nmax
        if self.n_max < 1:
            self.n_current = 0
        
    def __repr__(self):
        return f'Numero {self.n_max} da sequencia de Fibonacci: {self.n_current}'
    
    def calc_fibo_recursive(self,n):
        if n > 1:
            return self.calc_fibo_recursive(n-1) + self.calc_fibo_recursive(n-2)
        return n+1


fib1 = fibonacci_number(10)
calc_fibo(fib1)
print(fib1)


def test_answer():
    assert fib1.n_current == calc_fibo_fallback(fib1)