from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety.models import AnalyzeImageOptions, ImageData

endpoint = "https://contentsafety578345.cognitiveservices.azure.com/"
credential = "5gscYl0IBXJCaHJEMfMtjfZHZgHC0VD0AriYEKLs1lE1Q1dEnITuJQQJ99BHACYeBjFXJ3w3AAAHACOGgGlm"
client = ContentSafetyClient(endpoint, AzureKeyCredential(credential))


with open("input.jpg", "rb") as image_file:
    request = AnalyzeImageOptions(image=ImageData(content=image_file.read()))

response = client.analyze_image(request)
print("Image Analysis Result:")
print(response)
