day=int(input("Enter a number b/w(1-7): "))
match day:
    case 1:
        print("Its Monday")
    case 2:
        print("Its Tuesday")
    case 3:
        print("Its Wednesday")
    case 4:
        print("Its Thursday")
    case 5:
        print("Its Friday")
    case 6:
        print("Its Saturday")
    case 7:
        print("Its Sunday")
    case _:
        print("Enter a valid number")

command = input("Enter the command(start or stop): ")

match command:
    case "start":
        print("🚀 System is booting up...")
        print("Please wait a moment.")
    case "stop":
        print("🛑 Shutting down immediately.")
    case _:
        print("❓ Unknown command entered.")
    