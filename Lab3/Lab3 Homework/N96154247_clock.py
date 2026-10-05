import tm1637
import time
from datetime import datetime

CLK = 23
DIO = 24

tm = tm1637.TM1637(clk=CLK, dio=DIO)

while True:
    now = datetime.now()

    hour = now.hour
    minute = now.minute

    # 偶數秒亮冒號，奇數秒關冒號
    if now.second % 2 == 0:
        tm.numbers(hour, minute, True)
    else:
        tm.numbers(hour, minute, False)

    time.sleep(0.1)