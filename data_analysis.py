# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106061227.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
    # remove data if PRES is -99 or -999
    if(row["PRES"] != "-99" and row["PRES"] != "-999"):
        data.append(row)
      
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.

target_id = ["C0A880", "C0F9A0", "C0G640", "C0R190", "C0X260"]
target_data = {}
for ids in target_id:
    values = []
    for stations in data:
        if(stations["station_id"] == ids):
            values.append(float(stations["PRES"]))
    if(values == []):
        target_data[ids] = "None"
    else:
        target_data[ids] = sum(values)/len(values)
            
#target_data = data[:10]

#=======================================

# Part. 4
#=======================================
# Print result
#print(pres_mean)
print(target_data)
#========================================