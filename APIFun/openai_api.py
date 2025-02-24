# @author Gina Sprint
# Get Genre for Searched Artist Name
# Get API key: https://platform.openai.com/docs/quickstart
# NOTE: using OpenAI models costs $! The GU CS dept has API credits students can
# use for class and educational side projects
# Create chat completion: https://platform.openai.com/docs/api-reference/chat

import requests
# import json # needed if using json.loads(response.text)
# code below uses response.json() instead

# TODO: move API key into a file/environment variable external to the code
api_key = "YOUR API KEY HERE" 
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
body = {
    "model": "gpt-4o-mini",
    "messages": [
      {
        "role": "developer",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "What do you know about CPSC 222 at Gonzaga University?"
      }
    ]
}
response = requests.post(url, headers=headers, json=body)
# print(response.text)
json_obj = response.json() # alternative to json.loads(response.text)
choice = json_obj["choices"][0]
msg_content = choice["message"]["content"]
print("Chat response:", msg_content)