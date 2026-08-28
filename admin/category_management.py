from database import categories


def add_category():

    category = input("Enter category: ")

    if category in categories:
        print("Category was already exists")
        return

    categories.append(category)

    print("Category added successfully")


def view_categories():

    if not categories:
        print("No categories available")
        return

    for category in categories:
        print(category)


def delete_category():

    category = input("Enter category: ")

    if category in categories:

        categories.remove(category)

        print("Category was deleted successfully")

    else:
        print("Category was not found")