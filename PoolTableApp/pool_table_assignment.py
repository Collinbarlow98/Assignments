
import datetime
import json

pooltables = []
pt_object_array = []

class PoolTable:
  def __init__(self,tablenumber):
    self.tablenumber = tablenumber
    self.start_time = 0
    self.end_time = 0
    self.is_available = True
    self.total_time_played = 0

  def check_out(self):
    if self.is_available == True:
      self.is_available = False
      self.start_time = datetime.datetime.now()
    else:
      print("Pool Table", self.tablenumber, "Is Checked Out")

  def check_in(self):
    self.is_available = True
    self.end_time = datetime.datetime.now()

  def calculate_total(self):
    self.total_time_played = self.end_time - self.start_time
    total_cost = self.total_time_played.total_seconds() / 60 / 60 * 30
    print(total_cost, "Dollars")

def crash_protection():
    with open('crashprotection.json') as file_object:
        pt_object_array = json.load(file_object)
        for index in range(0,len(pt_object_array)):
            pt_object = pt_object_array[index]
            for key in pt_object:
                pooltables[pt_object["tablenumber"] - 1].tablenumber = pt_object["tablenumber"]
                pooltables[pt_object["tablenumber"] - 1].start_time = datetime.datetime.strptime(pt_object["start_time"], '%Y-%m-%d %H:%M:%S.%f')
                pooltables[pt_object["tablenumber"] - 1].is_available = pt_object["is_available"]

for index in range(1,13):
        pool_table = PoolTable(index)
        pooltables.append(pool_table)

crash_protection()

while True:

  for index in range(0,len(pooltables)):
      print("Table", pooltables[index].tablenumber)
      if pooltables[index].is_available == True:
        print("NOT OCCUPIED")
      else:
        print("OCCUPIED", pooltables[index].start_time, datetime.datetime.now() - pooltables[index].start_time)
  print("--------------------------------------")

  print("Press 1 To Check Out A Table")
  print("Press 2 To Check In A Table")
  choice = input("Enter Your Choice: ")
  print("--------------------------------------")

  if choice == "1":
    print("Enter Table Number To Check Out")
    tablenoco = int(input("Enter Number: "))
    pooltables[tablenoco - 1].check_out()
    print("--------------------------------------")
    pt_object = {
    "tablenumber": pooltables[tablenoco - 1].tablenumber,
    "start_time":  str(pooltables[tablenoco - 1].start_time),
    "is_available": pooltables[tablenoco - 1].is_available,
    }
    pt_object_array.append(pt_object)
    with open('crashprotection.json', 'w') as file_object:
        json.dump(pt_object_array,file_object)
  elif choice == "2":
    print("Enter Table Number To Check In")
    tableno = int(input("Enter Number: ")) - 1
    if pooltables[tableno].is_available is False:
      pooltables[tableno].check_in()
      pooltables[tableno].calculate_total()
      print("--------------------------------------")
      with open('11-12-2019.txt', 'a') as file_object:
          file_object.write("Table Number: ")
          file_object.write(str(pooltables[tableno].tablenumber))
          file_object.write('\r')
          file_object.write("Start Time: ")
          file_object.write(str(pooltables[tableno].start_time))
          file_object.write('\r')
          file_object.write("End Time: ")
          file_object.write(str(pooltables[tableno].end_time))
          file_object.write('\r')
          file_object.write("Total Time Played: ")
          file_object.write(str(pooltables[tableno].total_time_played))
          file_object.write('\r')
          file_object.write("Total Cost: ")
          file_object.write(str(pooltables[tableno].total_time_played.total_seconds() / 60 / 60 * 30))
          file_object.write(" Dollars")
          file_object.write('\r')
    else:
      print("Table Number", pooltables[tableno].tablenumber, "Is Checked In")
      print("--------------------------------------")
  else:
    choice3 = input("Enter Q To Quit or Anything Else To Continue: ").upper()

    if choice3 == "Q":
        cp = {}
        with open('crashprotection.json','w') as file_object:
            json.dump(cp,file_object)
        break
    else:
      pass

# If the app crashes, have the app read a text file and set up the tables again
# first set up a text file at check out to mark down the start time
# then have the app check that file to see if there are any previously open tables
# then input the start time from those tables
# make the information into a dictionary so that json can dump
