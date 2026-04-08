from pydantic import BaseModel
from typing import List, Literal, Optional


class Observation(BaseModel):
    user_query: str
    history: List[str]
    available_tools: List[str]


class Action(BaseModel):
    action_type: Literal["respond", "call_tool", "route"]
    content: str


class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: dict
