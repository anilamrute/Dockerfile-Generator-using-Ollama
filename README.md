# Dockerfile Generator using Ollama

## 📌 Introduction
This project automates the generation of optimized Dockerfiles based on the selected programming language. It leverages the Ollama API to provide best-practice Docker configurations with explanatory comments.

---

## 🚀 Installation Guide

### 1️⃣ Download and Install Ollama
Ollama is required for generating Dockerfiles using an AI model. It must be installed before running the script.

#### For Linux:
```sh
curl -fsSL https://ollama.com/install.sh | sh
```
#### For macOS:
```sh
brew install ollama
```

### 2️⃣ Pull the Required Model
Before using Ollama, you need to download the required AI model to generate optimized Dockerfiles.
```sh
ollama pull llama3.2:1b
```

### 3️⃣ Create and Activate a Virtual Environment
A virtual environment ensures that dependencies are installed in an isolated environment, preventing conflicts with system-wide packages.

#### On Linux/macOS:
```sh
python3 -m venv venv
source venv/bin/activate
```
#### On Windows:
```sh
python3 -m venv venv
.\venv\Scripts\activate
```

### 4️⃣ Install Dependencies
To ensure all necessary Python packages are available, install them using the `requirements.txt` file.
```sh
pip3 install -r requirements.txt
```

---

## ▶️ Running the Application
Run the script to generate a Dockerfile based on the programming language you input.
```sh
python3 generate_dockerfile.py
```

---

## 🔧 How It Works
1. The script prompts the user to enter a programming language (e.g., Python, Node.js, Java).
2. It connects to the locally running Ollama API to generate an optimized Dockerfile.
3. The API analyzes best practices and outputs a structured Dockerfile.
4. The generated Dockerfile includes explanatory comments to help understand its structure.

---

## 💡 Example Usage
```sh
python3 generate_dockerfile.py
```
```
Enter programming language: python
# Generated Dockerfile will be displayed...
```

---

## 🏆 Troubleshooting
- Ensure the **Ollama service** is running before executing the script.
- Verify that the correct **model (llama3.2:1b)** is downloaded and available.
- Modify the generated Dockerfile as needed for other programming languages.

---

## 📜 License
This project is open-source. Feel free to modify and use it as needed.

---

## ✨ Contributions
Contributions are welcome! Feel free to submit issues or pull requests to improve the script.

---

## 🖥️ Code Explanation
This script takes user input for a programming language and generates an optimized Dockerfile using the Ollama API.

```python
import ollama  # Import the Ollama library to interact with the API

# Define a prompt template that tells the AI to generate a Dockerfile with best practices
PROMPT = """
ONLY Generate an ideal Dockerfile for {language} with best practices. Do not provide any description
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
"""

def generate_dockerfile(language):
    """Generates an optimized Dockerfile for the given programming language."""
    response = ollama.chat(
        model='llama3.1:8b',  # Specifies the AI model to use
        messages=[{'role': 'user', 'content': PROMPT.format(language=language)}]  # Sends user input to the AI
    )
    return response['message']['content']  # Returns the generated Dockerfile content

if __name__ == '__main__':
    language = input("Enter the programming language: ")  # Ask user for the programming language
    dockerfile = generate_dockerfile(language)  # Generate the Dockerfile
    print("\nGenerated Dockerfile:\n")
    print(dockerfile)  # Print the output
```

### 📌 Explanation of the Code:
- **Import Ollama:** Loads the API to process user input.
- **Define the Prompt:** Instructs the AI to generate an optimized Dockerfile.
- **Function `generate_dockerfile(language)`:**
  - Uses Ollama to process the request and return a best-practice Dockerfile.
- **Main Execution Block:**
  - Takes user input for the programming language.
  - Calls the function to generate a Dockerfile.
  - Displays the generated Dockerfile to the user.

This ensures the script remains simple, effective, and follows best practices.

