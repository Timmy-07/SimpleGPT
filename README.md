# SimpleGPT

Example
-------

from SimpleGPT import SiCl

api_key = 'your_api_key_here'
model = 'AI model here' # default is 3.5 turbo #
client = SiCl(api_key, model)

response = client.send_message("Hello, how are you?") 
print(f"Response: {response}")

------
