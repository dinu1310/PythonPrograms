from datetime import datetime
from time import time
evening = "17:00"
morning = "09:00"
import math
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# if current_time <= evening and current_time>=morning:
#     print(current_time)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
hours = int(now.strftime("%H")) * 60 * 60
minutes = int(now.strftime("%M")) * 60
seconds = int(now.strftime("%S"))
Currtotal_Seconds = hours + minutes + seconds
#61140
pretotal_Seconds = 9 * 60 *60
print(pretotal_Seconds)
print(f"current seconds {Currtotal_Seconds}")
init=time()
print("harry ",init)
li1 = []
li2 = []
li3 = []
for i in range(pretotal_Seconds,16*3600+59*60,1800):
    if i/1800:
      li1.append(i)

for j in range(pretotal_Seconds,16*3600+59*60,2700):
    if j/2700:
        li2.append(j)

for k in range(pretotal_Seconds,16*3600+59*60,3000):
    if k/3000:
        li3.append(k)


print(f"{li1} \n {li2} \n {li3}")

