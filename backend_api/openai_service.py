from openai import OpenAI
import os
from dotenv import load_dotenv


class openai_service:
    
    message_history = [
        {
            "role": "developer",
            "content": "Talk like a doctor. "
        }
        
    ]
    def __init__(self):
        self.client = OpenAI(api_key = os.getenv('GITHUB_API'),base_url= os.getenv('BASE_URL'))
        
    
    def make_response(self,input):
        self.message_history.append({
                    "role": "user",
                    "content": input,
                })
        
        response = self.client.chat.completions.create(
            messages=self.message_history,
            model="gpt-4o",
            temperature=1,
            max_tokens=500,
            top_p=1
        )
        
        self.message_history.append(response.choices[0].message)
        return response.choices[0].message.content
    
        
        
        
 
model = openai_service()
i = 0

while i <= 5:
    inp = input('Make prompt: ')
    print(model.make_response(inp))
    print(model.message_history)
    print('\n','\n','\n','\n')
    i+=1

