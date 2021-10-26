# rl-gym-maze
A Maze Environment for Reinforcement Learning Solutions in OpenAI Gym.  

This is a fully functional Gym environment (see https://gym.openai.com/ for documentation).

It can be downloaded and installed with the following terminal commands (requires [git](https://git-scm.com/) and [pip](https://pypi.org/project/pip/)):
```bash
git clone https://github.com/AngusMaiden/rl-gym-maze
pip install -e ./rl-gym-maze
```

## Environment Scope

The maze is represented by a two-dimensional grid of 10×10 discrete square spaces, which can be constructed as a custom Gym environment. The agent's starting location is a particular square, while the exit is another square at the edge of the maze, with the goal of the agent being to reach the exit as efficiently as possible. The state space **s<sub>t</sub>** is the agent's location at time **t**, represented by x and y coordinates in the range of the maze grid, **(x,y | x,y ∈ [0,1,2,…,9])**. There are thus 10×10 = 100 potential location states. Movement is the process of changing states over time **t**, which is measured in discrete intervals where **t** is a positive integer, **t ∈ N**. Thus movement is observed as a sequence of discrete time steps.

At each step, the agent can move into an adjacent location, within certain constraints. The action space **a<sub>t</sub>** is the set of all possible movements from the current location **s<sub>t</sub>** to an adjacent location **s<sub>(t+1)</sub>**, constrained to four cardinal directions in a two-dimensional plane: *Up*, *Down*, *Left* and *Right*. The walls of the maze add further constraints on movement between certain locations, so for example if there is a wall between location **(1,2)** and location **(2,2)** below it, then the action space **a<sub>t</sub>** at **s<sub>t</sub> = (1,2)** is limited to *Up*, *Left* and *Right*, with *Down* not being a possible action. By constructing action spaces at every possible state **(x,y)** we can describe the whole structure of the maze in terms of the agent's potential movements through it.

Each time step from **t** to **t+1** updates the agent's state **s<sub>t</sub>** to a new state **s<sub>(t+1)</sub>** which is determined by a choice of actions from the action space **a<sub>t</sub>**. So for example, the agent could move from state **s<sub>t</sub> = (1,2)** to **s<sub>(t+1)</sub> = (1,3)** by choosing the action **a<sub>t</sub> = Right**. Choosing the best action from the possible choices is the problem that reinforcement learning solves. In order to do this, the learning agent must formulate a policy that chooses actions at each state so as to reach the exit, at time **t = T**,  in the most efficient way. To differentiate between a 'good' action and a 'bad' action in terms of this goal, a reward signal **r<sub>(t+1)</sub>** is received from the environment after each action, which will be -1 in this model, **r<sub>(t+1)</sub> = -1**.  The motivation for using this reward signal is that a route which backtracks or takes unnecessary turns is penalised, whilst taking the shortest path is rewarded. A reward of +10 is also given for reaching the goal location, **r<sub>t=T</sub> = 10**, which motivates the agent to prefer actions which lead to that location state.

