# -*- coding: utf-8 -*-

class Tutoring1:
  expertise = {} # Created expertise as a dictionary
  role = {} # Created tole as a dictionary
  time = {} # Created time as a dictionary
  needed_role = "mentor"
  dom = None # Domain of expertise
  demand_stack = None

  def __init__ (self,no): #no is the parameter which tells the current number of entry. Used as key for dictionary
    print("Welcome")
    self.key = no
    self.expertise[self.key] = []
    self.role[self.key] = []
    self.time[self.key] = []
  
  def addStacks(self,dom):
    self.expertise[self.key].append(dom)

  def setMentorOrLearner(self,role): # Enter mentor for 'mentor' and 'learner' for learner
    self.role[self.key].append(role)

  def setAvailableTime(self,time): # Assuming time is given as an integer value
    if self.role[self.key] ==['mentor']:
      self.time[self.key].append(time)
    else:
      self.time[self.key].append(None)

  def getMentor(self,demand_stack,req_time): # demand_stack is the demanded expertise
    f=0
    needed = demand_stack
    req_role = ['mentor']
    for j in self.role:
      if self.role[j]==['mentor']:
        if demand_stack in self.expertise[j]:
          if req_time in self.time[j]:
            print("Mentor " + j + " is available")
            f=1
    if f==0:
      print("No mentor is available")


# Now will show output

t1 = Tutoring1("alan")
# Welcome

t1.addStacks("Python")
t1.addStacks("C")
t1.setMentorOrLearner("mentor")
t1.setAvailableTime(2)
t1.getMentor("Python",2)
# Mentor alan is available
t2 = Tutoring1("bk")
# Welcome
t2.addStacks("C")
t2.setMentorOrLearner("mentor")
t2.setAvailableTime(1)
t2.getMentor("C",1)
# Mentor bk is available

t2.getMentor("C",2)
# Mentor alan is available

t2.getMentor("Java",3)
 #No mentor is available

t3 = Tutoring1("abrew")
# Welcome
t3.addStacks("Go")
t3.setMentorOrLearner("learner")
t3.setAvailableTime(2)
t3.getMentor("Python",2) # Here, i gave different area of demand, beacuse of the assumptiion that learner can select different domain other than his area of expertise
# Mentor alan is available