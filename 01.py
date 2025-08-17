from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety.models import AnalyzeImageOptions, ImageData

endpoint = "https://<yourservice>.cognitiveservices.azure.com/"
credential = "your-azure-key-here"  # Replace with your actual Azure key
client = ContentSafetyClient(endpoint, AzureKeyCredential(credential))


with open("input.jpg", "rb") as image_file:
    request = AnalyzeImageOptions(image=ImageData(content=image_file.read()))

response = client.analyze_image(request)
print("Image Analysis Result:")
print(response)
