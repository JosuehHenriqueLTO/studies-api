from openai import OpenAI

from key import API_KEY

client = OpenAI(api_key=API_KEY)


def talking(message):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": "Olá, fico muito contente em ajudar em qualquer que seja o assunto!"},
            {"role": "user", "content": message}
        ]
    )
    return completion.choices[0].message


print(talking("Tempo tá bom aí?"))
