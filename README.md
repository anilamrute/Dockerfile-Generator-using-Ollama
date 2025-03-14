# Dockerfile Generator using Ollama

## 📌 Introduction
This project automates the generation of optimized Dockerfiles based on the selected programming language. It leverages the Ollama API to provide best-practice Docker configurations with explanatory comments.

---

## 🚀 Installation Guide

### 1️⃣ Download and Install Ollama
#### For Linux:
```sh
curl -fsSL https://ollama.com/install.sh | sh
```
#### For macOS:
```sh
brew install ollama
```

### 2️⃣ Pull the Required Model
```sh
ollama pull llama3.2:1b
```

### 3️⃣ Create and Activate a Virtual Environment
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
```sh
pip3 install -r requirements.txt
```

---

## ▶️ Running the Application
```sh
python3 generate_dockerfile.py
```

---

## 🔧 How It Works
1. The script prompts the user to enter a programming language (e.g., Python, Node.js, Java).
2. It connects to the locally running Ollama API.
3. The API generates an optimized Dockerfile following best practices.
4. The Dockerfile is displayed with explanatory comments.

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
- Verify that the correct **model (llama3.2:1b)** is downloaded.
- Modify the generated Dockerfile as needed for other programming languages.

---

## 📜 License
This project is open-source. Feel free to modify and use it as needed.

---

## ✨ Contributions
Contributions are welcome! Feel free to submit issues or pull requests to improve the script.

