import random

# Define topics and templates
topics = {
    "Technology": ["AI", "social media", "smartphones", "cybersecurity"],
    "Education": ["online learning", "homework", "grading", "school policies"],
    "Health": ["diet", "exercise", "mental health", "healthcare access"],
    "Environment": ["climate change", "recycling", "pollution", "energy use"]
}

templates = [
    "What is your opinion on {topic}?",
    "How often do you engage with {topic}?",
    "How satisfied are you with {topic}?",
    "What changes would you like to see regarding {topic}?",
    "How important is {topic} to you?"
]

def generate_question(category=None):
    if category is None or category not in topics:
        category = random.choice(list(topics.keys()))
    chosen_topic = random.choice(topics[category])
    template = random.choice(templates)
    return template.format(topic=chosen_topic)

def generate_multiple_questions(n=5, category=None):
    return [generate_question(category) for _ in range(n)]

# Example usage
if __name__ == "__main__":
    print("Generated Survey Questions:\n")
    questions = generate_multiple_questions(5)
    for idx, q in enumerate(questions, 1):
        print(f"{idx}. {q}")
