import uuid
import ollama
import json
from database.database import init_db, create_session, save_message, get_messages

with open("config.json", "r") as f:
    config = json.load(f)

init_db()

session_id = str(uuid.uuid4())
create_session(session_id)

MODEL = config["model"]
SYSTEM_PROMPT = config["system_prompt"]

while True:
    user_input = input("You: ")

    # exit condition
    if user_input.lower() in ["exit", "bye", "quit"]:
        print("AI: Goodbye 👋")
        break

    # save user message
    save_message(session_id, "user", user_input)

    # load full memory
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages += get_messages(session_id, Limit=4)
    print(get_messages(session_id, Limit=5))

    # call ollama
    response = ollama.chat(
        model=MODEL,
        messages=messages
    )

    

    ai_response = response["message"]["content"]

    # save AI response
    save_message(session_id, "assistant", ai_response)

    # print(f"AI: {ai_response}\n")
