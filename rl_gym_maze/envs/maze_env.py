import gym
from gym import error, spaces, utils
from gym.utils import seeding

class MazeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        print("init")
    def step(self, action):
        pass
    def reset(self):
        pass
    def render(self, mode='human'):
        pass
    def close(self):
        pass