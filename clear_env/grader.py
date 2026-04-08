def grade(task, action_history):
    score = 0.0

    last_action = action_history[-1] if action_history else {}

    if task["intent"] in last_action.get("content", ""):
        score += 0.4

    if "tool" in last_action.get("content", ""):
        score += 0.3

    if "resolved" in last_action.get("content", ""):
        score += 0.3

    return min(score, 1.0)
