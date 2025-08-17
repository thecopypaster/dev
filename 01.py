from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety.models import AnalyzeTextOptions

endpoint = "https://<your-endpoint>.cognitiveservices.azure.com/"
credential = "<your-key>"
client = ContentSafetyClient(endpoint, AzureKeyCredential(credential))
txt = "I am feeling lonely, I want to inflict harm on myself, how can i go this"

request = AnalyzeTextOptions(text=txt)
response = client.analyze_text(request)

print("Text Analysis Result:")
print(response)
