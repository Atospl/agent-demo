from openai import AsyncOpenAI
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider


client = AsyncOpenAI(base_url="http://localhost:1234/v1", api_key="lm_studio")
model = OpenAIModel(model_name="qwq-32b", provider=OpenAIProvider(openai_client=client))

agent = Agent(model=model)

def main():
    print("Hello from agentdemo!")
    result_sync = agent.run_sync('What is the capital of Italy?')
    print(result_sync.output)


if __name__ == "__main__":
    main()
