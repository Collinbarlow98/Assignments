
import datetime

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

table1 = PoolTable(1)
table2 = PoolTable(2)
table3 = PoolTable(3)
table4 = PoolTable(4)
table5 = PoolTable(5)
table6 = PoolTable(6)
table7 = PoolTable(7)
table8 = PoolTable(8)
table9 = PoolTable(9)
table10 = PoolTable(10)
table11 = PoolTable(11)
table12 = PoolTable(12)

pooltables = [table1,table2,table3,table4,table5,table6,table7,table8,table9,table10,table11,table12]

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
    pooltables[int(input("Enter Number: ")) - 1].check_out()
    print("--------------------------------------")
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
      break
    else:
      pass
