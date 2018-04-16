# -*- coding: utf-8 -*-

def demo(num1,num2):

    assert isinstance(num1,int) , "num1 必须是数字"
    assert isinstance(num2,int) , "num2 必须是数字"
    assert num2 != 0 , "num2 不能为　0"

    num1 = float(num1)
    num2 = float(num2)


    v = num1/num2


    return v


if __name__ == '__main__':
    print demo(1,2)