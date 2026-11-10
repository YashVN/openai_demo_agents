from dotenv import load_dotenv
import os 
from agents import Agent, Runner, SQLiteSession 
from calc_tools import add,sub,mul,div,modulus 

def main(session_id = "Session_1"):
    session  = SQLiteSession(session_id = session_id,
                             db_path = "calculator_memory.db")
    MODEL_NAME = os.getenv('OPENAI_MODEL', 'gpt-5.6-luna')
    agent = Agent(
        name = "Smart Calculator",
        tools = [add,sub,mul,div,modulus],
        model = MODEL_NAME,
        instructions = ''' You are a helpful calculator tool

    Understand Mathemetics questions in natural language.

    Always use the provided calculator tools for arthemetic operations

    Use appropritate tools for addition, subtraction, multiplication, division or modulus

    Explain the final answer simply'''
    )
    result = Runner.run_sync(agent,"I have 5 apples",
    session = session)

    print(result.final_output)
    result = Runner.run_sync(
        agent,
        "I have bought 20 more apples, how many apples do I have now?",
        session = session
    )
    print(result.final_output)

if __name__ == '__main__':
    load_dotenv()
    main()

    