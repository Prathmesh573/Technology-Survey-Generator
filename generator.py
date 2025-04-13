import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_scenario(player_name):
    prompt = f"""
    You are a game master. Create an imaginative scenario in a fantasy world for a player named {player_name}. 
    Present 2 options for them to choose from. Be descriptive but concise.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']
