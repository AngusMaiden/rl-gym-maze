import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
from enum import Enum

# Encode directions as numbers for easier coding.
class Action(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

# Types of squares are a vector of four boolean values, indicating if a wall is at a direction (Up, Down, Left, Right)

a = [0,0,0,1]
b = [0,0,1,0]
c = [0,1,0,0]
d = [1,0,0,0]
e = [0,0,1,1]
f = [0,1,0,1]
g = [1,0,0,1]
h = [0,1,1,0]
i = [1,0,1,0]
j = [1,1,0,0]
k = [0,1,1,1]
l = [1,1,1,0]
m = [1,0,1,1]
n = [1,1,0,1]
o = [1,1,1,1]
p = [0,0,0,0]

# Construct a 2-d maze described by the walls in each location, using the boolean values as a third dimension.
# The result is a 3-d numpy array of shape (10,10,4) storing Boolean values.
map = np.array([[l,j,j,j,d,d,d,d,d,g],
       [i,j,j,g,e,e,e,b,f,e],
       [e,i,j,a,e,k,k,e,i,a],
       [e,e,l,f,b,n,i,c,c,a],
       [e,h,j,j,a,m,h,j,n,e],
       [b,j,j,n,e,b,j,j,d,a],
       [e,i,j,j,p,c,j,d,f,e],
       [e,b,j,g,h,g,l,f,m,e],
       [h,c,g,k,i,a,i,g,e,e],
       [l,j,c,j,c,c,f,h,c,f]], dtype=bool)

# Define the environment using Gym API.

class MazeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        
        self.map = map
        self.goal_location = (9,9)

        # Define action space as 4 possible directions (Up, Down, Left, Right).
        self.action_space = spaces.Discrete(4)

        # Define observation space as a 'Box space', bounded by (0,0) and (9,9), of integers (i.e. discrete values).
        self.observation_space = spaces.Box(low=0, high=9, shape=(2,), dtype=np.int64)        

    # Gym's step function takes an action from the action space, and returns (observation, reward, done, info).
    def step(self, action):     
        assert self.action_space.contains(action), "%r (%s) invalid" % (action, type(action))
        


        # Initialise variables.
        reward = 0
        done = False
        info = {}

        # This code checks the boolean value of the action direction against the map.
        # If there is no wall there (0 value in that direction in the Boolean vector),
        # we update the location and give reward (penalty).

        # If there is a wall in that direction, the location is not updated and no reward is given
        # (a null action).

        if action == Action.UP.value:
            if self.map[self.location][0] != 1:
                self.location = (self.location[0]-1, self.location[1])
                reward = -1

        elif action == Action.DOWN.value:
            if self.map[self.location][1] != 1:
                self.location = (self.location[0]+1, self.location[1])
                reward = -1

        elif action == Action.LEFT.value:
            if self.map[self.location][2] != 1:
                self.location = (self.location[0], self.location[1]-1)
                reward = -1

        elif action == Action.RIGHT.value:
            if self.map[self.location][3] != 1:
                self.location = (self.location[0], self.location[1]+1)
                reward = -1
        
        else:
            print("Invalid action")
            raise ValueError

        # If after these updates, the new location is the goal, the task is complete.
        if self.location == self.goal_location:
            reward = 0
            done = True
        
        state = np.array(self.location)
        return state, reward, done, info
    
    # Resetting function
    def reset(self):
        self.location = (0,0)
        return np.array(self.location)
    
    
    def render(self, mode='human'):
        pass
    
    def close(self):
        pass
    
    @property
    def actions(self):
        return [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT]