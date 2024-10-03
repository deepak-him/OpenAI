# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
import os
from openai import AzureOpenAI
import json
import requests
from PIL import Image


client = AzureOpenAI(
    api_version="2024-05-01-preview",
    azure_endpoint="https://deepaklabs.openai.azure.com/",
    api_key='1dbfa09c501745538a844b4c35aad652',
)

result = client.images.generate(
    model="dall-e", # the name of your DALL-E 3 deployment
    prompt="create an army official pic od msdhoni infront of indian flag",
    n=1
)

# image_url = json.loads(result.model_dump_json())['data'][0]['url']
json_response = json.loads(result.model_dump_json())

# Set the directory for the stored image
image_dir = os.path.join(os.curdir, 'images')

# If the directory doesn't exist, create it
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

# Initialize the image path (note the filetype should be png)
image_path = os.path.join(image_dir, 'generated_image.png')

# Retrieve the generated image
image_url = json_response["data"][0]["url"]  # extract image URL from response
generated_image = requests.get(image_url).content  # download the image
with open(image_path, "wb") as image_file:
    image_file.write(generated_image)

# Display the image in the default image viewer
image = Image.open(image_path)
image.show()

