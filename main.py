from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()


class ResearchAgent:
    def __init__(self, topic):
        self.topic = topic

    def research(self):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a research assistant."},
                {"role": "user", "content": f"Research about {self.topic}"}
            ],
            stream=True,
        )
        completion_string = ""
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                completion_string += chunk.choices[0].delta.content
        
        return completion_string

class SummaryAgent:
    def __init__(self, content):
        self.content = content

    def summarize(self):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a summarizer."},
                {"role": "user", "content": f"Summarize the following content: {self.content}"}
            ],
            stream=True
        )
        completion_string = ""
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                completion_string += chunk.choices[0].delta.content
        
        return completion_string

def main():
    topic = "Artificial Intelligence"
    
    # Araştırma ajanı oluştur
    research_agent = ResearchAgent(topic)
    research_content = research_agent.research()
    print(f"Research Content: {research_content}")

    # Özet ajanı oluştur
    summary_agent = SummaryAgent(research_content)
    summary = summary_agent.summarize()
    print(f"Summary: {summary}")



if __name__ == "__main__":
    main()

    