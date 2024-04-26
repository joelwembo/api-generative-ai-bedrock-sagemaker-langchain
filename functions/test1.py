import boto3
import json

prompt_data="""
AI tell me more about advertising in ecommerce using social media
"""

bedrock=boto3.client(service_name="bedrock-runtime")

payload={
    "prompt":prompt_data,
    "maxTokens":512,
    "temperature":0.8,
    "topP":0.8
}
body = json.dumps(payload)
model_id = "ai21.j2-mid-v1"
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json",
)

output = json.loads(response.get("body").read())
response_text = output.get("completions")[0].get("data").get("text")
print(response_text)