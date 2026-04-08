from clear_env.env import ClearEnv

env = ClearEnv()

obs = env.reset()
done = False
total_reward = 0

while not done:
    action = {
        "action_type": "respond",
        "content": "billing issue resolved using tool"
    }

    obs, reward, done, info = env.step(action)
    total_reward += reward

    print("Step Reward:", reward)

print("Final Score:", total_reward)
