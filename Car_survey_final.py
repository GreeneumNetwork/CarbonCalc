import openai

openai.api_key = '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'

def take_survey():
    print("Welcome to the Carbon Emissions Survey!")
    print("Please answer the following questions:\n")

    # Questions
    questions = [
        "1. How many cars are currently being used in your operations, and how frequently are these vehicles being used?",
        "2. How much fuel, in terms of gallons, is consumed by your total number of vehicles on an average week?",
        "3. What is the average distance (in miles) typically traveled by your vehicles on an average week?",
        "4. What policies or initiatives do you implement to reduce carbon emission output from your vehicle(s)?",
        "5. Are you operating any hybrid or electric vehicles? If so, what percentage of total cars do they represent?",
        "6. What percentage of your organization's total carbon emissions is attributed to cars?",
        "7. What is your organization's readiness to install or increase the number of electric vehicle charging stations at your facilities?"
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
