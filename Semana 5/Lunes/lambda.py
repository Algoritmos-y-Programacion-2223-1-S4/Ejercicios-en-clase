def square(x):
    return x**2

def main():
    square_lambda = lambda x: x**2
    print(square(5))
    print(square_lambda(5))

main()