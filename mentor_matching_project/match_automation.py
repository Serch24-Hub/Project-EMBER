#match_automation Code

#the line of code below imports the pnadas library an named it as pd, this library is used for data handling
import pandas as pd

#Loading data from CSV files
def loadData():
    print("Accessing data from CSV files...")

    try: 
        mentors = pd.read_csv("mentors.csv")
        mentees = pd.read_csv("mentees.csv")

        print (f"Loaded {len(mentors)} mentor profiles.")
        print (f"Loaded {len(mentees)} mentee profiles.")

        return mentors, mentees
    
    except Exception as e:
        print ("Error loading data:", e)
        return None, None


#Defining the classes for Mentor and Mentee: 
class Mentor:
    def __init__(self, row):
        self.id = row["MentorID"]
        self.name = row["Name"]
        self.expertise = row["Expertise"]
        self.industry = row["Industry"]
        self.availability =row["Availability"]
        self.style = row["MentoringStyle"]
        self.capacity = int(row["MentoringCapacity"])
        self.years = int(row["yearsOfExperience"])
        self.assignedMentees = []

    def hasCapacity(self):
        return len(self.assignedMentees) < self.capacity
    
    def assignMentee(self, mentee):
        self.assignedMentees.append(mentee)

    def __str__(self):
        return f"{self.name} - Expertise: {self.expertise}, Industry: {self.industry}, Years of Experience: {self.years}, Capacity: {self.capacity}" 


class Mentee:
    def __init__(self, row):
        self.id = row["MenteeID"]
        self.name = row["Name"]
        self.goals = row["LearningGoals"]
        self.expertise = row["DesiredExpertise"]
        self.industry = row["IndustryInterest"]
        self.challenges = row["CurrentChallenges"]  
        self.availability = row["Availability"]

    def __str__(self):
        return f"{self.name} - Goals: {self.goals}, Interested in: {self.expertise}, Industry: {self.industry}, Availability: {self.availability}"


#matching algorithm to find best matches for a mentor with multiple mentees
def matchesCalculation(mentor, mentee):
    score = 0
    if mentee.expertise.strip().lower() == mentor.expertise.strip().lower():
        score += 1
    if mentee.industry.strip().lower() == mentor.industry.strip().lower():
        score += 1
    if mentee.availability.strip().lower() == mentor.availability.strip().lower():
        score += 1
    return score


#automation to match all mentors with multiple mentees
def autoMatchMultiple(mentorsDf, menteesDf):
   mentors = [Mentor(row) for _, row in mentorsDf.iterrows()]
   mentees = [Mentee(row) for _, row in menteesDf.iterrows()]
   unmatchedMentees = []

   for mentee in mentees:
       bestMatch = None
       bestScore = -1

       for mentor in mentors:
           if mentor.hasCapacity():
               score = matchesCalculation(mentor, mentee)
               if score > bestScore:
                   bestScore = score
                   bestMatch = mentor

       if bestMatch:
           bestMatch.assignMentee(mentee)
       else:
           unmatchedMentees.append(mentee)


#Print matched mentors and their assigned mentees
   print("\n--- Matched Mentors and Mentees ---")
   for mentor in mentors:
       print(f"\nMentor: {mentor}")
       if mentor.assignedMentees:
           print("Assigned Mentees:")
           for mentee in mentor.assignedMentees:
               print(f" - {mentee}")
       else:
           print("No mentees assigned due to capacity limits.")

 # Print unmatched mentees
   if unmatchedMentees:
       print("\nUnmatched Mentees:")
       for mentee in unmatchedMentees:
           print(f" - {mentee.name} (desired expertise: {mentee.expertise}, industry interest: {mentee.industry}, availability: {mentee.availability})")


#Run the Script
if __name__ == "__main__":
    mentorsDf, menteesDf = loadData()

    if mentorsDf is not None and menteesDf is not None:
        print ("\n--- Automated Matching (Multiple) ---")
        autoMatchMultiple(mentorsDf, menteesDf)