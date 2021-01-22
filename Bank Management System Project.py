#Code by IG@kamran_hccp
# DATABASE account holders
customerNames = ['HASNAT', 'KAMRAN', 'FIZZA', 'RAZA', 'HAMZA', 'ASMA', 'HAIDER', 'ADIL', 'LAIBA', 'ALEESHA', 'HASNAIN',
                 'ABUZAR']
customerAccType = ['S', 'Y', 'Y', 'C', 'S', 'C', 'S', 'Y', 'S', 'S', 'S', 'C']
customerAge = [18, 17, 17, 18, 19, 18, 18, 17, 20, 19, 20, 20]
customerPins = ['0123', '2575', '7275', '5049', '3453', '2533', '4363', '5334', '8006', '4646', '5456', '5444']
customerPhNumber = ['31787382', '3242223', '23223232', '32323222', '54532242', '22433537', '434343366', '64764644',
                    '747844684', '67454635', '53533337', '353630953']
customerBalances = [10000, 20000, 40000, 10000, 23003, 20000, 90000, 23000, 54005, 45005, 12000, 54000]
adminID = ['kamran79', 'hasnat78', 'raza23']
adminPassword = ['kam123', 'has321', 'faz453']
deposition = 0
withdrawal = 0
balance = 0
i = 0

#Code by IG@kamran_hccp
# This statement in program run continuously
while True:
    # Welcome Note for our banking system
    print("  *********************************   ")
    print("| Welcome to COMSATS Banking System | ")
    print("  ********************************* \n")
    print("<===========================>")
    print("1. Open a New account        ")
    print("2. Withdraw Money            ")
    print("3. Deposit Money             ")
    print("4. Check Customers & Balance ")
    print("5. Exit/Quit                 ")
    print("<===========================>")
    # The below statement takes the choice number from the user.
    choiceNumber = input("Select your Choice: ")

    # for Opening Account
    if choiceNumber == "1":
        print("Greetings!Customer wants to Open a New Account.\n")

        print("<==Account Type==>  \n"
              "A. Current Account. \n"
              "B. Savings Account. \n"
              "C. Youth Account.     ")
        #Code by IG@kamran_hccp
        #for account selection whether SAVING, CURRENT or YOUTH Account
        account_type = input("Enter your Account Type(C/S/Y): ")
        if account_type.upper() == "Y":
            verification_age = input("Enter your Age(for Verification): ")
            if verification_age <= "18" and verification_age >= "14":
                print("Nice! You are Eligible for Youth Account opening.")
                # These few lines will take information from customer and then append them to the list.
                print("\nPlease Enter Correct Details for Account!")
                customerAccType.append("Y")
                name = input("Enter your Full Name: ")
                customerNames.append(name)
                age = (input("Enter your Age: "))
                customerAge.append(eval(age))
                phNumber = eval(input("Enter your Ph. Number: "))
                customerPhNumber.append(phNumber)
                pin = str(input("Create a 4 Digit Pin for your Account: "))
                customerPins.append(pin)
                balance = 0
                deposition = eval(input("Enter Amount(>= 100-/Rs) to Deposit: "))
                if deposition < 100:
                    print("Please! Enter amount >= 100.")
                else:
                   balance = balance + deposition
                customerBalances.append(balance)
                print("\n====================")
                print("Name:", name, end=" \n")
                print("Ph.Number:", phNumber, end=" \n")
                print("Pin:", str(pin), end=" \n")
                print("Balance:", str(balance), end=" -/Rs\n")
                print("Account Type:", str(account_type.upper()), end=" \n")
                print("=====================")

                # print("New account created successfully!")
                #Code by IG@kamran_hccp
                print("Youth Account Created SuccessfulL! Details added to System!")
                print("\n")
                print("Note! Please remember your Pin!")
                print("<=====================================>")
        elif account_type.upper() == "C":
            verification_age = input("Enter your Age(for Verification): ")
            if verification_age > "18" and verification_age != "18":
                print("Nice! You are Eligible for Current Account opening.")
                # These few lines will take information from customer and then append them to the list.
                print("\nPlease Enter Correct Details for Account!")
                customerAccType.append("C")
                name = input("Enter your Full Name: ")
                customerNames.append(name)
                age = (input("Enter your Age: "))
                customerAge.append(eval(age))
                phNumber = eval(input("Enter your Ph. Number: "))
                customerPhNumber.append(phNumber)
                pin = str(input("Create a 4 Digit Pin for your Account: "))
                customerPins.append(pin)
                balance = 0
                deposition = eval(input("Enter Amount(>= 1000-/Rs) to Deposit: "))
                if deposition < 1000:
                    print("Please! Enter amount >= 1000.")
                else :
                    balance = balance + deposition
                customerBalances.append(balance)
                print("\n====================")
                print("Name:", name, end=" \n")
                print("Ph.Number:", phNumber, end=" \n")
                print("Pin:", str(pin), end=" \n")
                print("Balance:", str(balance), end=" -/Rs\n")
                print("Account Type:", str(account_type.upper()), end=" \n")
                print("=====================")

                # print("New account created successfully!")
                print("Current Account Created SuccessfulL! Details added to System!")
                print("\n")
                print("Note! Please remember your Pin!")
                print("<=====================================>")
        elif account_type.upper() == "S":
            verification_age = input("Enter your Age(for Verification): ")
            if verification_age > "18" and verification_age != "18":
                print("Nice! You are Eligible for Saving Account opening.")
                # These few lines will take information from customer and then append them to the list.
                print("\nPlease Enter Correct Details for Account!")
                customerAccType.append("S")
                name = input("Enter your Full Name: ")
                customerNames.append(name)
                age = (input("Enter your Age: "))
                customerAge.append(eval(age))
                phNumber = eval(input("Enter your Ph. Number: "))
                customerPhNumber.append(phNumber)
                pin = str(input("Create a 4 Digit Pin for your Account: "))
                customerPins.append(pin)
                balance = 0
                deposition = eval(input("Enter Amount(>= 500-/Rs) to Deposit: "))
                if deposition < 500:
                    print("Please! Enter amount >= 500.")
                else:
                    balance = balance + deposition
                customerBalances.append(balance)
                print("\n====================")
                print("Name:", name, end=" \n")
                print("Ph.Number:", phNumber, end=" \n")
                print("Pin:", str(pin), end=" \n")
                print("Balance:", str(balance), end=" -/Rs\n")
                print("Account Type:", str(account_type.upper()), end=" \n")
                print("=====================")

                # print("New account created successfully!")
                print("Saving Account Created SuccessfulL! Details added to System!")
                print("\n")
                print("Note! Please remember your Pin!")
                print("<=====================================>")
                #Code by IG@kamran_hccp
        else:
            print("You are not eligible for Account Opening.\n")

        # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Enter any Key to Continue to Main Menu...")


    # For Withdrawing Money
    elif choiceNumber == "2":
        j = 0
        print("You wants to Withdraw Money.")
        # This while loop will prevent the user using the account if the username or pin is wrong.
        while j < 1 :
            k = -1
            name = input("Please Enter Account Holder Name: ")
            pin = input("Please Enter Account Pin: ")
            # This while loop will keep the function running when variable k is smaller than length of the
            # customerNames list.
            while k < len(customerNames) - 1 :
                k = k + 1
                # These two if conditions find where both the name and pin matches.
                if name.upper() == customerNames[k] :
                    if pin == customerPins[k] :
                        j = j + 1
                        #Code by IG@kamran_hccp
                        # These few statement would show the balance taken from the list.
                        print("Your Current Balance:", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs\n")
                        balance = (customerBalances[k])
                        # Statement below would take the amount to withdraw from user.
                        withdrawal = eval(input("Input Amount you want to Withdraw: "))
                        # The if condition below would look whether the withdraw is greater than the balance.
                        if withdrawal > balance :
                            # This statement below would take a deposition from the customer.
                            deposition = eval(input(
                                "Please Deposit a higher Value because your Balance mentioned above is not enough: "))
                            # These few statements would update the value and show the balance to user.
                            balance = balance + deposition
                            print("Your Current Balance:", end=" ")
                            print(balance, end=" ")
                            print("-/Rs\n")
                            balance = balance - withdrawal
                            print("-\n")
                            print("<---Withdraw Successfull!--->")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n")
                            #Code by IG@kamran_hccp
                        else :
                            # Else condition mentioned above is to do withdrawal if the balance is greater than the
                            # withdraw amount.
                            balance = balance - withdrawal
                            # These few statement would update the values in the list and show it to the customer.
                            print("\n")
                            print("<---Withdraw Successfull!--->")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n")
            if j < 1 :
                # The if condition above would work when the pin or the name is wrong.
                print("Account Holder Name and Pin does not match! Try Again>>\n")
                break

        mainMenu = input("Enter any Key to Continue to Main Menu...") #main menu


    # For Depositing Money
    elif choiceNumber == "3":
        print("You wants to Deposit Amount!")
        n = 0
        #Code by IG@kamran_hccp
        # The while loop below would work when the pin or the username is wrong.
        while n < 1:
            k = -1
            name = input("Please Enter Account Holder Name: ")
            pin = input("Please Enter Account Pin: ")
            # The while loop below will keep the function running to find the correct user.
            while k < len(customerNames) - 1 :
                k = k + 1
                # The two if conditions below would find whether both the pin and the name is correct.
                if name.upper() == customerNames[k] :
                    if pin == customerPins[k] :
                        n = n + 1
                        # These statements below would show the customer balance and update list values according to
                        # the deposition made.
                        print("Your Current Balance: ", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs")
                        balance = (customerBalances[k])
                        # This statement below takes the depositionn from the customer.
                        deposition = eval(input("Enter the Amount you want to Deposit: "))
                        balance = balance + deposition
                        customerBalances[k] = balance
                        print("\n")
                        print("<---Deposit Successful!--->")
                        print("Your New Balance: ", balance, end=" ")
                        print("-/Rs\n")
            if n < 1:
                print("Account Holder Name and Pin does not match! Try Again>>\n")
                break

        #Code by IG@kamran_hccp
        mainMenu = input("Enter any Key to Continue to Main Menu...") #main menu


    #Code by IG@kamran_hccp
    # For customrers List
    elif choiceNumber == "4":
        print()
        print("This Panel is for Administration ONLY!")
        admin_name_admin = input("Please Enter Admin ID: ")
        admin_pin_admin = input("Please Enter Admin Password/PIN: ")
        if admin_name_admin in adminID and admin_pin_admin in adminPassword :
            # The while loop below will keeping running until all the customers and balances are shown.
            print("Customer Names and Balance: ")
            k = 0
            while k <= len(customerNames) - 1:
                print("->Customer =", customerNames[k])
                print("->Balance =", customerBalances[k], end=" ")
                print("-/Rs")
                print("\n")
                k = k + 1
                print("")
                #Code by IG@kamran_hccp
        else:
            print("\nYou enter Wrong Admin ID or Password!")
            print("System Closed!")
            print("\n")
        mainMenu = input("Enter any Key to Continue to Main Menu...")  # Menu code



    # For closing/Quiting system
    #Code by IG@kamran_hccp
    elif choiceNumber == "5":
        # These statements would be just showed to the customer.
        print("Thank you for using COMSATS Banking System!")
        print("Hope to see you Again :)")
        print( )
        break
    else:
        # This else function above would work when a wrong function is chosen.
        print("Invalid Option Selected!")
        print("Please Try again!")
        # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Enter any Key to Continue to Main Menu...")

                
        #Code by IG@kamran_hccp
