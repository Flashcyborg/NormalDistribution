import csv
import pandas as pd
import statistics

df = pd.read_csv("data.csv") 
height_list = df["Height(Inches)"].to_list()

mean = statistics.mean(height_list)
std_dev = statistics.stdev(height_list)
range1_start,range1_end = mean-std_dev,mean+std_dev
range2_start,range2_end = mean-2*std_dev,mean+2*std_dev
range3_start,range3_end = mean-3*std_dev,mean+3*std_dev

range1_array = [result for result in height_list if result > range1_start and result < range1_end]
range2_array = [result for result in height_list if result > range2_start and result < range2_end]
range3_array = [result for result in height_list if result > range3_start and result < range3_end]

len1 = len(range1_array)
len2 = len(range2_array)
len3 = len(range3_array)

print (len1)
print (len2)
print (len3)