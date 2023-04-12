from dotenv import load_dotenv
import openai
import os
import sys


class Cmd_Search_GPT:
    def __init__(self, prompt):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.prompt = " ".join(prompt)
        self.send_request()
        self.parse_response()

    def send_request(self):
        openai.api_key = self.api_key
        self.request = openai.Completion.create(engine="text-davinci-003",
                                                prompt=self.prompt,
                                                max_tokens=1024,
                                                n=1,
                                                stop=None,
                                                temperature=0.5)

    def parse_response(self):
        response = self.request.choices[0].text
        print(response)
        print("\n")


obj = Cmd_Search_GPT(sys.argv[1:])
