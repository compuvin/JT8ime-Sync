#!/usr/bin/python3

from datetime import datetime, timedelta
import subprocess
import time
import glob
import os

#Adjust these as you see fit
HeardFolder = "/usr/local/MSHV/AllTxtMonthly/" #Folder containing the files of decoded stations

TimeToAdjust = 2 #Time to adjust time by in seconds
OnceLockedEvalEvery = 60 #Once time is locked, evaluate every x seconds (starts at 15 seconds and doubles until it gets to this number)
#####

TimeLocked = 0
TimeChanged = 0
TimeToEval = 15

#Get the newest decoded text file
list_of_files = glob.glob("{}/*".format(HeardFolder)) # * means all if need specific format then *.csv
HeardFile = max(list_of_files, key=os.path.getctime)
print("Watching " + HeardFile)
with open(HeardFile, 'r') as file: lines = len(file.readlines())
#print(lines)

def set_time_funct():
   try:
       subprocess.run(["sudo", "date", "-s", "{} {}".format(new_date, new_time)], check=False)
       #print("Date and time have been set successfully.")
   except subprocess.CalledProcessError as e:
       print("Error occurred: ", e)


now = datetime.now()

#Ask the user for the current date and time, prefilling what we know
current_date = now.strftime("%m/%d/%Y")
new_date = input("Enter current date [{}]:".format(current_date))
current_time = now.strftime("%H:%M:%S")
new_time = input("Enter current time [{}]:".format(current_time))
if new_date == "": new_date = current_date
if new_time == "": new_time = current_time

#print("Setting to = {} {}".format(new_date, new_time))

set_time_funct()

#Now we listen. We're now on full automatic in the hands of the computers.
while not (TimeLocked == 1):
   #Monitor decoded stations file
   with open(HeardFile, 'r') as file: 
      if (lines < len(file.readlines())):
         TimeLocked = 1
         print("The time has been locked. Fine tuning...")
         break;

   time.sleep(15) #Wait 15 seconds
   #Increase time by "TimeToAdjust" seconds
   # Combine parsed_date and parsed_time into a datetime object
   combined_datetime = datetime.combine(datetime.strptime(new_date, '%m/%d/%Y'), datetime.strptime(new_time, '%H:%M:%S').time())

   # Add seconds to the combined datetime based on TimeToAdjust variable
   new_time = (combined_datetime + timedelta(seconds=17)).strftime("%H:%M:%S")
   set_time_funct()
   TimeChanged = TimeChanged + TimeToAdjust

   #Display current time, runtime, ETA to lock
   ETAtoLock = ((16/2) * 15) - (TimeChanged*15/2+TimeChanged)
   print("Curent time: {}, Runtime: {}, ETA to lock: {}".format(new_time, int(TimeChanged*15/2+TimeChanged), "{:02}:{:02}".format(int(ETAtoLock // 60), int(ETAtoLock % 60))))
   #If the time has increased by > 15 seconds:
   if (TimeChanged > 15):
      #Revert time back to time minus timechanged
      new_time = (combined_datetime - timedelta(seconds=TimeChanged)).strftime("%H:%M:%S")
      set_time_funct()
      #Display message that no stations were heard. Unable to get a time lock.
      print("No stations were heard. Unable to get a time lock.")
      TimeChanged = 0

while (TimeLocked == 1):
   #Create array from recent monitor of the decoded stations
   data_lines = []
   i = 0
   dt_total = 0  # Variable to store the total DT values for calculating the average
   with open(HeardFile, "r") as file:
      for line in file:
         i += 1
         if i > lines:
            if line.strip():
                #print("Line here")
                #print(line.strip().split('\n')[0])
                # Split the line using '|' and extract the required columns
                call_sign = line.strip().split('|')[6].split()[1]
                dt_value = float(line.strip().split('|')[4])
                
                # Append the station and DT values to data_lines
                data_lines.append([call_sign, dt_value])
                
                # Add DT value to the total for calculating the average
                dt_total += dt_value
   lines = i
   #print(data_lines)
   #Create an array with the DT and call sign
   if len(data_lines) > 0:
      average_dt = dt_total / len(data_lines)
      print("Calculating the time based on the following stations:")
      print("Station, DT")
      for station, dt in data_lines:
         print(f"{station}, {dt:.1f}") #Display array of stations
      
      #Adjust the time by the average of received station's difference
      now = datetime.now()
      new_date = now.strftime("%m/%d/%Y")
      if average_dt > 0.5:
         print(now)
         #new_time = now.strftime("%H:%M:%S")
         new_time = (now + timedelta(seconds=average_dt/2)).strftime("%H:%M:%S")
         set_time_funct()
         #Display message showing the changes made to time
         print(f"Time adjusted by: {average_dt/2:.1f}")
      elif average_dt < -0.5:
         new_time = (now - timedelta(seconds=average_dt/2)).strftime("%H:%M:%S")
         set_time_funct()
         #Display message showing the changes made to time
         print(f"Time adjusted by: {average_dt/2:.1f}")
      else:
         print("Time within 0.5 seconds. No adjustments needed.")

      print(f"Listening for {TimeToEval} seconds...")
      time.sleep(TimeToEval) #Wait for x seconds for more stations to be received.
      if OnceLockedEvalEvery > (TimeToEval * 2):
         TimeToEval = TimeToEval * 2
      else:
         TimeToEval = OnceLockedEvalEvery
 
