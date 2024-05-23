import requests, json

class SiCl:
    def __init__(self, api_key, model="gpt-3.5"):
        self.api_key = api_key
        self.model = model
        self.url = 'https://api.openai.com/v1/chat/completions'
        self.headers = {
            'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'
            }
        self.conversation_history = [
            {"role": "system", "content": "You are Jarvis, a personal assistant."}
        ]
        self.load_conversation_history()
        
    def save_conversation_history(self, filename='conversation_history.json'):
        with open(filename, 'w') as file:
            json.dump(self.conversation_history, file, indent=4)

    def load_conversation_history(self, filename='conversation_history.json'):
        try:
            with open(filename, 'r') as file:
                self.conversation_history = json.load(file)
        except FileNotFoundError:
            self.conversation_history = [
                {"role": "system", "content": "You are Jarvis, a personal assistant."}
            ]
    
    def send_message(self, user_message):
        self.conversation_history.append({"role": "user", "content": user_message})
        recent_conversation = self.conversation_history[-9:]
        payload = {
            'model': self.model,
            'messages': recent_conversation
        }
        response = requests.post(self.url, headers=self.headers, json=payload)

        if response.status_code == 200:
            response_data = response.json()
            assistant_message = response_data['choices'][0]['message']['content']
            self.conversation_history.append({"role": "assistant", "content": assistant_message})
            self.save_conversation_history
            return assistant_message
        else:
            return f"The request failed with status code {response.status_code}: {response.text}"
