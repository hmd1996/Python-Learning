def test_print1():
    print("1" * 10)

def test_print2():
    print('2' * 10)
    test_print1()
    print('2' * 10)
test_print2()