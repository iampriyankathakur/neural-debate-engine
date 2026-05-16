from agents.debater import DebaterAgent
from agents.judge import DebateJudge

class DebateManager:

    def __init__(self):
        self.agent_a = DebaterAgent("Agent A", "for")
        self.agent_b = DebaterAgent("Agent B", "against")
        self.judge = DebateJudge()

    def run_debate(self, topic):

        argument_a = self.agent_a.generate_argument(topic)
        argument_b = self.agent_b.generate_argument(topic)

        results = self.judge.evaluate(
            topic,
            argument_a,
            argument_b
        )

        return {
            "topic": topic,
            "argument_a": argument_a,
            "argument_b": argument_b,
            "results": results
        }
