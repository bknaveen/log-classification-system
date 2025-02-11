 # Log Classification System 📄
## Project Description
The **Log Classification System** is a machine learning-based pipeline designed to classify log messages into predefined categories. It simplifies understanding and processing log data, helping organizations monitor, analyze, and resolve errors from logs efficiently. The project utilizes fine-tuned BERT embeddings, pretrained Hugging Face models, and a custom classifier for interpreting patterns in log messages. Advanced integration is included for identifying HTTP status codes and specific patterns dynamically.
## Features
- **Predictive Classification**: Classifies logs into categories like "Error", "Restart", "404 Not Found", etc., using `SentenceTransformer` embeddings and `joblib`-based classifiers.
- **HTTP Status Detection**: Dynamically identifies and reports HTTP status codes (e.g., `404`, `500`) within the logs.
- **Customizable Labels**: Easily extend the classifier for new log categories.
- **Multi-level Processors**:
    - **BERT-based Prediction** (`bertProcessor.py`): Embedding-based transformer model for advanced text classification.
    - **Regular Expression Processing** (`regexProcessor.py`): Detects patterns like HTTP codes and predefined patterns.
    - **LLM-based Classification** (`llmProcessor.py`): Uses large language models for fallback processing and complex message understanding.

- **High Precision**: Ensures classifier outputs are precise and reliable with confidence thresholds.

## Architecture
### 1. **Input Flow**:
- Log Messages are supplied as input to the system. These can be:
    - Raw messages from logs
    - HTTP server logs
    - System event notifications

### 2. **Classification Pipeline**:
- **Preprocessing**: Tokens are generated using the Hugging Face tokenizer and transformed using `all-MiniLM-L6-v2` (`bertProcessor.py`).
- **Embedding**: Using `SentenceTransformer`, the input is converted to vector representations.
- **Classification Models**:
    - A `Joblib` pre-trained classifier utilizes the embeddings to predict log categories.
    - If a high-confidence classification is not met, the fallback mechanism (`regexProcessor.py` and `llmProcessor.py`) provides additional classifications.

### 3. **Custom Processors**:
- **HTTP Status Code Processor**: Extracts HTTP status codes and outputs them directly when identified.
- **Regex Processor**: Uses regular expressions for pattern-based classification (e.g., detecting numeric IDs, server statuses, etc.).

### 4. **Output Flow**:
- The system outputs:
    - Human-readable labels (e.g., "Error", "404", "Login Failures")
    - Raw HTTP status codes (e.g., `200`, `404`) if detected within the logs.

- If the system cannot classify a message confidently, it falls back to an "Unclassified" label.
