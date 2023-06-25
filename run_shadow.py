#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


tk = TkDrawer()
try:
    tests = ['test'+str(i) for i in range(1, 8)]
    for name in tests + ["ccc", "cube", "box", "pyramid", "king", "cow"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        p = Polyedr(f"data/{name}.geom")
        p.draw(tk)
        print("сумма длин проекций полностью невидимых рёбер, центр которых",
              " находится строго внутри сферы радиуса 4 -> ", p._lenght())
        delta_time = time() - start_time
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
