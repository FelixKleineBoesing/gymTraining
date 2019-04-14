import sys
import numpy as np
import gym
from mdp import MDP, FrozenLakeEnv
import grading
sys.path.append("..")


def submit_interface(policy, email, token):
    TIME_LIMIT = 250
    env = gym.wrappers.TimeLimit(gym.envs.classic_control.MountainCarEnv(),
                                max_episode_steps=TIME_LIMIT + 1)
    s = env.reset()
    actions = {'left': 0, 'stop': 1, 'right': 2}

    for t in range(TIME_LIMIT):
        s, r, done, _ = env.step(policy(s, t))
        if done:
            break
    else:
        s = [-1]
    grader = grading.Grader("3T7pSSz0EeifGhJb4HAv7A")
    grader.set_answer("sDilm", s[0])
    grader.submit(email, token)


def submit_taxi(generate_session, policy, email, token):
    sessions = [generate_session(policy) for _ in range(100)]
    _, _, session_rewards = zip(*sessions)
    session_rewards = np.array(session_rewards)
    grader = grading.Grader("s4pTlNbTEeeQvQ7N1-Sa3A")
    grader.set_answer("GsMSL", np.mean(session_rewards))
    grader.submit(email, token)


def submit_mountain_car(generate_session, email, token):
    sessions = [generate_session() for _ in range(100)]
    _, _, session_rewards = zip(*sessions)
    session_rewards = np.array(session_rewards)
    grader = grading.Grader("EyYJW9bUEeeXyQ5ZPWKHGg")
    grader.set_answer("mXDUE", np.mean(session_rewards))
    grader.submit(email, token)

def submit_bandits(agents, scores, email, token):
    epsilon_greedy_agent = None
    ucb_agent = None
    thompson_sampling_agent = None

    for agent in agents:
        if "EpsilonGreedyAgent" in agent.name:
            epsilon_greedy_agent = agent.name
        if "UCBAgent" in agent.name:
            ucb_agent = agent.name
        if "ThompsonSamplingAgent" in agent.name:
            thompson_sampling_agent = agent.name

    assert epsilon_greedy_agent is not None
    assert ucb_agent is not None
    assert thompson_sampling_agent is not None

    grader = grading.Grader("VL9tBt7zEeewFg5wtLgZkA")
    grader.set_answer(
        "YQLYE",
        (int(scores[epsilon_greedy_agent][int(1e4) - 1]) -
         int(scores[epsilon_greedy_agent][int(5e3) - 1])))

    grader.set_answer(
        "FCHOZ",
        (int(scores[epsilon_greedy_agent][int(1e4) - 1]) -
         int(scores[ucb_agent][int(1e4) - 1])))

    grader.set_answer(
        "0JWHl",
        (int(scores[epsilon_greedy_agent][int(5e3) - 1]) -
         int(scores[ucb_agent][int(5e3) - 1])))

    grader.set_answer(
        "4rH5M",
        (int(scores[epsilon_greedy_agent][int(1e4) - 1]) -
         int(scores[thompson_sampling_agent][int(1e4) - 1])))

    grader.set_answer(
        "TvOqm",
        (int(scores[epsilon_greedy_agent][int(5e3) - 1]) -
         int(scores[thompson_sampling_agent][int(5e3) - 1])))

    grader.submit(email, token)


def submit_mcts(total_reward, email, token):
    grader = grading.Grader("Giz88DiCEei4TA70mSDOBg")
    grader.set_answer("L1HgT", int(total_reward))
    grader.submit(email, token)

def submit_cartpole(generate_session, email, token):
    sessions = [generate_session() for _ in range(100)]
    session_rewards = np.array(sessions)
    grader = grading.Grader("oyT3Bt7yEeeQvhJmhysb5g")
    grader.set_answer("7QKmA", int(np.mean(session_rewards)))
    grader.submit(email, token)


def submit_kungfu(agent, env, evaluate, email, token):
    sessions = [evaluate(agent=agent, env=env, n_games=1) for _ in range(100)]
    session_rewards = np.array(sessions)
    grader = grading.Grader("6sPnVCn6EeieSRL7rCBNJA")
    grader.set_answer("HhNVX", int(np.mean(session_rewards)))
    grader.submit(email, token)

def submit_cartpole(generate_session, email, token):
    sessions = [generate_session() for _ in range(100)]
    session_rewards, _, _ = map(np.array, zip(*sessions))
    grader = grading.Grader("RDofv-QXEeeaGw6kpIOf3g")
    grader.set_answer("NRNkl", int(np.mean(session_rewards)))
    grader.submit(email, token)

def submit_experience_replay(rewards_replay, rewards_baseline, email, token):
    flag1 = np.mean(rewards_replay[:100]) - np.mean(rewards_baseline[:100])
    flag2 = np.mean(rewards_replay[-100:])
    flag3 = np.mean(rewards_baseline[-100:])

    grader = grading.Grader("XUt-8d7yEee8nwq8KJgXXg")
    grader.set_answer("iEQwT", flag1)
    grader.set_answer("8N1Wm", flag2)
    grader.set_answer("F0Am8", flag3)

    grader.submit(email, token)


def submit_qlearning(rewards_q1, rewards_q2, email, token):
    grader = grading.Grader("XbjcGd7xEeeDzRKutDCmyA")

    flag1 = np.mean(rewards_q1[-10:])
    grader.set_answer("5NB4z", flag1)

    flag2 = np.mean(rewards_q2[-10:])
    grader.set_answer("CkyJ4", flag2)

    grader.submit(email, token)


def submit_sarsa(rewards_ql, rewards_sarsa, email, token):
    flag1 = np.mean(rewards_ql[-100:])
    flag2 = np.mean(rewards_sarsa[-100:])
    flag3 = np.mean(rewards_sarsa[-100:]) - np.mean(rewards_ql[-100:])

    grader = grading.Grader("pazQX97xEee_JA6t1Myltg")
    grader.set_answer("ZarWJ", flag1)
    grader.set_answer("izJi4", flag2)
    grader.set_answer("frgbU", flag3)

    grader.submit(email, token)


def submit_breakout(agent, env, evaluate, email, token):
    sessions = [evaluate(env, agent, n_games=1) for _ in range(100)]
    session_rewards = np.array(sessions)
    grader = grading.Grader("WTOZHCn1EeiNwAoZNi-Hrg")
    grader.set_answer("VFM7Z", int(np.mean(session_rewards)))
    grader.submit(email, token)

def submit_experience_replay(rewards_replay, rewards_baseline, email, token):
    flag1 = np.mean(rewards_replay[:100]) - np.mean(rewards_baseline[:100])
    flag2 = np.mean(rewards_replay[-100:])
    flag3 = np.mean(rewards_baseline[-100:])

    grader = grading.Grader("XUt-8d7yEee8nwq8KJgXXg")
    grader.set_answer("iEQwT", flag1)
    grader.set_answer("8N1Wm", flag2)
    grader.set_answer("F0Am8", flag3)

    grader.submit(email, token)


def submit_qlearning(rewards_q1, rewards_q2, email, token):
    grader = grading.Grader("XbjcGd7xEeeDzRKutDCmyA")

    flag1 = np.mean(rewards_q1[-10:])
    grader.set_answer("5NB4z", flag1)

    flag2 = np.mean(rewards_q2[-10:])
    grader.set_answer("CkyJ4", flag2)

    grader.submit(email, token)


def submit_sarsa(rewards_ql, rewards_sarsa, email, token):
    flag1 = np.mean(rewards_ql[-100:])
    flag2 = np.mean(rewards_sarsa[-100:])
    flag3 = np.mean(rewards_sarsa[-100:]) - np.mean(rewards_ql[-100:])

    grader = grading.Grader("pazQX97xEee_JA6t1Myltg")
    grader.set_answer("ZarWJ", flag1)
    grader.set_answer("izJi4", flag2)
    grader.set_answer("frgbU", flag3)

    grader.submit(email, token)

def submit_assigment(
        get_action_value,
        get_new_state_value,
        get_optimal_action,
        value_iteration,
        email,
        token):
    grader = grading.Grader("EheZDOgLEeenIA4g5qPHFA")
    sys.stdout = None

    transition_probs = {
        's0': {
            'a0': {'s1': 0.8, 's2': 0.2},
            'a1': {'s1': 0.2, 's2': 0.8},
        },
        's1': {
            'a0': {'s0': 0.2, 's2': 0.8},
            'a1': {'s0': 0.8, 's2': 0.2},
        },
        's2': {
            'a0': {'s3': 0.5, 's4': 0.5},
            'a1': {'s3': 1.0},
        },
        's3': {
            'a0': {'s1': 0.9, 's2': 0.1},
            'a1': {'s1': 0.7, 's2': 0.3},
        },
        's4': {
            'a0': {'s3': 1.0},
            'a1': {'s3': 0.7, 's1': 0.3},
        }
    }
    rewards = {
        's0': {'a0': {'s1': 0, 's2': 1}, 'a1': {'s1': 0, 's2': 1}},
        's1': {'a0': {'s0': -1, 's2': 1}, 'a1': {'s0': -1, 's2': 1}},
        's2': {'a0': {'s3': 0, 's4': 1}, 'a1': {'s3': 0, 's4': 1}},
        's3': {'a0': {'s1': -3, 's2': -3}, 'a1': {'s1': -3, 's2': -3}},
        's4': {'a1': {'s1': +10}}
    }

    mdp = MDP(transition_probs, rewards, initial_state='s0')

    test_Vs = {s: i for i, s in enumerate(sorted(mdp.get_all_states()))}
    qvalue1 = get_action_value(mdp, test_Vs, 's1', 'a0', 0.9)
    qvalue2 = get_action_value(mdp, test_Vs, 's4', 'a1', 0.9)

    grader.set_answer("F16dC", qvalue1 + qvalue2)

    # ---

    svalue1 = get_new_state_value(mdp, test_Vs, 's2', 0.9)
    svalue2 = get_new_state_value(mdp, test_Vs, 's4', 0.9)

    grader.set_answer("72cBp", svalue1 + svalue2)

    # ---

    state_values = {s: 0 for s in mdp.get_all_states()}
    gamma = 0.9

    # ---

    action1 = get_optimal_action(mdp, state_values, 's1', gamma)
    action2 = get_optimal_action(mdp, state_values, 's2', gamma)

    grader.set_answer("xIuti", action1 + action2)

    # ---

    s = mdp.reset()
    rewards = []
    for _ in range(10000):
        s, r, done, _ = mdp.step(get_optimal_action(mdp, state_values, s, gamma))
        rewards.append(r)

    grader.set_answer("Y8g0j", np.mean(rewards) + np.std(rewards))

    mdp = FrozenLakeEnv(slip_chance=0.25)
    state_values = value_iteration(mdp)
    gamma = 0.9

    total_rewards = []
    for game_i in range(1000):
        s = mdp.reset()
        rewards = []
        for t in range(100):
            s, r, done, _ = mdp.step(get_optimal_action(mdp, state_values, s, gamma))
            rewards.append(r)
            if done: break
        total_rewards.append(np.sum(rewards))

    grader.set_answer("ABf1b", np.mean(total_rewards) + np.std(total_rewards))

    # ---

    mdp = FrozenLakeEnv(slip_chance=0.25, map_name='8x8')
    state_values = value_iteration(mdp)
    gamma = 0.9

    total_rewards = []
    for game_i in range(1000):
        s = mdp.reset()
        rewards = []
        for t in range(100):
            s, r, done, _ = mdp.step(get_optimal_action(mdp, state_values, s, gamma))
            rewards.append(r)
            if done: break
        total_rewards.append(np.sum(rewards))

    grader.set_answer("U3RzE", np.mean(total_rewards) + np.std(total_rewards))

    sys.stdout = sys.__stdout__
    grader.submit(email, token)

