import math
# math module(==library)를 통째로 가져옴
from math import pi
# math module로부터 pi만을 가져옴

import random

if __name__ == "__main__":
    print(pi)
    print(math.ceil(0.2))
    print(math.floor(2.34))
    print(math.sqrt(16))

    print(random.random())
    print(random.randint(1, 10))



