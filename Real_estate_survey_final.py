import openai

openai.api_key = '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'

def take_survey():
    print("Welcome to the Carbon Emissions Survey!")
    print("Please answer the following questions:\n")

    # Questions
    questions = [
       "1. How do you currently track and measure your carbon energy emissions within your real estate operations?",
        "2. What steps have you taken to reduce your carbon footprint and promote energy efficiency in your properties?",
        "3. Have you implemented renewable energy sources, such as solar panels or geothermal systems, in any of your properties?",
        "4. Do you actively monitor and manage energy consumption in your buildings?",
        "5. How do you ensure energy efficiency and minimize wastage?",
        "6. What strategies do you have in place to promote sustainability and environmentally responsible practices in your real estate development and management processes?",
        "7. Are you involved in any energy conservation initiatives or programs?"
    ]

    # Collect responses
    responses = []
    for question in questions:
        response = input(question + "\n")
        responses.append(response)

    # Print survey summary
    print("\n--- Survey Summary ---")
    for i, response in enumerate(responses):
        print(questions[i])
        print("Response:", response)
        print()

    # Constructing a conversation with user responses
    survey_summary = "Here are the answers to the survey:\n" + "\n".join([f"{questions[i]} {response}" for i, response in enumerate(responses)])

    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": survey_summary},
        {"role": "user", "content": "Please suggest ways to reduce my carbon emissions based on my responses, but in a continuous paragraph, not as a list."}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=conversation,
    )

    # Extract the assistant's message
    chat_response = response.choices[0].message['content']

    print("\n--- Suggestions to Reduce Carbon Emissions ---")
    print(chat_response)

# Run the survey
take_survey()
