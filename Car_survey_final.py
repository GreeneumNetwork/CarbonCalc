import openai

openai.api_key = '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'

def take_survey():
    print("Welcome to the Carbon Emissions Survey!")
    print("Please answer the following questions:\n")

    # Questions
    questions = [
        "1. What is the average fuel efficiency of your vehicle(s)?",
        "2. Do you have any hybrid or electric vehicle options? If so, what is their range and charging infrastructure?",
        "3. How do you incorporate renewable energy sources in your daily life?",
        "4. Are you aware of your carbon footprint or greenhouse gas emissions data?",
        "5. Have you made any commitments to reducing your overall carbon emissions in the coming years?",
        "6. Are there any initiatives or incentives you've considered to choose more environmentally friendly alternatives?",
        "7. Do you have an estimate of your personal carbon footprint?"
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
