import gym
import gym_maze
import numpy as np
import time


from GLIE_MC import MC_agent

env = gym.make('maze-random-30x30-plus-v0')
agent = MC_agent(env, 0.99, 0.02, 0.9, 0.999)
min_eps = 0.1
r = []
n_episodes = 1000
for n in range(1, n_episodes + 1):
    episode = agent.play_episode()
    _, _, rewards = zip(*episode)
    r.append(np.mean(rewards))
    if n%10 == 0:
        template = 'Episode: {}/{}, Rewards: {}, Epsilon: {}'
        print(template.format(n, n_episodes, np.mean(r), agent.eps))
        r = []
    agent.update_knowledge(episode)
    agent.eps = max(min_eps, agent.eps_step * agent.eps) 
for n in range(10):
    agent.play_episode(show=True, delay=0.06)

