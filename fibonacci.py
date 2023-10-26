class fibonacci_number:
    def __init__(self,nmax):
        self.n_ant = 0
        self.n_current = 1
        self.n_max = nmax
        if self.n_max < 1:
            self.n_current = 0
        
    def __repr__(self):
        return f'Numero {self.n_max} da sequencia de Fibonacci: {self.n_current}'
    
    def calc_fibo(self):
        n = 1
        while n < self.n_max:
            aux = self.n_current
            self.n_current += self.n_ant
            self.n_ant = aux
            n += 1


fib1 = fibonacci_number(10)
fib1.calc_fibo()
print(fib1)