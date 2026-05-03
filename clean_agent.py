import random

class Room:
    def __init__(self):
        self.dirty_level=0
    def dirty(self):
        return self.dirty_level>0#make room dirty
    def make_dirty(self):
        self.dirty_level=random.randint(1,5)#setting dirtiness level to a random level from 1 to 5
    def clean_room(self):#make room clean
        self.dirty_level=0 

class Agent:
    def __init__(self,n_rooms):
        self.energy=2.5*n_rooms
        self.position=0
        self.used_energy=0
        self.actions=[]#to store the actions taken(suck,move right,move left)
        self.clean_count=0

def create_environment(n_rooms,initial_room_dirtiness=0.7):#to  create (n_rooms) rooms with random dirtiness
    rooms=[Room() for _ in range(n_rooms)]
    for rm in rooms:
        if random.random()<initial_room_dirtiness:
            rm.make_dirty()
    return rooms 

def dirty_again(rooms):#make rooms dirty with each room having a 10% chance of begoming dirty again
    for rm in rooms:
        if not rm.dirty() and random.random()<0.1:
            rm.make_dirty()

def simulate(n_rooms,max_steps):
    rooms=create_environment(n_rooms)
    agent=Agent(n_rooms)
    for step in range(max_steps):
        if all(not rm.dirty() for rm in rooms):#if all rooms are clean
            break
        current_room=rooms[agent.position]
        if current_room.dirty():
            cost=current_room.dirty_level
            if agent.energy>=cost:#clean the room if it is dirty and agent still has enough energy
                agent.energy-=cost
                agent.used_energy+=cost
                agent.clean_count+=1
                current_room.clean_room()
                agent.actions.append(f"SUCK in Room({agent.position})")
            else:
                break
        else:
            if agent.energy<2:#stop simulation if system ran out of energy
                break
            if agent.position<n_rooms-1:#condition to move right 
                agent.position+=1
                agent.energy-=2
                agent.used_energy+=2
                agent.actions.append("MoveRight")
            elif agent.position>0:#condition to move left 
                agent.position-=1
                agent.energy-=2
                agent.used_energy+=2
                agent.actions.append("MoveLeft")
            else:
                break
        dirty_again(rooms)#after the first round 

    
    print("Final room states:")
    for i,rm in enumerate (rooms):
        if rm.dirty():
            print(f"Room{i}:Dirty(level)={rm.dirty_level}")
        else:
            print(f"Room{i}:Clean")
    
    print("\n Cleaning Results:")
    print("Rooms cleaned:",agent.clean_count)
    print("Total energy consumed",agent.used_energy)
    print("Remaining energy",agent.energy)
    print("Action taken",agent.actions)


simulate(n_rooms=5,max_steps=100)

