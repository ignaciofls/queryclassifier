import os, requests
import openai
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

openai.api_key = 'x1'
openai.api_type = 'azure'
openai.api_base = 'https://y.openai.azure.com/'
openai.api_version = '2021-11-01-preview'
language_key = 'x2'
language_endpoint = 'https://z.api.cognitive.microsoft.com/'
query = 'For how long can I run a Microsoft Teams live event?'
trainingphrases = 'The following is a list of queries and the categories they fall into\n\n*: Syntax\nWhat is the ph of soil in Argelia for 2000 m depth?: Semantic\nHow long has artificial intelligence been around?: Semantic\nA21415 embedding: Syntax\nWho is responsible for product X inside Microsoft: Semantic\nAML director: Syntax\nWill I get my anual variable bonus while on paternity leave?: Semantic\nLeave policy HR: Syntax\nFor how long do I need to be employed in Microsoft to be able to buy in the company store?: Semantic\nCompany store faq: Syntax\nhow do I bake a carrot pie: Semantic\nsince when is Washington the capital of USA?: Semantic\nthis textt is full of typpos: Semantic\naml security best practices: Syntax\n'
myprompt = trainingphrases+query

print("Query is : ", query)

response = openai.Completion.create(
   engine='davinci-002',
   prompt=myprompt
)

#Given the preview nature of Azure OpenAI and its SDK, you might have to use REST API (ie python requests) if you get a "Resource not found" error.
# url = 'https://y.openai.azure.com/openai/deployments/davinci-002/completions?api-version=2021-11-01-preview'
# payload = {"prompt": myprompt,
# "max_tokens": 500,
# "temperature": 0.2,
# "top_p": 1,
# "frequency_penalty": 1,
# "presence_penalty": 1.5}

# try:
#     r = requests.post(url, 
#         headers = {
#             # Request headers
#             'Content-Type': 'application/json',
#             'api-key': 'x1',
#           },
#         json = payload
#     )
#     print('This query is classified as ', r.json()['choices'][0]['text'])
# except Exception as err:
#     print(err)

# Authenticate the Azure CogSvcs client using your key and endpoint 
def authenticate_client():
    ta_credential = AzureKeyCredential(language_key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=language_endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

# Example method for detecting the language of text
def language_detection_example(client):
    try:
        response = client.detect_language(documents = [query])[0]
        print("Language: ", response.primary_language.name)
    except Exception as err:
        print("Encountered exception. {}".format(err))
language_detection_example(client)
