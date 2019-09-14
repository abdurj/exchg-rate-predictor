from xe_init import *
import datetime
import pandas as pd
from tqdm import tqdm
import sys

first_day = datetime.datetime(2017, 1, 1).date() # change as appropriate
last_day = datetime.datetime(2019, 9, 13).date()

if not len(sys.argv) == 2:
  print("Usage: scrapping CURRENCY")

cur = sys.argv[1]

all_dates = [first_day]
day = first_day
while (day < last_day):
    day += datetime.timedelta(days=1)
    all_dates.append(day)

#currencies = ["EUR", "JPY", "GBP", "CHF", "CAD", "AUD"]

inp = dict()
arr = []
for day in tqdm(all_dates):
    lkup = xecd.historic_rate_period(1, "USD", cur, str(day) + "T00:00", str(day) +"T23:59")
    print(lkup)
    if not 'to' in lkup:
        print("The last successful date is {}".format(str(day))
        break
    arr.append(lkup['to'][cur][-1]['mid'])
    #lkup = xecd.historic_rate(day, "", "USD", cur, 1)
    #arr.append(lkup['to'][0]['mid'])
inp[cur] = arr

df = pd.DataFrame(inp, index = all_dates)
df.to_csv(cur + "conv.csv")


