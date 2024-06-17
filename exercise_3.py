#The Valencia Hospital is developing an application to manage appointments. Design an algorithm for this application with the following features:
#It must have a login and validate the data; after the third failed attempt, it should be locked.
#The user can schedule an appointment for: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology
#Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
#There are 3 doctors for each specialty.
#The user can only book one appointment per specialist. 
# An error message should be displayed if the user tries to choose two appointments with the same doctor or the same specialty.
# As a developer, you can choose the doctors' names.
#The maximum limit for appointments, in general, is 3.
#Upon selecting a specialty, it will display if the user prefers a morning or afternoon appointment and show available hours.
# As a developer, you can choose the hours.
#Display available specialists.
#The user can choose their preferred specialist.
#The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot.

accounts = {
}

departments = {
    "General Medicine" : {
        "General Medicine Doctor 1": {
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        },
        "General Medicine Doctor 2": {
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
        },
        "General Medicine Doctor 3": {
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
        }
    },
    "Emergency Care": {
        "Emergency Care Doctor 1": {
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        },
        "Emergency Care Doctor 2": {
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
            }
        },
        "Emergency Care Doctor 3": {
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
        }
    },
    "Clinical Analysys": {
        "Clinical Analysis Doctor 1": {
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        },
        "Clinical Analysis Doctor 2":{
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        },
        "Clinical Analysis Doctor 3":{
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        }
    },
    "Cardiology": {
        "Cardiology Doctor 1": {
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        },
        "Cardiology Doctor 2":{
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        },
        "Cardiology Doctor 3":{
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        }
    },
    "Neurology": {
        "Neurology Doctor 1": {
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        },
        "Neurology Doctor 2":{
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        },
        "Neurology Doctor 3":{
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        }
    },
    "Nutrition": {
        "Nutrition Doctor 1": {
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        },
        "Nutrition Doctor 2":{
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        },
        "Nutrition Doctor 3":{
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        }
    },
    "Phisiotherapy": {
        "Phisiotherapy Doctor 1": {
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        },
        "Phisiotherapy Doctor 2":{
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        },
        "Phisiotherapy Doctor 3":{
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        }
    },
    "Traumatology": {
        "Traumatology Doctor 1": {
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        },
        "Traumatology Doctor 2":{
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        },
        "Traumatology Doctor 3":{
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        }
    },
    "Internal Medicine" : {
        "Internal Medicine Doctor 1": {
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        },
        "Internal Medicine Doctor 2":{
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        },
        "Internal Medicine Doctor 3":{
            "Monday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Tuesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Wednesday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Thursday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            },
            "Friday": {
                "Morning": ["10:00", "11:00", "12:00"],
                "Afternoon": ["14:00", "15:00", "16:00"]
            }
        }
    }
    
}
    
def login(locked):
    if locked:
        print("Your account is locked. Please try again later.")
        return
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in accounts and accounts[username] == password:
            print("Login successful!")
            break
        elif username not in accounts:
            print("Not username find in database.")
            print("Do you want to create an account?")
            decision = str(input("Enter yes or no: "))
            if decision == 'yes':
                create_account()
                break
            else:
                while attempts < 3:
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")
                    if username in accounts and accounts[username] == password:
                        print("Login successful!")
                        break
                    else:
                        print("Invalid username or password. Please try again.")
                        attempts += 1
                else:
                    print("You have exceeded the maximum number of attempts. Your account will be locked temporarily.")
                    locked = True
                    break
        elif username in accounts and accounts[username] != password:
            print("Invalid password. Please try again.")
            attempts = 0
            while attempts < 3:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if username in accounts and accounts[username] == password:
                    print("Login successful!")
                    break
                else:
                    print("Invalid username or password. Please try again.")
                    attempts += 1
            else:
                print("You have exceeded the maximum number of attempts. Your account will be locked temporarily.")
                locked = True
                break

def create_account():
    while True:
        username = input("Enter your username: ")
        if username in accounts:
            print("Username already exists. Please choose a different username.")
        else:
            break
    password = input("Enter your password: ")
    accounts[username] = password
    print("Account created successfully!")
    
def appointment():
    print("Welcome to the appointment booking system!")
    print("Please select a department:")
    for i, department in enumerate(departments, start=1):
        print(f"{i}.{department}")
    
    specialist = int(input("Enter the number: "))
    hours_for_specialist(specialist)
    
    
def hours_for_specialist(specialist):
    print(f"Please select a doctor for {departments[specialist]} department:")
    for i, doctor in enumerate([departments[specialist]], start=1):
        print(f"{i}.{doctor}")
    
    
if __name__ == "__main__":
    locked = False
    login(locked)
    appointment()