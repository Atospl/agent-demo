import logfire

from ai_assistant.agents import agent

logfire.configure()
logfire.instrument_httpx(capture_all=True)


def main():
    print("Hello from agentdemo!")
    result_sync = agent.run_sync("What is the capital of Italy?")
    print(result_sync.output)


if __name__ == "__main__":
    main()
