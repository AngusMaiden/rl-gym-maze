from gym.envs.registration import register

register(
    id='rl-gym-maze-v0',
    entry_point='rl_gym_maze.envs:MazeEnv',
)