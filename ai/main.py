import openai

# Set OpenAI API configuration
openai.api_type = "azure"
openai.api_key = '9fd2d1a84636415685bcf7dc451040fb'
openai.api_base = 'https://api.umgpt.umich.edu/azure-openai-api/ptu'
openai.api_version = '2023-03-15-preview'

try:
    # Initialize conversation history
    conversation_history = [
        {"role": "system", "content": "You are a helpful virtual health assistant that creates structured workout and diet plans for every day of the week. Provide a diet for seven days a week and a workout for the amount of days the user wants. Use the same format everytime"},
    ]
    user_data={age: " ", gender: " ", weight:" ", height: " ", goal: " ",level:" ", diet: " ", supplements: " ", days:" "}
    survey=["16","female","124","5 feet","lose weight", "beginner","vegan","no","5"]
    for i=0, i< len(user_data), i+=1:
        user_data[age]=survey[i];

    start=0
    while True:
        # Get user input
        if start==0:
          print("Hi I am a virtual health assistant. I can give you advice on your diet or workout routine.")
          '''
          Age=input("Age: ")
          Gender=input("Gender: ")
          Goal=input("Goal: ")
          Height=input("Height: ")
          Weight=input("Weight: ")
          DaysPerWeek=input("Days of the week you want to workout: ")
          foods=input("Favorite foods:")
          restrictions=input("Dietary restrictions: ")
          user_input = Age+" "+ Gender+" " +" "+" "+ Goal+" " +Height+" "+Weight+" They want to workout "+ DaysPerWeek+ " Their favorite foods are "+ foods+ "Thier dietary restrictions are "+ restrictions
          '''
         ## user_input="Here is information about user x. The order is age, height,"
          start=1
        else:
            user_input=input("Anything else? ") 
        
        
        # Breaking condition
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break

        # Add user message to conversation
        conversation_history.append({"role": "user", "content": user_input})

        # Make a ChatCompletion request
        response = openai.ChatCompletion.create(
            engine='gpt-4',
            messages=conversation_history
        )

        # Get and print the assistant's reply
        assistant_reply = response['choices'][0]['message']['content']
        print(f"Assistant: {assistant_reply}")

        # Add assistant's reply to conversation
        conversation_history.append({"role": "assistant", "content": assistant_reply})

except openai.error.APIError as e:
    # Handle API error here, e.g., retry or log
    print(f"OpenAI API returned an API Error: {e}")

except openai.error.AuthenticationError as e:
    # Handle Authentication error here, e.g., invalid API key
    print(f"OpenAI API returned an Authentication Error: {e}")

except openai.error.APIConnectionError as e:
    # Handle connection error here
    print(f"Failed to connect to OpenAI API: {e}")

except openai.error.InvalidRequestError as e:
    # Handle connection error here
    print(f"Invalid Request Error: {e}")

except openai.error.RateLimitError as e:
    # Handle rate limit error
    print(f"OpenAI API request exceeded rate limit: {e}")

except openai.error.ServiceUnavailableError as e:
    # Handle Service Unavailable error
    print(f"Service Unavailable: {e}")

except openai.error.Timeout as e:
    # Handle request timeout
    print(f"Request timed out: {e}")

except Exception as e:
    # Handles all other exceptions
    print(f"An exception has occurred: {e}")

