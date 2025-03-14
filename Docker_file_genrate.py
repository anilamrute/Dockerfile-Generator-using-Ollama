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