import sys

DATAFILE = 'contacts.txt'

def load_datafile():
    contacts = {}

    try:
        with open(DATAFILE, 'r') as f:
            for line in f:
                words = line.split()
                name = words[0]
                emails = words[1:]
                contacts[name] = emails
    except FileNotFoundError:
        pass

    return contacts


def save_datafile(contacts):
    with open(DATAFILE, 'w') as f:
        for name, emails in contacts.items():
            f.write("{} {}\n".format(name, ' '.join(emails)))


def add_new_contact(contacts, name, email):
    email_list = contacts.get(name, [])
    email_list.append(email)
    contacts[name] = email_list


def get_mail_for_contact(contacts, name):
    print("Emails: {}".format(contacts.get(name)))


contacts = load_datafile()
if len(sys.argv) == 2:
    get_mail_for_contact(contacts, sys.argv[1])
elif len(sys.argv) > 2:
    add_new_contact(contacts, sys.argv[1], sys.argv[2])
    save_datafile(contacts)
else:
    sys.exit("Missing name")

