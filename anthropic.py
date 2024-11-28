import anthropic 

model="claude-3-5-sonnet-20241022"

def txt_string(filename:str):
    file_path = f"{filename}.txt"
    with open(file_path, 'r') as file:
        return file.read()

class AnthropicDoc:
    def __init__(self, doc, model: str, max_tokens: int, messages: list):
        self.role = "User"
        self.system_prompt = txt_string("system_prompt")
        self.model = model
        self.doc = doc
        self.max_tokens = max_tokens
        self.questions = messages
    

    def send_message(self, messages):
        client = anthropic.Anthropic()
        message = client.messages.create(
            model = self.model,
            max_tokens = self.max_tokens,
            temperature = 0,
            system = self.system_prompt,
            messages = messages
        )
    
    def cache_prompt(self):
        pass
