"""
Simulating an AI prompt request.
"""

import json

payload = {
    "prompt": "Explain what artificial intelligence is",
    "temperature": 0.2,
    "max_tokens": 100
}

#Convert payload to JSON string
json_payload = json.dumps(payload, indent=4)

print("Prompt Payload Sent to AI:")
print(json_payload)


#Output:

#Prompt Payload Sent to AI:

{
    "prompt": "Explain what artificial intelligence is",
    "temperature": 0.2,
    "max_tokens": 100
}
