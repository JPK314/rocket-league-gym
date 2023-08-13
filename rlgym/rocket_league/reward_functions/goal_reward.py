from typing import List, Dict, Any

from rlgym.api.config.reward_function import RewardFunction
from rlgym.api.typing import AgentID
from rlgym.rocket_league.engine.game_state import GameState


class GoalReward(RewardFunction[AgentID, GameState, float]):
    def reset(self, initial_state: GameState, shared_info: Dict[str, Any]) -> None:
        pass

    def get_rewards(self, agents: List[AgentID], state: GameState, is_terminated: Dict[AgentID, bool],
                    is_truncated: Dict[AgentID, bool], shared_info: Dict[str, Any]) -> Dict[AgentID, float]:
        return {agent: self._get_reward(agent, state) for agent in agents}

    def _get_reward(self, agent: AgentID, state: GameState) -> float:
        if state.goal_scored:
            return 1 if state.scoring_team == state.cars[agent].team_num else -1
        else:
            return 0
