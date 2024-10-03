import os
from openai import AzureOpenAI

client = AzureOpenAI(
  api_key =  '1dbfa09c501745538a844b4c35aad652',  
  api_version = "2024-02-01",
  azure_endpoint = 'https://deepaklabs.openai.azure.com/'
)

conversation=[{"role": "system", "content": "You are a helpful assistant."}]

while True:
    user_input = input("Q:")      
    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model = 'gpt-4o',
        messages=conversation
    )

    conversation.append({"role": "assistant", "content": response.choices[0].message.content})
    print("\n" + response.choices[0].message.content + "\n")