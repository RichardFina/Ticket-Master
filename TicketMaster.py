TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

# Create calculate_price function. It takes the number of tickets requested as a parameter and returns the total price

def calculate_price(tickets):

    # Create new constant for a $2 service charge and add it to the result

    result = (tickets * TICKET_PRICE) + SERVICE_CHARGE

    return result

# Run this code continuously until we run out of tickets

while tickets_remaining >= 1:

    # Output how many tickets are remaining using the tickets_remaining variable

    print("{} tickets remaining.".format(tickets_remaining))

    # Gather the user's name and assign it to a new variable

    username = input("Enter your name.\n\n")

    # Prompt the user by name and ask how many tickets they would like

    tickets_requested = input("{}, how many tickets would you like?\n\n".format(username))

    # Expect a ValueError to happen and handle it

    try:
        tickets_requested = int(tickets_requested)

        # Raise a ValueError if the request is for more tickets than are available
        if tickets_requested > tickets_remaining:
            raise ValueError("There are only {} tickets left".format(tickets_remaining))

    except ValueError as err:

        # Include error text in output

        print("We ran into an issue. {}. Please try again.\n\n".format(err))

    else:
        # Calculate the price (number of tickets multiplied by the price) and assign it to a variable

        ticket_total = calculate_price(tickets_requested)

        # Output the price to the screen

        print("Your total is: ${}\n\n".format(ticket_total))

        # Prompt the user if they want to proceed. Y/N?

        response = input("Do you want to proceed?  Y/N   ")

        # If they want to proceed print out "SOLD!" to confirm purchase

        if response.lower() == "y":
            print("SOLD!")

            # and then decrement the tickets remaining by the number of tickets purchased

            tickets_remaining -= tickets_requested

            # TODO: Gather credit card information and process it

        else:

            # Otherwise, thank them by name

            print("Thanks, {}!".format(username))

# Notify user that the tickets are sold out

print("All tickets are sold out!")