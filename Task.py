import random

class CareerGuidanceChatbot:
    def __init__(self):
        self.greetings = [
            "Hello! How can I help you today?",
            "Hi there! What can I assist you with?",
            "Welcome! Ready to explore your career options?"
        ]
        self.farewells = [
            "Goodbye! Best of luck with your career!",
            "See you! Don't hesitate to reach out again!",
            "Take care and keep chasing your dreams!"
        ]
        self.career_paths = {
            "technology": ["Software Engineer", "Data Scientist", "Cybersecurity Analyst", "Web Developer"],
            "healthcare": ["Doctor", "Nurse", "Pharmacist", "Physical Therapist"],
            "engineering": ["Mechanical Engineer", "Civil Engineer", "Electrical Engineer", "Chemical Engineer"],
            "arts": ["Graphic Designer", "Animator", "Writer", "Musician"],
            "business": ["Marketing Manager", "Financial Analyst", "Entrepreneur", "Human Resources Specialist"],
            "designing": ["Graphic Designer", "Product Designer", "Fashion Designer", "Web Designer", "Architechtural Designer"]
        }

    def greet(self):
        return random.choice(self.greetings)

    def farewell(self):
        return random.choice(self.farewells)

    def ask_interest(self):
        return "What field or area interests you the most? (e.g., technology, healthcare, engineering, arts, business, desiginging)"

    def recommend_jobs(self, interest):
        interest = interest.lower()
        if interest in self.career_paths:
            jobs = self.career_paths[interest]
            output = ""
            for i in range(len(jobs)):
                if (i != len(jobs) - 1):
                    output += f"     {i + 1}) {jobs[i]}\n"
                else:
                    output += f"     {i + 1}) {jobs[i]}"

            return f"Based on your interest in {interest}, here are some career options: {"\n"}{output}"
        
        else:
            return "I'm sorry, I don't have recommendations for that field. Could you specify another area of interest?"

    def handle_query(self, user_input):
        user_input = user_input.lower()
        if any(word in user_input for word in ["hello", "hi", "hey"]):
            return self.greet()
        elif any(word in user_input for word in ["bye", "goodbye", "see you", "quit", "exit"]):
            return self.farewell()
        elif any(word in user_input for word in ["help", "career", "job"]):
            return self.ask_interest()
        else:
            return self.recommend_jobs(user_input)

if __name__ == "__main__":
    bot = CareerGuidanceChatbot()
    print(bot.greet())

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit", "goodbye", "see you"]:
            print(f"Bot: {bot.farewell()}")
            break
        else:
            response = bot.handle_query(user_input)
            print(f"Bot: {response}")