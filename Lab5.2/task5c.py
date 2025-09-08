def greet_user(name, gender):
    gender = gender.lower()
    if gender == "male":
        title = "Mr."
    elif gender == "female":
        title = "Mrs."
    else:
        # gender-neutral option
        title = "Mx."
    
    return f"Hello, {title} {name}! Welcome."
# --- Take user inputs ---
name_input = input("Enter your name: ")
gender_input = input("Enter your gender (male/female/other): ")

# --- Call function ---
message = greet_user(name_input, gender_input)
print(message)
