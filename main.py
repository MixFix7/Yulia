import openai
from key import openai_key


openai.api_key = openai_key


def gpt_bot(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        promt=message,
        temperature=0.25,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    ai_answer = response['choices'][0]['text']
    return ai_answer






