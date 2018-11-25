import random

def get_contacts():
    contacts = {}
    with open('phone_numbers.txt') as f:
        for line in f:
            t = line.strip().split()
            contacts[t[2]] = {'name':t[1], 'phone':t[0]}

    return contacts


def generate_random_transactions(n):
    contacts = get_contacts()
    transactions = []
    for i in range(0,n):
        type_of = random.choice([0,1])
        contact = contacts[random.choice(contacts.keys())]
#        print(contact)
        transactions.append([contact['phone'], contact['name'], str(type_of)])

    return transactions


def generate_history(n):
    records = generate_random_transactions(n)

    with open('history.log', 'w') as f:
        f.write('\n'.join([' '.join(x) for x in records]))
        

#generate_history(1000)

