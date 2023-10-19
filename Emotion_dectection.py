import requests

def emotion_detector(text_to_analyze):
    # Define the URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network'
    headers = {"grpc-metadata-mm-model-id": "emotion_ag"}

    # Create the input JSON data
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send a POST request to the Watson NLP Library
    response = requests.post(url, headers=headers, json=input_json)

    # Check for a successful response
    if response.status_code == 200:
        # Parse and return the result (you may need to adapt this based on the actual response format)
        result = response.json()
        return result
    else:
        # Handle errors if needed
        return "Error: Emotion detection request failed"

# Example usage:
if _name_ == "_main_":
    text_to_analyze = "I'm feeling great today!"
    result = emotion_detector(text_to_analyze)
    print(result)
