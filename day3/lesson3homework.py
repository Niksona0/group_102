# this programm will ask for survey and format type at first, then it will ask for your info and based on your given info it will print long text about you in terminal
# if - short, detaild survey
# if 2 - formated, not-formated

survey_type = input("What type of survey would you like to get ? detaild or short : ")
format_type = input("What type of format would you like to see on text ? formated or unformated : ")

if survey_type == "detaild":
      name = input("Enter your name: ")
      surname = input("Enter your surname: ")
      age = input("How old are you: ")
      hobbies = input("What are your hobbies: ")
      academy_subject = input("Which subject are you learning in your academy? ")
      academy_name = input("In which academy are your learning? ")
      location = input("Where do you live? ")
      if format_type == "formated":
            print("""
            Your name is {} {}.
            You are {} years old.
            you love {}.
            In {} you are learning {}.
            you are living at {}.""".format(name, surname, age, hobbies, academy_name, academy_subject, location))
      else:
            print("Your name is {} {}, You are {} years old and you love {}, in {} you are learning {}, you are living at {}.".format(name, surname, age, hobbies, academy_name, academy_subject, location))
else:
      if format_type == "formated":
            name = input("Enter your name: ")
            surname = input("Enter your surname: ")
            age = input("How old are you: ")
            academy_name = input("In which academy are your learning? ")

            print("""
            Your name is {} {}.
            You are {} years old.
            You are learning in {}.""".format(name, surname, age, academy_name))
      else:
            name = input("Enter your name: ")
            surname = input("Enter your surname: ")
            age = input("How old are you: ")
            academy_name = input("In which academy are your learning? ")

            print("""Your name is {} {}, You are {} years old, You are learning in {}.""".format(name, surname, age, academy_name))
