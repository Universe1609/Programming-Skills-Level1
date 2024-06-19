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

#creando db de citas:
appointments = {
}

departments = {
    "General Medicine" : {
        "General Medicine Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "General Medicine Doctor 2": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "General Medicine Doctor 3": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        }
    },
    "Emergency Care": {
        "Emergency Care Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Emergency Care Doctor 2": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Emergency Care Doctor 3": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        }
    },
    "Clinical Analysys": {
        "Clinical Analysis Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Clinical Analysis Doctor 2":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Clinical Analysis Doctor 3":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        }
    },
    "Cardiology": {
        "Cardiology Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Cardiology Doctor 2":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Cardiology Doctor 3":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        }
    },
    "Neurology": {
        "Neurology Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Neurology Doctor 2":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Neurology Doctor 3":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        }
    },
    "Nutrition": {
        "Nutrition Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Nutrition Doctor 2":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Nutrition Doctor 3":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        }
    },
    "Phisiotherapy": {
        "Phisiotherapy Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Phisiotherapy Doctor 2":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Phisiotherapy Doctor 3":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        }
    },
    "Traumatology": {
        "Traumatology Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Traumatology Doctor 2":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Traumatology Doctor 3":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        }
    },
    "Internal Medicine" : {
        "Internal Medicine Doctor 1": {
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Internal Medicine Doctor 2":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                }
        },
        "Internal Medicine Doctor 3":{
            "Monday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Tuesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Wednesday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Thursday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
                },
            "Friday": {
                "Morning" : ["10:00", "11:00", "12:00"],
                "Afternoon" : ["14:00", "15:00", "16:00"]
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
    departments_list = list(departments.keys())
    for i, department in enumerate(departments_list, start=1):
        print(f"{i}.{department}")
    
    choice = int(input("Enter the number: "))
    specialist = departments_list[choice - 1]
    doctor_for_specialist(specialist)
    
    
def doctor_for_specialist(specialist):
    print(f"Please select a doctor for {specialist} department:")
    doctor_list = list(departments[specialist].keys())
    for i, doctor in enumerate(doctor_list, start=1):
        print(f"{i}.{doctor}")
    
    choice = int(input("Enter the number: "))
    doctor = doctor_list[choice - 1]
    day_for_doctor(doctor,specialist)
    
def day_for_doctor(doctor,specialist):
    print(f"Please select a day for {doctor}:")
    day_list = list(departments[specialist][doctor].keys())
    for i, time_slot in enumerate(day_list, start=1):
        print(f"{i}.{time_slot}")
    
    choice = int(input("Enter the number: "))
    day = day_list[choice - 1]
    time_slot_for_day(day, doctor, specialist)
    
def time_slot_for_day(day, doctor, specialist):
    print(f"Please select a time slot for {day}:")
    time_slot_for_day = list(departments[specialist][doctor][day].keys())
    for i, time_slot in enumerate(time_slot_for_day, start=1):
        print(f"{i}.{time_slot}")
    choice = int(input("Enter the number: "))
    time = time_slot_for_day[choice - 1]
    hours_slot_for_time(day, doctor, specialist, time)

def hours_slot_for_time(day, doctor, specialist, time):
    print(f"Please select a time slot:")
    time_slot_list = list(departments[specialist][doctor][day][time])
    for i, hours_slot in enumerate(time_slot_list, start=1):
        print(f"{i}.{hours_slot}")
    choice = int(input("Enter the number: "))
    hours = time_slot_list[choice - 1]
    print(f"Your appointment is scheduled for {day} at {time} at {hours} with {doctor}.")
    print("Thank you for your appointment!")
    

    choice = int(input("Enter the number: "))
    time_slot = time_slot_list[choice - 1]
    
    print("Thank you for your appointment!")
    
if __name__ == "__main__":
    locked = False
    login(locked)
    appointment()
    print("Do you want to make another appointment? ")
    decision = str(input("Enter yes or no: "))
    if decision == 'yes':
        appointment()