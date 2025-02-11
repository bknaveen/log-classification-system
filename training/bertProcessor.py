# import joblib
# from sentence_transformers import SentenceTransformer
#
# model_embedding = SentenceTransformer('all-MiniLM-L6-v2')
# model_classification = joblib.load("../models/log_classifier.joblib")
#
#
# def classify_with_bert(log_message):
#     embeddings = model_embedding.encode([log_message])
#     probabilities = model_classification.predict_proba(embeddings)[0]
#     if max(probabilities) < 0.5:
#         return "Unclassified"
#     predicted_label = model_classification.predict(embeddings)[0]
#
#     return predicted_label
#
#
# if __name__ == "__main__":
#     logs = [
#         "alpha.osapi_compute.wsgi.server - 12.10.11.1 - API returned 404 not found error",
#         "GET /v2/3454/servers/detail HTTP/1.1 RCODE   404 len: 1583 time: 0.1878400",
#         "System crashed due to drivers errors when restarting the server",
#         "Hey bro, chill ya!",
#         "Multiple login failures occurred on user 6454 account",
#         "Server A790 was restarted unexpectedly during the process of data transfer"
#     ]
#     for log in logs:
#         label = classify_with_bert(log)
#         print(log, "->", label)
#
#

import joblib
from sentence_transformers import SentenceTransformer

# Map numeric labels to human-readable class names
LABEL_MAPPING = {
    0: "Error",
    1: "Restart",
    2: "HTTP Status",
    4: "Login Failures",
    None: "Unclassified"
}

# Load the embedding model and the classification model
model_embedding = SentenceTransformer('all-MiniLM-L6-v2')
model_classification = joblib.load("../models/log_classifier.joblib")


def classify_with_bert(log_message):
    # Get the embeddings for the log message
    embeddings = model_embedding.encode([log_message])
    # Get the probabilities from the classification model
    probabilities = model_classification.predict_proba(embeddings)[0]
    # If the highest probability is below 0.5, classify it as "Unclassified"
    if max(probabilities) < 0.5:
        return "Unclassified"

    # Get the predicted numeric label
    predicted_label = model_classification.predict(embeddings)[0]
    # Map the numeric label to a human-readable string
    return LABEL_MAPPING.get(predicted_label, "Unclassified")


if __name__ == "__main__":
    logs = [
        "alpha.osapi_compute.wsgi.server - 12.10.11.1 - API returned 404 not found error",
        "GET /v2/3454/servers/detail HTTP/1.1 RCODE   404 len: 1583 time: 0.1878400",
        "System crashed due to drivers errors when restarting the server",
        "Hey bro, chill ya!",
        "Multiple login failures occurred on user 6454 account",
        "Server A790 was restarted unexpectedly during the process of data transfer"
    ]

    # Classify each log message and print the result
    for log in logs:
        label = classify_with_bert(log)
        print(log, "->", label)

