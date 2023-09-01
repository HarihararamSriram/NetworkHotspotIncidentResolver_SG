import pickle
import numpy as np
import openai
from map import incident_to_type
import pandas as pd
from langchain import PromptTemplate, LLMChain
from langchain import HuggingFaceHub
from dotenv import load_dotenv

load_dotenv()

def predict(query) -> str:
    f = open("./hotspot_model.pkl", "rb")
    classifier = pickle.load(f)
    encoders = pickle.load(open("./LabelEncoder.pkl", "rb"))
    try:
        incident_type = incident_to_type[query]
        print(incident_type)
        encoded_type = encoders["Type"].transform([incident_type])
        encoded_query = encoders['Incident'].transform([query])
        querys = pd.DataFrame(
            {'Type': encoded_type, 'Incident': encoded_query})
        pred = classifier.predict(querys)
        answer = encoders['Resolution'].inverse_transform(pred)[0]
        # answer += chat_gpt(answer)
        return f"Sure, he is the solution to your query on the incident:\n\n{answer}"
    except Exception as e:
        print(e)
        return "I'm sorry, but I couldn't find a solution based on the provided information. It's possible that there might be some issues with the input or details you've provided. If you could please provide more context or clarify your request, I'll do my best to assist you further. Your input is essential, and I'm here to assist you to the best of my abilities."


def chat_gpt(message) -> str:
    """
    llm = HuggingFaceHub(repo_id="tiiuae/falcon-7b-instruct", model_kwargs={"temperature": 0.8, "max_new_tokens" : "200"})
    prompt = PromptTemplate(template="You are a intelligent assistant. Explain the following in detail: {message}", input_variables=["message"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    reply = llm_chain.run(message=message, raw_response=True)
    print(reply)
    return f"{reply}"
    """
    openai.api_key = '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'
    messages = [{"role": "system", "content":
                 "You are a intelligent assistant."}]
    if message:
        messages.append(
            {"role": "user", "content": f"Explain this in detail: f{message}"},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    return f"{reply}"
