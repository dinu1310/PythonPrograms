import time
import time as t
# tm=t.time()
# print(f"initial time {tm}")
# i=0
# while i<10:
#     print("this is time taken by while loop")
#     i+=1
#
# print(f"initial time {tm}")
#
# for i in range(20):
#     print("this is time taken for loop")
#
# print(f"initial time {tm}")
localtime=time.asctime(time.localtime(time.time()))
print(localtime)

start = int(time.time())

time.sleep(2)  # or do something more productive

done = int(time.time())
elapsed = done - start
print(elapsed)


