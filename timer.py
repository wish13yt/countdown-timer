import time
timen = "60"
for x in range(0, 60):
  time.sleep(1)
  timeint = int(timen)
  print(timeint)
  timem = timeint - 1
  print(timem)
  timen = str(timem)