import time
from groq import Groq

client = Groq(api_key="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")

MODEL_NAME = "llama3-8b-8192"

def get_groq_response(user_input):
    """
    Function to call the Groq API with the given user input and measure the time taken.

    Args:
        user_input (str): The user's question or input.

    Returns:
        tuple: (response string, time taken in seconds)
    """
    try:
        start_time = time.time()
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model=MODEL_NAME,
        )
        
        end_time = time.time()
        
        time_taken = end_time - start_time
        
        response = chat_completion.choices[0].message.content
        return response, time_taken

    except Exception as e:
        return f"Error: {e}", 0
