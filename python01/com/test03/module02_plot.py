import matplotlib.pyplot as plt
import random


def plot1():
    y = [1, 5, 2, 3, 4]

    #plt.plot(y)
    #plt.plot(y, 'y-')
    #plt.plot(y, 'ro')
    plt.plot(y, 'm*')  # '색상 스타일'

    plt.xlabel('x-label')
    plt.ylabel('y-label')

    plt.show()


def plot2():
    y_1 = [10, 2, 5, 3, 9]
    y_2 = [3, 6, 5, 7, 1]

    plt.plot(y_1, 'r-.')
    plt.plot(y_2, 'y-')

    plt.xlabel('x')
    plt.ylabel('y')

    # x축 눈금 표시
    plt.xticks([0, 1, 2, 3, 4])

    plt.show()


def plot3():
    # 월별 판매수량
    month = range(1, 13) # x좌표로 삼을예정 (월별)
    #amount = [14, 12, 17, 20, 10, ....., ]
    amount = [random.randint(10, 20) for i in range(12)] # y좌표로 삼을예정(판매수량)

    plt.plot(month,amount)

    plt.xlabel('month')
    plt.ylabel('sales amount')

    plt.xticks(month)
    plt.yticks(range(10, 21))

    plt.show()


if __name__ == "__main__":
    plot3()