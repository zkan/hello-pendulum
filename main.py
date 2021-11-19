from datetime import datetime

import pendulum


dt = pendulum.datetime(2021, 11, 19)
print(isinstance(dt, datetime))
print(dt)

dt_helsinki = pendulum.datetime(2021, 11, 19, tz="Europe/Helsinki")
print(f"Date Time in Helsinki: {dt_helsinki}")

dt_bangkok = pendulum.datetime(2021, 11, 19, 20, 0, 0, tz="Asia/Bangkok")
print(f"Date Time in Bangkok: {dt_bangkok}")

dt_bangkok_in_sg = dt_bangkok.in_tz("Singapore")
print(f"Date Time Bangkok in Singapore: {dt_bangkok_in_sg}")

dt_bangkok_in_us_eastern = dt_bangkok.in_tz("US/Eastern")
print(f"Date Time in Bangkok in US/Eastern: {dt_bangkok_in_us_eastern}")

diff = dt_bangkok.diff(dt_helsinki)
print(f"Diff in Days: {diff.in_days()}")
print(f"Diff in Hours: {diff.in_hours()}")
print(f"Diff in Minutes: {diff.in_minutes()}")
print(f"Diff in Seconds: {diff.in_seconds()}")

print(pendulum.from_format("2021-11-19 20:11:00", "YYYY-MM-DD HH:mm:ss"))

now = pendulum.now()
print(f"Now: {now}")
print(f"Now in US/Eastern: {now.in_tz('US/Eastern')}")

dt = pendulum.from_format("2021-11-19 20:11:00", "YYYY-MM-DD HH:mm:ss")
print(dt.diff_for_humans())
