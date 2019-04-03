import matplotlib.pyplot as plt
import gym
env = gym.make("MountainCar-v0")

plt.imshow(env.render('rgb_array'))
print("Observation space:", env.observation_space)
print("Action space:", env.action_space)

obs0 = env.reset()
print("initial observation code:", obs0)

print("taking action 2 (right)")
new_obs, reward, is_done, _ = env.step(2)

print("new observation code:", new_obs)
print("reward:", reward)
print("is game over?:", is_done)


# create env manually to set time limit. Please don't change this.
TIME_LIMIT = 250
env = gym.wrappers.TimeLimit(gym.envs.classic_control.MountainCarEnv(),
                             max_episode_steps=TIME_LIMIT + 1)
s = env.reset()
actions = {'left': 0, 'stop': 1, 'right': 2}

# prepare "display"
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()
plt.show(block=True)
def policy(s, t):
    print(s)
    print(t)
    if s[0] > -0.4301 and s[1] > 0:
        print("right")
        return actions["right"]
    elif s[0] > -0.4301 and s[1] < 0:
        print("left")
        return actions["left"]
    elif s[0] < -0.4301 and s[1] < 0:
        print("left")
        return actions["left"]
    elif s[0] < -0.4301 and s[1] > 0:
        print("rigth")
        return actions["right"]
    else:
        print("right")
        return actions["right"]
    
for t in range(TIME_LIMIT):
    
    s, r, done, _ = env.step(policy(s, t))
    
    #draw game image on display
    ax.clear()
    ax.imshow(env.render('rgb_array'))
    fig.canvas.draw()
    
    if done:
        print("Well done!")
        break
else:    
    print("Time limit exceeded. Try again.")





