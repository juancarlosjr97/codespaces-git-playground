from datetime import datetime

if __name__ == "__main__":
    current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M")
    message = f"Congratulations, you are running the a python script from a GitHub Codespace environment. Now, it is {current_datetime} and time for further development."
    
    print(message)
