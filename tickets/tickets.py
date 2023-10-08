def main():
    while True:
        try:
            start = int(input('Start point: '))
            end = int(input('End point: '))
            people = int(input('Number of passengers: '))
            break
        except:
            print('All inputs must be integers. Try again!')
            continue
        
    cost = get_total(people, end - start)
    print(f'Cost: ${cost}')
    while True:
        try:
            money = int(input('Payment: '))
            break
        except:
            print('Input must be an integer.')
            continue
    
    print(f'Change: ${money - cost}')


def get_total(passengers, stations):
    discount = 0
    if passengers > 3:
        discount = 0.1

    total = (passengers * stations) - (passengers * discount)

    return total


if __name__ == '__main__':
    main()