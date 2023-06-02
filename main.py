import openai
import sqlite3
from key import openai_key
from gpytranslate import SyncTranslator

t = SyncTranslator()

conn = sqlite3.connect('yulia.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS ChatWithYulia
                (id INTEGER PRIMARY KEY, 
                name TEXT NOT NULL, 
                message TEXT NOT NULL)''')

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

    cursor.execute("INSERT INTO ChatWithYulia (name, message) VALUES (?, ?)", ('Lubomyr', user_message))

    if user_message == "exit":
        conn.close()
        break

    with open("memory.txt", 'a') as f:
        f.write(f"\nLubomyr: {user_message}")

    with open("memory.txt", 'r') as f:
        memory = f.read()

    Yulia_message = Yulia_Bot(memory)

    cursor.execute("INSERT INTO ChatWithYulia (name, message) VALUES (?, ?)", ('Yulia', Yulia_message))

    conn.commit()


    with open("memory.txt", 'a') as f:
        f.write(f"\n{Yulia_message}")

    print(f"\n{Yulia_message}")

