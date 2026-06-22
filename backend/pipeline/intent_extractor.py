from openai import OpenAI
import json

client = OpenAI()

def extract_intent(prompt):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role":"system",
                "content":"Extract app requirements and return JSON only."
            },
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return json.loads(
        response.choices[0].message.content
    )
