def loan_approval_john(income, credit_score):
    if income > 30000 and credit_score > 650:
        return "Approved"
    else:
        return "Denied"
def loan_approval_priya(income, credit_score):
    if income > 35000 and credit_score > 700:
        return "Approved"
    else:
        return "Denied"
def loan_approval_ahmed(income, credit_score):
    if income > 32000 and credit_score > 670:
        return "Approved"
    else:
        return "Denied"
def loan_approval_emily(income, credit_score):
    if income > 28000 and credit_score > 630:
        return "Approved"
    else:
        return "Denied"
applicants = [
    ("John", loan_approval_john, 32000, 660),
    ("Priya", loan_approval_priya, 36000, 710)
]
for name, func, income, credit_score in applicants:
    result = func(income, credit_score)
    print(f"Applicant: {name}, Income: {income}, Credit Score: {credit_score} => {result}")

print("\nAnalysis:")
print("The approval criteria differ for each applicant based on their name, which may reflect bias in the logic.")