'''
作者：卢沛安
时间：2022年10月11日
'''
from typing import List , Tuple , Dict , Optional

'''
https://pycoder.blog.csdn.net/article/details/124789706
'''
# IN:   /a//b/a b/aa/
def solve( st ) :
    a , b = '' , ''
    if len( st ) == 1 :
        if st[ 0 ].startswith( " " ) :
            b = st[ 0 ]
        else :
            a = st[ 0 ]
    elif len( st ) == 2 :
        a = st[ 0 ]
        b = st[ 1 ]

    else :
        print( "/" )
    while a.endswith( '/' ) :
        a = a[ :-1 ]
    while b.startswith( "/" ) :
        b = b[ 1 : ]
    a += '/'
    return (a+b)


while 1:
    try:
        sto = input()
        st = sto.split()
        a = ""
        b = ""
        if len(st) == 1:
            # 判断是 前缀还是后缀
            if sto.startswith(" "):
                b = st[0]
            else:
                a = st[0]
        elif len(st) == 2:
            a = st[0]
            b = st[1]
        else:
            print("/")
            continue

        # 我们要求 前缀不由 / 结尾
        # 结尾有多个 /
        while a.endswith("/"):
            a = a[:-1]

        # 开头有多个 /
        while b.startswith("/"):
            b = b[1:]

        # 我们要求 后缀由 / 开始
        b = f"/{b}"

        ans = solve( st)
        true = a+b
        assert( ans  == true )
        print( ans )

    except Exception as e:
        break


if __name__ == '__main__' :
    print( "finished!" )

    a = '/go dfaf??'
