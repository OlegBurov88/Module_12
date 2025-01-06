import calk


def test_add():
    if calk.add(2, 3) == 5:
        print('Test add(a, b) is OK')
    else:
        print('Test add(a, b) is FAIL')


def test_sub():
    if calk.sub(2, 3) == -1:
        print('Test sub(a, b) is OK')
    else:
        print('Test sub(a, b) is FAIL')


def test_mul():
    if calk.mul(2, 3) == 6:
        print('Test mul(a, b) is OK')
    else:
        print('Test mul(a, b) is FAIL')


def test_div():
    if calk.div(2, 3) == 2 / 3:
        print('Test div(a, b) is OK')
    else:
        print('Test div(a, b) is FAIL')


test_add()
test_sub()
test_mul()
test_div()
