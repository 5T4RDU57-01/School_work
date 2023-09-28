import sys

def main():
    while True:
        money = input('Amount: ')
        if validation(money):
            twenty , ten = bills(int(money))
            print(f'$20 bills: {twenty}\n$10 bills: {ten}')
            break
        else:
            continue


def validation(money):
    try:
        money = int(money)
    except:
        return False
    if money % 10 == 0:
        return True
    
    return False


def bills(n):
    twenty = n // 20
    ten = (n - (twenty * 20)) // 10

    return twenty , ten


if __name__ == '__main__':
    main()