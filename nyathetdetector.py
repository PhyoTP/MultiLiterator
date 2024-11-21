import requests
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("API_KEY")
# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# # CHANGE THIS to something you want your machine learning model to classify
# demo = classify("စား(သည်)။")

# label = demo["class_name"]
# confidence = demo["confidence"]


# # CHANGE THIS to do something different with the result
# print ("result: '%s' with %d%% confidence" % (label, confidence))

# This function will store your text in one of the training
# buckets in your machine learning project
def storeTraining(text, label):
    key = "ce2c1f20-a7d7-11ef-b4bc-3f9f6b744595f23dbb4e-3c80-4e33-839b-1f4f784bd4f5"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/train"

    response = requests.post(url, json={ "data" : text, "label" : label })

    if response.ok == False:
        # if something went wrong, display the error
        print (response.json())

