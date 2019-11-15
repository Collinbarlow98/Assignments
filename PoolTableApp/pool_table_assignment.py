
import datetime
import json
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

now = datetime.datetime.now()

pooltables = []
pt_object_array = []

class PoolTable:
  def __init__(self,tablenumber):
    self.tablenumber = tablenumber
    self.start_time = 0
    self.end_time = 0
    self.is_available = True
    self.total_time_played = 0
    self.total_cost = 0

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
    self.total_cost = self.total_time_played.total_seconds() / 60 / 60 * 30

def crash_protection():
    with open('crashprotection.json') as file_object:
        pt_object_array = json.load(file_object)
        for index in range(0,len(pt_object_array)):
            pt_object = pt_object_array[index]
            for key in pt_object:
                pooltables[pt_object["tablenumber"] - 1].tablenumber = pt_object["tablenumber"]
                pooltables[pt_object["tablenumber"] - 1].start_time = datetime.datetime.strptime(pt_object["start_time"], '%Y-%m-%d %H:%M:%S.%f')
                pooltables[pt_object["tablenumber"] - 1].is_available = pt_object["is_available"]

def send_final_report():
    subject = "An email with attachment from Pool Tables"
    body = "This is an email with attachment sent from Pool Tables"
    sender_email = "practiceemailforcode@gmail.com"
    receiver_email = "practiceemailforcode@gmail.com"
    password = input("Type your password and press enter: ")
    report = f'{now.year}-{now.month}-{now.day}.txt'
    smtp_server = "smtp.gmail.com"
    port = 587

    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(f'{report}', 'rb').read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition",f"attachment; filename= {report}",)
    message.attach(part)

    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
    except SMTPException as error:
        print("Error")

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
      print(round(pooltables[tableno].total_cost, 2), "Dollars")
      print("--------------------------------------")
      with open(f'{now.year}-{now.month}-{now.day}.txt', 'a') as file_object:
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
          file_object.write(str(round(pooltables[tableno].total_time_played.total_seconds() / 60 / 60 * 30, 2)))
          file_object.write(" Dollars")
          file_object.write('\r')
    else:
      print("Table Number", pooltables[tableno].tablenumber, "Is Checked In")
      print("--------------------------------------")
  else:
    choice_quit = input("Enter Q To Quit or Anything Else To Continue: ").upper()
    if choice_quit == "Q":
        cp = {}
        with open('crashprotection.json','w') as file_object:
            json.dump(cp,file_object)
        choice_email = input("Would You Like An Email Of The Final Report? Enter Yes or No: ").upper()
        if choice_email == "YES":
            send_final_report()
        else:
            pass
        break
    else:
      pass
