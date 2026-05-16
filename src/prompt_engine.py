def build_prompt(topic, stance):

    if stance == "for":
        return f"Argue in favor of: {topic}"

    return f"Argue against: {topic}"
