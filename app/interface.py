from rich.console import Console
from rich.panel import Panel

console = Console()

def display_debate(debate):

    console.print(
        Panel(
            debate["topic"],
            title="📌 Debate Topic"
        )
    )

    console.print(
        Panel(
            debate["argument_a"],
            title="🟢 Agent A"
        )
    )

    console.print(
        Panel(
            debate["argument_b"],
            title="🔴 Agent B"
        )
    )

    results = debate["results"]

    summary = (
        f"Winner: {results['winner']}\n"
        f"Reason: {results['reason']}\n\n"
        f"Agent A Score: {results['score_a']:.3f}\n"
        f"Agent B Score: {results['score_b']:.3f}"
    )

    console.print(
        Panel(
            summary,
            title="⚖️ Judge Decision"
        )
    )
