def get_wealth(accounts):
    max_wealth = 0
    for lista in accounts:
        if sum(lista) > max_wealth:
            max_wealth = sum(lista)
    return max_wealth

def main():
    accounts = [
        [1,2,3],
        [3,2,1],
        [10,28,15],
        [30,25,17],
        [38,27,14]
    ]
    wealth = get_wealth(accounts) 
    print("The max wealth is", wealth)

main()

