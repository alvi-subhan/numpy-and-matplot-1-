import numpy as np
from matplotlib import pyplot as plt

dates, price, close,volume=np.loadtxt('prices.csv', delimiter=',', usecols=(0,2,3,6), unpack=True, dtype='str')
"""print(type(dates))
print(type(price))
print(volume)"""

i=0
str_date=[]
str_close=[]
str_price=[]
str_volume=[]
for date in dates:
    zz=date.split("'")
    str_date.append(zz[1])
for cl in close:
    clz=cl.split("'")
    str_close.append(clz[1])
for pr in price:
    prz=pr.split("'")
    str_close.append(prz[1])
#print(type(str_close[1]))

for vl in volume:
    vlz=vl.split("'")
    str_volume.append(vlz[1])
#volume

import datetime
def dates2num(s):
    return datetime.datetime.strptime(s, "%d-%m-%Y").date().weekday()
dates=list(map(dates2num,str_date))
dates=np.asanyarray(dates,'f')
price=np.asanyarray(str_price,'f')
close=np.asanyarray(str_close,'f')
volume=np.asanyarray(str_volume,'f')
#print(dates)

avgs = np.zeros(5)
for i in range(5):
    indices = np.where(dates == i)
    prices = np.take(close, indices)
    avg = np.mean(prices)
    # print("Day", i, "\nprices", prices, "\nAverage", avg)
    avgs[i] = avg

print("average prices of week day:", avgs)

dayss=["Monday","Tuesday","Wednesday","Thursday","Friday"]

returns=np.diff(close)/close[:-1]
slicing_returns=returns[:1000]
positive_indexes=np.where(slicing_returns>0) #index of days with positive returns

days_poitiv=np.take(dates,positive_indexes)
days_poitiv=days_poitiv.tolist()#converting the numpy array to list
"""the length of the days_positiv was 1 therefore we did the below step"""
days_poitiv=[lii for li in days_poitiv for lii in li]
#print(len(days_poitiv))

#checking the day with most posetive return

num_of_days={0:0,1:0,2:0,3:0,4:0}
#for key,val in num_of_days.items:
for datss in days_poitiv:
    if datss in num_of_days:
        num_of_days[datss]+=1
print(num_of_days)

#week days and posetive returns
#trying to see the week day in which we have the most posetive returns

keyss=[]
vals=[]
for key,val in num_of_days.items():
    keyss.append(key)
    vals.append(val)

print(sum(vals))

plt.bar(keyss,vals)
plt.title("Week Day with the most returns out of 528 days")
plt.ylabel("No.of days")
plt.xlabel("Week day")
plt.xticks([i for i, _ in enumerate(dayss)], dayss)
plt.show()

#best week day where volume is high

"""avg_vol = np.zeros(5)
for i in range(5):
    indices_vol = np.where(dates == i)
    vols= np.take(volume, indices_vol)
    avg = np.mean(vols)
    # print("Day", i, "\nprices", prices, "\nAverage", avg)
    avg_vol[i] = avg

num_of_days={0:0,1:0,2:0,3:0,4:0}
#for key,val in num_of_days.items:
for datss in days_poitiv:
    if datss in num_of_days:
        num_of_days[datss]+=1
print(num_of_days)

keyss_vol=[]
vals_vol=[]
for key,val in avg_vol.items():
    keyss_vol.append(key)
    vals_vol.append(val)
print(avg_vol)

plt.bar(keyss_vol,vals_vol)
plt.title("Week Day with the most volume out of 528 days")
plt.ylabel("No.of days")
plt.xlabel("Week day")
plt.show()"""