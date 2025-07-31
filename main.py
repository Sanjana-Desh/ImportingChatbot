import google.generativeai as genai

# Paste your API key here
genai.configure(api_key="AIzaSyA-Qti2Eb4UWipN9O-s0Kni3Vo9XRcNPgw")
# for m in genai.list_models():
#     print(m.name)

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
chat = model.start_chat(history=[])

def chat_with_gemini(prompt):
    response = chat.send_message(prompt)
    return response.text.strip()

if __name__ == "__main__":
    print("Gemini Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            break
        response = chat_with_gemini(user_input)
        print("Bot:", response)
