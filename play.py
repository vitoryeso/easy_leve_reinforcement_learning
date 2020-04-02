import gym
import gym_maze
import numpy as np
import time


from GLIE_MC import MC_agent

env = gym.make('maze-random-30x30-plus-v0')
agent = MC_agent(env, 1.0, 0.02, 1, 0.2)

r = []
n_episodes = 1000
for n in range(1, n_episodes + 1):
    agent.eps = 0.8 if n < 900 else 0.1
    episode = agent.play_episode()
    _, _, rewards = zip(*episode)
    r.append(np.mean(rewards))
    if n%10 == 0:
        template = 'Episode: {}/{}, Rewards: {}, Epsilon: {}'
        print(template.format(n, n_episodes, np.mean(r), agent.eps))
        r = []
    agent.update_knowledge(episode)
for n in range(10):
    agent.play_episode(show=True, delay=0.06)

