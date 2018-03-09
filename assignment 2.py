from matplotlib import pyplot as plt
from collections import Counter

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)
#print(histogram)
cluster={0:0,1:0,2:0}

for key,val in histogram.items():
    if key<50:
        cluster[0]+=1
    elif key<70 :
        cluster[1]+=1
    else:
        cluster[2]+=1
print(cluster)

plt.bar([x+7 for x in cluster.keys()], # shift each bar to the left by 4
cluster.values(), # give each bar its correct height
8)# give each bar a width of 8
plt.axis([-5, 105, 0, 5]) # x-axis from -5 to 105,
# y-axis from 0 to 5

grading=["fail","A","A+"]

plt.xticks([i*10 for i in range(3)],grading) # x-axis labels at 0, 10, ..., 100

plt.xlabel("Decile")
plt.ylabel("num of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()