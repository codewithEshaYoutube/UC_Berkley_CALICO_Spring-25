def find_champion(T, test_cases):
    ans = []
    for t in range(T):
        N, names, powers = test_cases[t]
        while len(names) > 1:
            new_names, new_powers = [], []
            for i in range(0, len(names), 2):
                if powers[i] > powers[i+1]:
                    new_names.append(names[i])
                    new_powers.append(powers[i] + powers[i+1])
                elif powers[i] < powers[i+1]:
                    new_names.append(names[i+1])
                    new_powers.append(powers[i] + powers[i+1])
                else:
                    new_names.append(names[i] + names[i+1])
                    new_powers.append(powers[i] + powers[i+1])
            names, powers = new_names, new_powers
        ans.append(names[0])
    return ans

if __name__ == "__main__":
    T = int(input())
    test_cases = []
    for _ in range(T):
        N = int(input())
        names = input().split()
        powers = list(map(int, input().split()))
        test_cases.append((N, names, powers))
    
    res = find_champion(T, test_cases)
    for r in res:
        print(r)
