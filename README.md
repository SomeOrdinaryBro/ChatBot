# JARVIS

JARVIS is a Python program that generates responses to user input using OpenAI's natural language processing platform, along with Spacy and NLTK libraries. This code could serve as the foundation for building a chatbot or conversational AI.

## Requirements

To run JARVIS, you will need:

-   An **[OpenAI API](https://openai.com/api/)** key
-   **[Python 3.x](https://www.python.org/downloads/)** Latest
-   The following Python libraries: **OpenAI**, **spacy**, and **nltk**

## Usage

1.  Clone the repository to your local machine.
2.  Replace `""` with your OpenAI API key in the line `openai.api_key = ""`.
3.  Run the program in a terminal with the command `python jarvis.py`.
4.  JARVIS will prompt the user for input with the message "Hello, I'm Jarvis. How can I assist you today?".
5.  Enter your message and press Enter.
6.  JARVIS will generate a response based on your input and display it in the console.

To stop the program, press Ctrl+C.

## Customization

You can customize JARVIS to fit your needs by modifying the `model_engine` and `model_prompt` variables. The `model_engine` variable specifies the OpenAI model to use for generating responses. The `model_prompt` variable contains the message that JARVIS will display to the user before each response. You can change this message to fit your use case.

## Contributions

Contributions are welcome to JARVIS! If you find a bug or want to suggest an improvement, please open an issue or pull request.

## Update

The latest update has made the following changes to the code:

-   Define a single model prompt for generating responses.
-   Use a fixed prompt for all user inputs.
-   Generate only one response for each user input.
-   Use a temperature of 0.5 for response generation.
-   Remove the use of a stop sequence for response generation.
-   Remove some unnecessary pre-processing steps for the prompt.
-   Set the maximum token limit to 1024 for response generation.
-   Set a timeout limit of 10 seconds for response generation.
-   Do not remove non-ASCII characters from the generated response.
