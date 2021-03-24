from gym.envs.registration import register

register(
    id='rl-gym-maze',
    entry_point='rl_gym_maze.envs:MazeEnv',
)