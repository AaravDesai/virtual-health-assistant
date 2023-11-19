#Importing required libraries
import openai
# Set OpenAI API configuration
openai.api_type = "azure"
openai.api_key = '9fd2d1a84636415685bcf7dc451040fb'
openai.api_base = 'https://api.umgpt.umich.edu/azure-openai-api/ptu'
openai.api_version = '2023-03-15-preview'
try:
    # Initialize conversation history
    conversation_history = [
        {"role": "system", "content": "You are a helpful virtual health assistant"},
    ]
    labels=["age: ","dietaryRestriction: ","experience: ","fitnessGoal:  ","gender: ","height: ","weight: ","includeSupplements: ","numDays: "]
    values=["20","Vegetarian","Beginner","Muscle Gain","Male","5 feet 9 inches","155 Pounds","Yes","4"]
    age,dietaryRestriction,experience,fitnessGoal,gender,height,weight,includeSupplements,numDays = values
    user_data = f"This is the profile of a {age} year old {gender} weighing {weight} and standing at {height} who wants fitness goal is {fitnessGoal}. Currently a {experience}, the person has a {dietaryRestriction} dietary restriction. The imdividual has chosen to create a plan for {numDays} per week and has said {includeSupplements} to supplements."
    #setting control flag
    flag = False
    while True:
        # Get user input
        if flag==False:
          print("Hi I am a Vivo!, a virtual health assistant. I can provide you with a personalised Workout & Diet Routine.")
          user_input="Create a stuctured diet & workout plan for the user using the responses provided. Make it extremely personalized and tailored to the number of days per week he provides. Create a day by day plan for both the diet and workout(Base the workout on the fitness goal indicated by the user and make it extremely accurate) which has been provided by the user, and give the same format with the day by day and step by step Workout Routine followed Diet and include supplements in diet if user has said yes. Also provide with a note saying that you should consult a medical professional with the dosage of the supplement if indicated by the user that he wants a supplement. Wish him goodluck at the end and a message saying that hope he achieves the fitness goal which he mentioned. USe the format which I am providing below to base your answer on. Note only use the output format, the content is going to be determined by you \
          \
          **Day-by-Day Workout Routine**: \
            *Day 1 - Chest and Back* \
            \
            Warm-up with 10-15 minutes of cardio - Treadmill or cycling \
            1. Bench Press - 3 sets of 8-12 reps \
            2. Incline Dumbbell Press - 3 sets of 8-12 reps \
            3. Bent-over Rows - 3 sets of 8-12 reps \
            4. Lat Pulldowns - 3 sets of 8-12 reps \
            5. Finish with 10-15 minutes of stretching \
            \
            *Day 2 - Legs and Abs* \
            \
            Warm up with 10-15 minutes of cardio - Treadmill or cycling \
            1. Squats - 3 sets of 8-12 reps \
            2. Lunges - 3 sets of 8-12 reps per leg \
            3. Calf Raises - 3 sets of 15-20 reps \
            4. Planks - 3 sets of 30-60 seconds \
            5. Finish with 10-15 minutes of stretching \
            \
            *Rest on Day 3* \
            \
            *Day 4 - Arms and Shoulders* \
            \
            Warm up with 10-15 minutes of cardio - Treadmill or cycling \
            1. Bicep Curls - 3 sets of 8-12 reps \
            2. Tricep Dips - 3 sets of 8-12 reps \
            3. Shoulder Press - 3 sets of 8-12 reps \
            4. Finish with 10-15 minutes of stretching \
            \
            *Day 5 - Repeat of Day 1's routine* \
            \
            *Rest on Day 6* \
            \
            *Day 7 - Repeat of Day 2's routine*"" \
            \
            ***Diet Plan (Vegetarian)*** \
            \
            *Day 1:* \
            \
            - Breakfast: Oatmeal with chopped fruits \
            - Lunch: Chickpea salad with whole grain bread \
            - Dinner: Grilled cottage cheese with sautéed vegetables \
            - Snack: Guacamole and carrot sticks \
            \
            *Day 2:* \
            \
            - Breakfast: Greek yogurt with blueberries \
            - Lunch: Lentil soup with brown rice \
            - Dinner: Veggie stir fry with tofu \
            - Snack: Fruit smoothie \
            \
            *Day 3:* \
            \
            - Breakfast: Whole grain toast with avocado \
            - Lunch: Quinoa bowl with veggies and hummus \
            - Dinner: Stuffed bell peppers with bulgur and black beans \
            - Snack: A handful of nuts \
            \
            *Day 4:* \
            \
            - Breakfast: Scrambled tofu with spinach and tomatoes \
            - Lunch: Whole grain pasta with mushroom sauce \
            - Dinner: Vegetable curry with basmati rice \
            - Snack: A banana and a spoonful of almond butter \
            \
            ***Supplements*** \
            \
            Since you have indicated yes for supplements, here are a few you might consider: \
            \
            1. *Whey Protein*: Helps in muscle recovery and growth. \
            2. *Multivitamins*: Necessary for overall health. \
            3. *Creatine*: Helps in high intensity training. \
            \
            ***Note*: Please consult with a healthcare professional to determine the right dosage for your supplements based on your individual conditions and needs. * \
            \
            Now that you're good to go, I wish you the best of luck in your fitness journey! I hope you achieve your goal of gaining muscle mass and improving your overall fitness."
          user_input += user_data
          flag = True
        else:
            user_input=input("Would you like to add anything, or make any changes? ")
        # Breaking condition
        if user_input.lower() in ["exit", "quit", "bye","no"]:
            print("I hope I was able to provide you with a satisfactory personalized health plan. Goodbye!")
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
        print(f"Vivo: {assistant_reply}")
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
