import os

print("Welcome to Todo list.")
Q = input("Do you have an account? \n$ ").lower()
while True:
    if Q in ("yes", "y", "ye", "ys"):
        print("""Connect with Gmail => [1]
Connect with Facebook => [2]
Connect with Apple => [3]""")
        q = int(input("Sign in with: "))
        if q == 1:
            print("     Google")
            email = input("Email: ").strip()
            psw = input("Password: ").strip()
            break

        elif q == 2:
            print("     Facebook")
            email = input("Email: ").strip()
            psw = input("Password: ").strip()
            break

        elif q == 3:
            print("     Apple")
            email = input("Email: ").strip()
            psw = input("Password: ").strip()
            break



