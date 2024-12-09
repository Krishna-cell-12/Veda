import random

class CareerGuidanceChatbot:
    def __init__(self):
        self.greetings = [
            "Hello! How can I help you today?",
            "Hi there! What can I assist you with?"
           
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
            "arts": ["Art Director", "Animator", "Art Therapist", "Sculptor"],
            "sports": ["coach", "Professional Athlete", "Sports Commentator", "Refree/Umpire"]           
        }
        self.career_paths_description = {
            "technology": [
                "If you want to pursue Software Engineer, first get your education degree in Computer science; Then, focus on acquiring strong programming skills, knowledge of algorithms, data structures, and software development methodologies.",
                "If you want to pursue Data Scientist, first get your education degree in fields like Mathematics, Statistics, Computer Science, or a related discipline. Gain proficiency in programming languages such as Python or R, and familiarize yourself with data analysis and visualization tools. Understanding machine learning algorithms and statistical modeling is crucial. Practical experience through internships, projects, and online courses can greatly enhance your skills. Certifications in data science or related areas can also be beneficial.",
                "If you want to pursue Cybersecurity Analyst, first get your education degree in Cybersecurity, Computer Science, Information Technology, or a related field. Gain knowledge of network security, cryptography, risk management, and ethical hacking. Practical experience through internships or hands-on projects is important. Consider obtaining certifications like CISSP (Certified Information Systems Security Professional), CEH (Certified Ethical Hacker), or CompTIA Security+ to strengthen your credentials.",
                "If you want to pursue Web Developer, first get your education degree in Computer Science, Web Development, or a related field. Learn programming languages such as HTML, CSS, JavaScript, and back-end languages like Python, PHP, or Ruby. Familiarize yourself with frameworks and libraries like React, Angular, or Vue.js for front-end development. Building a portfolio of web projects and gaining practical experience through internships or freelance work is highly recommended. Staying updated with the latest web development trends and technologies is also crucial."
            ],
            "healthcare": [
                "If you want to pursue Doctor, first get your education degree in Medicine, typically known as an MBBS (Bachelor of Medicine, Bachelor of Surgery) or equivalent. After completing your degree, you'll need to complete a residency program in your chosen specialty and obtain a medical license to practice. Continuous education and specialization through fellowships can enhance your expertise.",
                "If you want to pursue Nurse, first get your education degree in Nursing, such as a Bachelor of Science in Nursing (BSN). After your degree, you need to pass the licensure examination (NCLEX-RN) to become a Registered Nurse (RN). Specializations and advanced practice roles, such as Nurse Practitioner (NP), require further education and certification.",
                "If you want to pursue Pharmacist, first get your education degree in Pharmacy, such as a Doctor of Pharmacy (Pharm.D.). After your degree, you'll need to pass licensing exams (NAPLEX) to practice as a pharmacist. Continuing education and specializations, like clinical pharmacy or research, can provide additional career opportunities.",
                "If you want to pursue Physical Therapist, first get your education degree in Physical Therapy, typically a Doctor of Physical Therapy (DPT). After completing your degree, you'll need to pass the licensure exam to practice. Continuous education and specialization in areas like sports therapy or geriatrics can enhance your career."
            ],
            "engineering": [
                "If you want to pursue Mechanical Engineer, first get your education degree in Mechanical Engineering. After completing your degree, gain practical experience through internships or cooperative education programs. Consider obtaining professional certification (such as Professional Engineer, PE) and staying updated with the latest technologies and industry standards.",
                "If you want to pursue Civil Engineer, first get your education degree in Civil Engineering. Following your degree, practical experience through internships or entry-level positions is essential. Consider obtaining licensure as a Professional Engineer (PE) and specializing in areas like structural engineering, transportation, or environmental engineering.",
                "If you want to pursue Electrical Engineer, first get your education degree in Electrical Engineering. After earning your degree, internships or cooperative education programs are valuable for gaining practical experience. Professional certification (such as Professional Engineer, PE) and staying updated with the latest advancements in technology are also important steps.",
                "If you want to pursue Chemical Engineer, first get your education degree in Chemical Engineering. Post-degree, practical experience through internships or entry-level roles in industries like pharmaceuticals, energy, or manufacturing is beneficial. Consider obtaining professional certification and continuous learning to stay abreast of industry trends."
            ],
            "arts": [
                "If you want to pursue Art Director, Obtain a degree in Graphic Design, Fine Arts, Advertising, or a related field. Develop leadership skills and a strong visual aesthetic.Showcase your ability to create cohesive visual styles.Gain experience as a graphic designer or illustrator and work your way up.Build connections with creative directors and industry leaders.",
                "If you want to pursue Animator, Obtain a degree in Animation, Fine Arts, or Computer Graphics.Learn animation software (Autodesk Maya, Blender) and techniques.Create a demo reel showcasing your animations.Work on animation projects for movies, video games, or other media.Connect with other animators and attend animation festivals.",
                "If you want to pursue Art Therapist,  Obtain a degree in Art Therapy, Counseling, or a related field.Learn therapeutic techniques and art practices.Obtain certification as an art therapist.Gain experience through internships and clinical practice.Join art therapy associations and attend workshops.",
                "If you want to pursue Sculptor, Obtain a degree in Fine Arts with a focus on sculpture.Learn techniques for working with various materials like clay, stone, and metal.Create a collection of your three-dimensional artworks.Participate in art shows and exhibitions.Join sculptor associations and connect with galleries"
            ],
            "sports": [
                "If you want to pursue coach, Obtain a degree in Sports Science, Physical Education, or a related field.Gain expertise in coaching techniques and strategies.Obtain coaching certifications relevant to your sport.Gain experience by coaching at local clubs, schools, or amateur teams.Connect with other coaches and sports organizations to advance your career.",
                "If you want to pursue Professional Athlete, Obtain a high school diploma; a college degree can be beneficial.Train intensively in your chosen sport.Compete in local, regional, and national competitions.Work with professional coaches to improve skills and performance.Connect with sports agents and scouts to pursue professional opportunities.",
                "If you want to pursue Sports Commentator, Obtain a degree in Journalism, Communications, or a related field.Develop strong speaking, writing, and analytical skills.Gain experience through internships, covering sports events, and working with media outlets.Connect with broadcasters and sports media professionals.",
                "If you want to pursue Refree/Umpire, Obtain a high school diploma; a college degree can be beneficial. Learn the rules and regulations of your chosen sport.Obtain certification as a referee or umpire.Gain experience by officiating at local, regional, and national levels.Stay updated with the latest rule changes and best practices."
            ],
            
        }

    def greet(self):
        return random.choice(self.greetings)

    def farewell(self):
        return random.choice(self.farewells)

    def ask_interest(self):
        options = [
            "1. Technology", "2. healthcare", "3. engineering", "4. arts", "5. sports"
        ]
        return "What field or area interests you the most? Please select one of the following options:\n" + "\n".join(options)

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
            print(f"Bot: Based on your interest in {interest}, here are some career options, select them:\n{output}")
            while True:
                choice = int(input("Bot: Enter the job number you want to pursue: "))
                if choice <= 0 or choice > len(jobs):
                    print("Bot: Invalid Number")
                else:
                    print(f"Bot: You selected {jobs[choice - 1]}.")
                    break
            description = self.career_paths_description[interest]
            return f"{description[choice - 1]}"
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
