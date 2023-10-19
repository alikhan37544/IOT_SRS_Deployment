# access_control.py

class AccessControlSystem:
    def __init__(self):
        self.users = {
            "user1": "password1",
            "user2": "password2",
            # Add more users as needed
        }

    def grant_access(self, username, password):
        if username in self.users and self.users[username] == password:
            print(f"Access granted for {username}")
        else:
            print(f"Access denied for {username}")

# Example usage
if __name__ == "__main__":
    access_system = AccessControlSystem()

    # User input for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Grant or deny access based on user input
    access_system.grant_access(username, password)
