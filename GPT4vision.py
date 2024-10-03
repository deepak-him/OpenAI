from openai import AzureOpenAI

api_base = 'https://deepaklabs.openai.azure.com/'
api_key= ''
deployment_name = 'gpt-4'
api_version = '2023-12-01-preview' # this might change in the future

client = AzureOpenAI(
    api_key=api_key,  
    api_version=api_version,
    base_url=f"{api_base}/openai/deployments/{deployment_name}"
)

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        { "role": "system", "content": "You are a helpful assistant." },
        { "role": "user", "content": [  
            { 
                "type": "text", 
                "text": "Describe this person in the picture:" 
            },
            { 
                "type": "image_url",
                "image_url": {
                    "url": "https://i.pinimg.com/originals/88/b8/6d/88b86ded3484fd59bbbe1e39aabbca80.jpg"
                }
            }
        ] } 
    ],
    max_tokens=2000 
)

print(response)
