import google.generativeai as genai

genai.configure(api_key="AIzaSyAMZ3wTOEdoNcFnr50uY1jOHb1UXEgmSGI")
model = genai.GenerativeModel('gemini-1.5-flash')

def chatbot():
    print("Chatbot: Hello! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Thank you!")
            break
        try:
            response = model.generate_content(user_input)
            print(f"Chatbot: {response.text}")
        except Exception as e:
            print("Chatbot: Sorry, something went wrong.")

chatbot()