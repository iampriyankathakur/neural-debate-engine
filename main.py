from src.debate_manager import DebateManager
from app.interface import display_debate

def load_topics():

    with open("data/topics.txt", "r") as f:
        topics = [line.strip() for line in f.readlines()]

    return topics

def main():

    topics = load_topics()

    print("\nAvailable Topics:\n")

    for idx, topic in enumerate(topics):
        print(f"{idx+1}. {topic}")

    choice = int(input("\nSelect topic number: ")) - 1

    selected_topic = topics[choice]

    manager = DebateManager()

    debate = manager.run_debate(selected_topic)

    display_debate(debate)

if __name__ == "__main__":
    main()
