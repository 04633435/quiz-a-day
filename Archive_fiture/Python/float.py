from objprint import op

op.config(arg_name=True)
op(0.1 + 0.2 == 0.3)    # False
op(1e50 == 10 ** 50)    # False

op(1e500 == 1e600)   # inf == inf
op(1e500 > 10 ** 1000)    # inf > integer

op(1e500 * 1e500 > 0)   # True
op(1e500 / 1e500 > 0)   # False
op(1e500 / 1e500 == 1e500 / 1e500)    # False


# IEEE 754 二进制下浮点数没办法完美的表示10进制下的浮点数，会产生精度损失。
# the max of double precision float 1e308, flaot('inf') and float('NaN) represent the infinite and non-number in flaot.

