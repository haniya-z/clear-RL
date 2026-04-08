# inference.py

# Import your real environment
from clear_env.env import ClearEnv
 # adjust if your path is different


# -------------------------------
# Rule-Based Agent (Starter)
# -------------------------------
class RuleAgent:
    def __init__(self):
        self.step_count = 0

    def act(self, obs):
        """
        Very simple logic:
        - Analyze the query and respond accordingly
        """

        self.step_count += 1
        query = obs.user_query.lower()

        if "payment" in query or "charged" in query:
            content = "billing issue resolved"
        elif "refund" in query:
            content = "refund processed"
        elif "support" in query or "didn't help" in query:
            content = "escalation handled"
        else:
            content = "issue resolved"

        if self.step_count == 2:
            return {"action_type": "call_tool", "content": content}
        else:
            return {"action_type": "respond", "content": content}


# -------------------------------
# Main Execution
# -------------------------------
def main():
    task = "clear-env-task"
    env_name = "clear-env"
    model_name = "rule-based-v1"

    env = ClearEnv()
    agent = RuleAgent()

    rewards = []
    success = False
    step = 0

    # START
    print(f"[START] task={task} env={env_name} model={model_name}")

    try:
        obs = env.reset()

        while True:
            step += 1

            action = agent.act(obs)

            try:
                obs, reward, done, info = env.step(action)
                error = "null"
            except Exception as e:
                reward = 0.0
                done = True
                error = str(e)

            rewards.append(f"{reward:.2f}")

            # STEP
            print(
                f"[STEP] step={step} action={action} "
                f"reward={reward:.2f} done={str(done).lower()} error={error}"
            )

            if done:
                success = reward > 0
                break

    except Exception:
        success = False

    finally:
        env.close()

        # END (ALWAYS PRINT)
        print(
            f"[END] success={str(success).lower()} "
            f"steps={step} rewards={','.join(rewards)}"
        )


# -------------------------------
# Entry Point
# -------------------------------
if __name__ == "__main__":
    main()
