def main():
    vals = []
    i = 0
    while i < 3:
        n = input('Value: ')
        try:
            vals.append(int(n))
            i += 1
        except:
            print('Value must be a number')
            continue

    print(order(vals))


def order(list_of_values):
    min , max = list_of_values[0] , list_of_values[0]
    for item in list_of_values:
        if item > max:
            max = item

        if item < min:
            min = item


    for item in list_of_values:
        if item not in [min , max]:
            mid = item

    return min , mid , max


if __name__ == '__main__':
    main()

    