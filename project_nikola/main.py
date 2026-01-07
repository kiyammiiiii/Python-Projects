from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.agents import create_react_agent


load_dotenv()

def main():
    model = ChatOpenAI(temperature=0)

    tools = []
    agent_executor = create_react_agent(model, tools)

    print("Welcome I am Nikola your AI assistant. Type 'exit' to quit.")
    print("How shall I assist you stupid human today?")
    
    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower().strip() == 'exit':
            print("Goodbye!")
            break
        
        print("\nNikola: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]} #pass message to the agent
        ):
           #stream long responses
           if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]: #loop through the messages
                    print(message.content, end="")
        print()  # New line after the response

if __name__ == "__main__":
    main()
