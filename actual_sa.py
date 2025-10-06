import earthaccess as ea
import pandas as pd
import numpy as np 
np.set_printoptions(legacy='1.25')

x= int(input("degree x"))
y = int(input("degree y"))
t = input("years")




ya = y*360
temp_df = pd.read_csv("2024-01-01", header = None)
print(temp_df.iloc[ya+x+1,2])



def avg(x,y,t):
  temp = []
  temp_slope = []
  avg_change = 0
  slope_changes = []
  d = 0
  t = int(t)
  ya = y*360
  for i in range(0,22):
    #temp of each year
    temp_df = pd.read_csv("2024-01-01", header = None)
    #Change this!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    temp.append(float(temp_df.iloc[ya+x+1,2]))
    i+=1
  d = len(temp)-1
  for i in range(0,d):
    #slope per year to modern day
    if i > 0:
      s = (temp[0]-temp[d])/i
      temp_slope.append(s)
    #this creates the differences in slopes
    if i > 1:
      slope_change = temp_slope[i-1]-temp_slope[i-2]
      slope_changes.append(slope_change)
  #this creates average slope increase per year
  a = sum(slope_changes)
  b = len(slope_changes)
  avg_change = a/b
  l = t * avg_change
  new_slope = temp_slope[d-2]+l
  final = temp[d]+new_slope
  return final

def cover(x,y,t,o,):
  cover_df = pd.read_csv("./AIRS.2024.01.01.L3.RetStd_IR001.v7.0.9.3.G25245225503.hdf.csv", header = None)
  cover.append(cover_df[x+o])
  

print("average temp is " + str(avg(x,y,t)))
'''
print("average temp is " + avg(x,y,t))
print("average humidity is " + avg(x,y,t))
print("average rainfall is " + avg(x,y,t))
print("average solidity is " + avg(x,y,t))
'''