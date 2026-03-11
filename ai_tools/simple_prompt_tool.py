"""
Simple AI-style prompt tool (simulation).
"""

def generate_response(prompt):
    if "python" in prompt.lower():
        return "Python is a powerful programming language used in AI and backend systems."
    elif "ai" in prompt.lower():
        return "Artificial Intelligence enables machines to perform tasks that normally require human intelligence."
    else:
        return "This is a simulated AI response."
    
user_prompt = input("Ask Something: ")
response = generate_response(user_prompt)

print("\AI Response:")
print(response)

        