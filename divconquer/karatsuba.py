def karatsuba(x, y):
    """Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
    len_x, len_y = len(str(x)), len(str(y))
    if len_x == 1 and len_y == 1:
        return x * y
    else:
        n = max(len_x, len_y)
        nby2 = int(n / 2)
        x_str = ('%0' + str(n) + 'd') % x
        y_str = ('%0' + str(n) + 'd') % y
        a = int(x_str[:(n - nby2)])
        b = int(x_str[(n - nby2):])
        c = int(y_str[:(n - nby2)])
        d = int(y_str[(n - nby2):])
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
        return int(str(ac) + '0'*(2*nby2)) + int(str(ad_plus_bc) + '0'*nby2) + bd


i = 3141592653589793238462643383279502884197169399375105820974944592
j = 2718281828459045235360287471352662497757247093699959574966967627
print(karatsuba(i, j) - (i * j))
