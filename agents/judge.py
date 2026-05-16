from src.scorer import semantic_similarity_score

class DebateJudge:

    def evaluate(self, topic, arg_a, arg_b):

        score_a = semantic_similarity_score(topic, arg_a)
        score_b = semantic_similarity_score(topic, arg_b)

        if score_a > score_b:
            winner = "Agent A"
            reason = "Higher semantic coherence."
        elif score_b > score_a:
            winner = "Agent B"
            reason = "More relevant reasoning."
        else:
            winner = "Tie"
            reason = "Arguments equally strong."

        return {
            "winner": winner,
            "reason": reason,
            "score_a": score_a,
            "score_b": score_b
        }
