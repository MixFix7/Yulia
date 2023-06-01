import openai
from key import openai_key

openai.api_key = openai_key


def Yulia_Bot(history):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=history,
        temperature=0.25,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=[" Lubomyr:", " Yulia:"]
    )
    ai_answer = response['choices'][0]['text']
    return ai_answer


while True:
    user_message = input("> ")

    if user_message == "exit":
        break

    with open("memory.txt", 'a') as f:
        f.write(f"\nLubomyr: {user_message}")

    with open("memory.txt", 'r') as f:
        memory = f.read()

    Yulia_message = Yulia_Bot(memory)

    with open("memory.txt", 'a') as f:
        f.write(f"\n{Yulia_message}")

    print(f"\n{Yulia_message}")

