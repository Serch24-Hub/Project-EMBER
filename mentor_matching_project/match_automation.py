#match_automation 
import pandas as pd

#Loading data from CSV files
def load_data():
    print("Loading Data...")

    try: 
        mentors = pd.read_csv("mentors.csv")
        mentees = pd.read_csv("mentees.csv")

        print (f"Loaded {len(mentors)} mentor profiles.")
        print (f"Loaded {len(mentees)} mentee profiles.")

        return mentors, mentees
    
    except Exception as e:
        print ("Error loading data:", e)
        return None, None
    

 #Main function to execute the script   
if __name__ == "__main__":
    mentors, mentees = load_data()

    #print mentors and mentees data
    if mentors and mentees:
        print("\nSample Mentor:")
        print(mentors[0])

        print("\nSample Mentee:")
        print(mentees[0])

#Data Structure code: 
class Mentor:
    def __init__(self, row):
        self.id = row["MentorID"]
        self.name = row["Name"]
        self.expertise = row["Expertise"]
        self.industry = row["Industry"]
        self.availability =row["Availability"]
        self.style = row["MentoringStyle"]

    def __str__(self):
        return f"{self.name} ({self.expertise})" 
    
class Mentee:
    def __init__(self, row):
        self.id = row["MenteeID"]
        self.name = row["Name"]
        self.goals = row["LearningGoals"]
        self.expertise = row["DesiredExpertise"]
        self.industry = row["IndustryInterest"]
        self.challenges = row["CurrentChallenges"]  

    def __str__(self):
        return f"{self.name} ({self.goals}, {self.availability})"
    