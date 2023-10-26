def input_number(text) -> int:
    print(text, end='')
    while True:
        try:
            number = int(input())
        except ValueError:
            print('Pls input a number (int): ', end='')
            continue
        else:
            break
    return number