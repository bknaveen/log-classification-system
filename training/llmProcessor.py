from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables.
load_dotenv()

# Retrieve the API key from the environment.
api_key = os.getenv("GroqAPIKey")


# Ensure the API key is loaded properly.
if not api_key:
    raise ValueError("The GROQ_API_KEY environment variable is not set.")

# Initialize the Groq client with the API key.
gq = Groq(api_key=api_key)

# To call the LLM
def classify_with_llm(log_message):
    prompt = f'''Classify the log message into one of these categories: 
    (1) Workflow Error, (2) Deprecation Warning.
    put those categories into <category></category> tags.
    If you can't figure out a category, use "Unclassified".
    Log message: {log_message}'''
    chat_completion = gq.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return chat_completion.choices[0].message.content

if __name__ == '__main__':
    print(classify_with_llm("Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_llm("The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classify_with_llm("System reboot initiated by user 12345."))
