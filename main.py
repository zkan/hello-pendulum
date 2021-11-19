from datetime import datetime

import pendulum


dt = pendulum.datetime(2021, 11, 19)
print(isinstance(dt, datetime))
print(dt)
