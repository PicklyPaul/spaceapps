import earthaccess
import xarray as x
import datetime as dt
import pandas as pd
import boto3 as b3

s3.b3.resource("s3")
login = earthaccess.login()
c = int(input("year:"))
#"AIRS3STD"
#"GPM_3IMERGDF"
d = input("shortname")
f = "SurfAirTemp_A"
def lookup(c,d,f):
    months = (31,28,31,30,31,30,31,31,30,31,30,31)
    l_months = (31,29,31,30,31,30,31,31,30,31,30,31)
    remainder = c % 4
    if remainder == 0:
        mon = months
    else:
        mon = l_months
    a = 1
    b = 1
    for i in range(0,51):
        week = i+1
        if a+6 > mon[b]:
            ba +=1
            aa = a+6-mon[b]
        else:
            ba = b
            aa = a+6
        merge = pd.DataFrame()
        results = earthaccess.search_data(
            short_name = d ,
            version = "7.0",
            temporal = (
                dt.datetime(c,b,a+1),
                dt.datetime(c,ba,aa),
                )
        )
        l = "data/"+str(c)+"/"+str(week)+'/'+str(d)
        download = earthaccess.download(results, local_path=l )
        z = len(results)-1
        for i in range(0,z):
             try:
                ds = x.open_dataset(download[i], engine="netcdf4")
                df = ds[f].to_dataframe()
                except Exception:
                e = 0
                finally:
                p = 'c' +str(i)
                merge[p] = df[f]
        sums = merge[["c0","c1","c2","c3","c4","c5"]].sum(axis=1)
        null = merge.notnull().sum(axis=1)
        avg = sums/null
        path = "data/" + str(c) +"/"+ str(week) + "/" + str(f)+"/week_final.csv"
        avg.to_csv(path)
        a = aa+1
        if a > mon[b]:
            b = ba+1
        else:
            b = ba
        i+=1
        


print(lookup(c,d))
air = ["AIRS3STD","RelHumSurf_A"]
gpm = ["precipitation","probabilityLiquidPrecipitation"]