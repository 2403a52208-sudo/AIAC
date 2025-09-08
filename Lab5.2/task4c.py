def score_applicant(education, experience, gender, age):
    """
    Scores a job applicant based on input features.
    Returns a score out of 100.
    """
    score = 0

    # Education scoring
    education_levels = {
        "none": 0,
        "highschool": 10,
        "bachelor": 25,
        "master": 35,
        "phd": 40
    }
    score += education_levels.get(education.lower(), 0)

    # Experience scoring
    if experience < 1:
        score += 0
    elif 1 <= experience < 3:
        score += 10
    elif 3 <= experience < 5:
        score += 20
    elif 5 <= experience < 10:
        score += 30
    else:
        score += 35

    # Gender scoring (should not affect score, but let's show if bias is present)
    if gender.lower() == "male":
        score += 0  # No bias
    elif gender.lower() == "female":
        score += 0  # No bias
    else:
        score += 0  # No bias

    # Age scoring
    if age < 18:
        score += 0
    elif 18 <= age < 25:
        score += 10
    elif 25 <= age < 40:
        score += 20
    elif 40 <= age < 60:
        score += 15
    else:
        score += 5

    return min(score, 100)

def main():
    print("Job Applicant Scoring System")
    education = input("Enter education level (None, Highschool, Bachelor, Master, PhD): ").strip()
    try:
        experience = float(input("Enter years of experience: ").strip())
    except ValueError:
        print("Invalid experience input. Setting to 0.")
        experience = 0
    gender = input("Enter gender (Male/Female/Other): ").strip()
    try:
        age = int(input("Enter age: ").strip())
    except ValueError:
        print("Invalid age input. Setting to 0.")
        age = 0

    score = score_applicant(education, experience, gender, age)
    print(f"\nApplicant Score: {score}/100")

    # Analysis of scoring logic for bias or unfair weightings
    print("\nAnalysis:")
    print("- Education and experience are weighted most heavily, which is generally fair if relevant to the job.")
    print("- Gender does not affect the score, which is fair and unbiased.")
    print("- Age gives some advantage to mid-career applicants, but does not exclude older or younger applicants entirely.")
    print("- If the job does not require higher education or experience, the weights may need adjustment to avoid unfairness.")
    print("- Always ensure that protected characteristics (like gender, age) are not unfairly weighted unless legally justified.")

if __name__ == "__main__":
    main()
