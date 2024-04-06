# Feaching All Users who currently loged in in machine

#This module return the date of the Event
def get_event_date(event):
  return event.date

#This module return the dictionary of all user who currently loged in machine.
def current_users(events): 
  events.sort(key=get_event_date) #sort the event according to the date
  machines = {} #create a dictionary to store the user and the machine
  for event in events: #loop through the events
    if event.machine not in machines: #if the machine is not in the dictionary
      machines[event.machine] = set() #add the machine to the dictionary
    if event.type == "login": #if the event is login
      machines[event.machine].add(event.user) #add the user to the machine
    elif event.type == "logout": #if the event is logout
        if event.user in machines[event.machine]: #if the user is in the machine
            machines[event.machine].remove(event.user) #remove the user from the machine
  return machines #return the dictionary machines

#This module give the name of all user who currently loged in machine.
def generate_report(machines): #this function takes the dictionary machines as an argument
  for machine, users in machines.items(): #loop through the dictionary machines
    if len(users) > 0: #if the machine has users
      user_list = ", ".join(users) #join the users with a comma and a space
      print("{}: {}".format(machine, user_list)) #print the machine and the users

class Event: #this class represent an event
  def __init__(self, event_date, event_type, machine_name, user): #this function initialize the event
    self.date = event_date  #this attribute represent the date of the event
    self.type = event_type  #this attribute represent the type of the event
    self.machine = machine_name  #this attribute represent the name of the machine
    self.user = user  #this attribute represent the name of the user

#this is events list
events = [
    Event('2024-04-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2024-04-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2024-04-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2024-04-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2024-04-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2024-04-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
    Event('2024-04-24 08:22:16', 'login', 'webserver.local', 'chris'),
    Event('2024-04-22 19:54:45', 'login', 'mailserver.local', 'aman'),
]

users = current_users(events) #call the function current_users
print(users) #print the dictionary users


generate_report(users) #call the function generate_report
