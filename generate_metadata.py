import os
import json
import openai
from dotenv import load_dotenv

from schema import Metadata, BimDiscipline

load_dotenv()

with open('school_plumbing.txt', 'r') as f:
#with open('schulgebäudes.txt', 'r') as f:
    context = f.readlines()

# Create client
client = openai.OpenAI(
    base_url="https://api.together.xyz/v1",
    api_key=os.environ["TOGETHER_API_KEY"],
)

# Call the LLM with the JSON schema
chat_completion = client.chat.completions.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    response_format={"type": "json_object", "schema": Metadata.model_json_schema()},
    messages=[
    {
        "role": "system",
        "content": f"You are a helpful assistant that understands BIM documents and engineering disciplines. Your answer should be in JSON format and only include the title, a brief one-sentence summary, and the discipline the document belongs to distinguishing between {[d.value for d in BimDiscipline]} based on the given document."
    },
    {
        "role": "user",
        "content": f"Analyze the provided document, which could be in either German or English. Extract the title, summarize it briefly in one sentence, and infer the discipline. Document:\n{context}"
    }
],
)

created_user = json.loads(chat_completion.choices[0].message.content)
print(json.dumps(created_user, indent=2))

{
  "title": "Plumbing System for a Typical School Building",
  "summary": "This document details the plumbing system of a school building, including potable water supply, fixtures and appliances, drainage waste and vent systems, and stormwater management, adhering to ADA compliance, low flow rates, water conservation standards, and local codes and regulations.\n",
  "discipline": "S - Sanit\u00e4r"
}