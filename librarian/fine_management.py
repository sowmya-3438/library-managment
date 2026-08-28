from database import fines


def add_fine():

    username = input("Enter member username: ")

    try:
        days = int(input("Enter late days: "))
    except ValueError:
        print("Enter a valid number")
        return

    if days <= 0:
        print("No fine required")
        return

    amount = days * 5

    fine = {
        "username": username,
        "days": days,
        "amount": amount
    }

    fines.append(fine)

    print("Fine added successfully")
    print("Fine amount:", amount)


def view_fines():

    print("\nFINES ")

    if not fines:
        print("No fines available")
        return

    for fine in fines:

        
        print("Username :", fine["username"])
        print("Late Days:", fine["days"])
        print("Amount   :", fine["amount"])