import psutil
import time
from datetime import datetime
import csv

#Sets CSV variables
header = ['CPU', 'Memory']
data = [psutil.cpu_percent(), psutil.virtual_memory().percent]
filename = datetime.now().strftime('process_monitor-%Y-%m-%d-%H-%M.csv')

#Variable set to raw datetime output
now = datetime.now()

#print(now.hour)

#Cleaned up datetime output
current_time = now.strftime("%H:%M:%S")
#Print out only hour variable from full datetime.now() output
#print(now.hour)

#Set greeting to good morning, good afternoon, good evening, or good night
if now.hour >= 0 and now.hour < 12:
    print("Good morning, it is ", current_time)
elif now.hour >= 12 and now.hour < 16:
    print("Good afternoon, it is ", current_time)
elif now.hour >= 16 and now.hour < 19:
    print("Good evening, it is ", current_time)
else:
    print("Good night, it is ", current_time)

print("Current CPU usage at " + str(psutil.cpu_percent()) + "%")

print("Current memory usage at " + str(psutil.virtual_memory().percent) + "%")

export = input("Would you like to export this data to a .csv file? (yes/no)")

if export == "yes":
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        # write the data
        writer.writerow(data)

        print("Data exported to .csv")

        exit()

elif export == "no":
    print("CSV export denied")

else:
    print("Invalid agrument.")
