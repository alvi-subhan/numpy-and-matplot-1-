from matplotlib import pyplot as plt
from collections import Counter

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

#for key,val in histogram.items():


plt.bar([x for x in histogram.keys()], # shift each bar to the left by 4
histogram.values(), # give each bar its correct height
8)# give each bar a width of 8
plt.axis([-5, 105, 0, 5]) # x-axis from -5 to 105,
# y-axis from 0 to 5

grading=["fail","fail","fail","fail","fail","fail","C","B","A","A+","A+"]
#10*i is used for spacing remove 10 and then check the results
plt.xticks([10 * i for i in range(11)],grading) # x-axis labels at 0, 10, ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()