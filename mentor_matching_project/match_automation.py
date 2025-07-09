#match_automation Code

#the line of code below imports the pnadas library an named it as pd, this library is used for data handling
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
    

 #Main function to execute the script   (Old One)
"""if __name__ == "__main__":
    mentors, mentees = load_data()

    if mentors is not None and mentees is not None:
        print("\nSample Mentor:")
        print(mentors.iloc[1])  # show first mentor

        print("\nSample Mentee:")
        print(mentees.iloc[1])  # show first mentee"""

#Defining the classes for Mentor and Mentee: 
class Mentor:
    def __init__(self, row):
        self.id = row["MentorID"]
        self.name = row["Name"]
        self.expertise = row["Expertise"]
        self.industry = row["Industry"]
        self.availability =row["Availability"]
        self.style = row["MentoringStyle"]

    def __str__(self):
        return f"{self.name} - Expertise: {self.expertise}, Industry: {self.industry}" 
    
class Mentee:
    def __init__(self, row):
        self.id = row["MenteeID"]
        self.name = row["Name"]
        self.goals = row["LearningGoals"]
        self.expertise = row["DesiredExpertise"]
        self.industry = row["IndustryInterest"]
        self.challenges = row["CurrentChallenges"]  

    def __str__(self):
        return f"{self.name} - Goals: {self.goals}, Interested in: {self.expertise}, Industry: {self.industry}"
    

#Code for manual matching of mentors and mentees
def show_manual_match(mentors_df, mentees_df, mentor_id, mentee_id):
    mentor_row = mentors_df[mentors_df["MentorID"] == mentor_id]
    mentee_row = mentees_df[mentees_df["MenteeID"] == mentee_id]


    if mentor_row.empty:
        print(f"Mentor with ID {mentor_id} not found.")
        return
    if mentee_row.empty:
        print(f"Mentee with ID {mentee_id} not found.")
        return
    
    mentor = Mentor(mentor_row.iloc[0])
    mentee = Mentee(mentee_row.iloc[0])

    print("\n--- Manual Match ---")
    print("Mentor:")
    print(mentor)
    print("Mentee:")
    print(mentee)


#Matching Algorithm by finding the best match for a mentor with a single mentee
def find_best_match(mentor, mentees_df):
    best_score = -1
    best_match = None

    for _, row in mentees_df.iterrows():
        mentee = Mentee(row)

        score = 0
        if mentee.expertise.strip().lower() == mentor.expertise.strip().lower():
            score += 1
        if mentee.industry.strip().lower() == mentor.industry.strip().lower():
            score += 1

        if score > best_score:
            best_score = score
            best_match = mentee

    return best_match


#matching algoprithm to find best matches for a mentor with multiple mentees
def find_best_matches(mentor, mentees_df):
    best_score = -1
    best_matches = []

    for _, row in mentees_df.iterrows():
        mentee = Mentee(row)
        score = 0

        if mentee.expertise.strip().lower() == mentor.expertise.strip().lower():
            score += 1
        if mentee.industry.strip().lower() == mentor.industry.strip().lower():
            score += 1

        if score > best_score:
            best_score = score
            best_matches = [mentee]
        elif score == best_score:
            best_matches.append(mentee)  

    return best_matches

#automation to match all mentors with mentees by pairs
def auto_match_all(mentors_df, mentees_df):
    for _, row in mentors_df.iterrows():
        mentor = Mentor(row)
        match = find_best_match(mentor, mentees_df)

        print(f"\nMentor: {mentor}")
        if match: 
            print (f"Matched with: {match}")
        else:
            print("No match found.")

#automation to match all mentors with multiple mentees
def auto_match_multiple(mentors_df, mentees_df):
    for _, row in mentors_df.iterrows():
        mentor = Mentor(row)
        matches = find_best_matches(mentor, mentees_df)

        print(f"\nMentor: {mentor}")
        if matches:
            print("Matched with:")
            for match in matches:
                print(f"- {match}")
        else:
            print("No match found.")


if __name__ == "__main__":
    mentors_df, mentees_df = load_data()

    if mentors_df is not None and mentees_df is not None:
        print ("\n--- Manual Match Example ---")
        show_manual_match(mentors_df, mentees_df, mentor_id=101, mentee_id=101)

        print ("\n--- Automated Matching ---")
        auto_match_all(mentors_df, mentees_df)

        print ("\n--- Automated Matching (Multiple) ---")
        auto_match_multiple(mentors_df, mentees_df)