import openai
import spacy
from nltk.stem import WordNetLemmatizer

openai.api_key = ""  # YOUR API KEY GOES HERE

model_engine = "text-davinci-002"
model_prompt = "Hello, I'm Jarvis. How can I assist you today?"

def generate_response(prompt):
    # Preprocess user input with SpaCy and NLTK
    nlp = spacy.load("en_core_web_sm")
    lem = WordNetLemmatizer()
    doc = nlp(prompt)
    tokens = [lem.lemmatize(token.text) for token in doc]
    processed_prompt = " ".join(tokens)

    response = openai.Completion.create(
        engine=model_engine,
        prompt=processed_prompt,
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None,
        timeout=10,
    )
    message = response.choices[0].text
    return message

while True:
    try:
        user_input = input("> ")
        prompt = model_prompt + user_input + "\n"
        response = generate_response(prompt)
        print(response)
    except KeyboardInterrupt:
        break
