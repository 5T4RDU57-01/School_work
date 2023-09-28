def main():
    values = []
    i = 0

    while i < 10:
        n = input('Value: ')
        try:
            values.append(int(n))
        except:
            print('Value must be a number')
            continue

        i += 1

    print(f'The lowest value is: {lowest(values)}')

def lowest(list_of_values):
    x = list_of_values[0]
    
    for item in list_of_values:
        if item < x:
            x = item
    
    return x


if __name__ == '__main__':
    main()