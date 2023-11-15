height = 5
counter = 1

while counter <= height:
    space = height - counter
    while space > 0:
        print(' ', end=' ')
        space -= 1

    copy_counter = counter
    while copy_counter > 0:
        print('*', end=' ')
        copy_counter -= 1
    print()

    counter += 1
