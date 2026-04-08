import random
from clear_env.tasks import TASKS
from clear_env.models import Observation, Action
from clear_env.grader import grade


class ClearEnv:

    def __init__(self):
        self.task = None
        self.history = []
        self.done = False

    def reset(self):
        self.task = random.choice(TASKS)
        self.history = []
        self.done = False
        self.step_count = 0

        return Observation(
            user_query=self.task["query"],
            history=[],
            available_tools=["check_order", "issue_refund"],
        )

    def step(self, action_dict):
        action = Action(**action_dict)
        self.history.append(action_dict)

        if not hasattr(self, "step_count"):
            self.step_count = 0
        self.step_count += 1

        reward = 0.0

        if self.step_count == 1:
            if self.task["intent"] in action.content.lower():
                reward += 0.2
        elif self.step_count == 2:
            if action.action_type == "call_tool":
                reward += 0.3
        elif self.step_count == 3:
            if "resolved" in action.content.lower():
                reward += 0.5
            self.done = True

        observation = Observation(
            user_query=self.task["query"],
            history=[str(a) for a in self.history],
            available_tools=["check_order", "issue_refund"],
        )

        return observation, reward, self.done, {"task_id": self.task["id"]}

    def close(self):
        pass

    def state(self):
        return {"task": self.task, "history": self.history}
