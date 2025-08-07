import datetime

def log_action(action):
    now = datetime.datetime.now()
    with open("data/log.txt", "a") as log_file:
        log_file.write(f"[{now}] {action}\n")
