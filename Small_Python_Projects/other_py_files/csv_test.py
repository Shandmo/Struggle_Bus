import csv

existing_data = []
csv_file_path = "C:/Users/shay/Documents/Dev/Lunchies/lunch.csv"

def read_csv():
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            existing_data.append(row)

def update_data(updated_data):
    with open(csv_file_path, 'w', newline='') as csv_file:
        field_names = ['name', 'balance']
        writer = csv.DictWriter(csv_file,fieldnames=field_names)
        writer.writeheader()
        writer.writerows(updated_data)
    print(f"Data successfully updated in {csv_file_path}")

def pay_all_lunch(csv_file_path):
    deduction_amt = input("What is the deduction amount today?\n> ")
    not_eating = []
    non_eater = ""
    print("Enter names who is not eating ONE at a time. Type 'q' to stop.")
    while non_eater != 'q':
        non_eater = input("Name:\n> ")
        not_eating.append(non_eater)
    read_csv()
    # Update balances of individuals eating today
    updated_data = []
    for row in existing_data:
        name = row.get('name')
        balance = row.get('balance')
        if name and balance:
            balance = int(balance)
            if name not in not_eating:
                balance -= int(deduction_amt)
            row['balance'] = str(balance)
            updated_data.append(row)

    with open(csv_file_path, 'w', newline='') as csv_file:
        field_names = ['name', 'balance']
        writer = csv.DictWriter(csv_file,fieldnames=field_names)
        writer.writeheader()
        writer.writerows(updated_data)
    print(f"Data successfully updated in {csv_file_path}")
    update_data(updated_data)

def add_to_balance():
    read_csv()
    name = input("Enter the name:\n> ")
    amt = input("Amount to add:\n> ")

    updated_data = []
    for row in existing_data:
        if row['name'] == name:
            balance = int(row['balance'])
            balance += int(amt)
            row['balance'] = str(balance)
            print(f"Updated balance for {name}: {balance}")
        updated_data.append(row)
    update_data(updated_data)

def menu_options():
    while True:
        option = input("\n=====Options=====\n1 = Pay Everyone's Lunch\n2 = Add to Balance\n3 = Exit\n> ")
        if option == '1':
            pay_all_lunch()
        elif option == '2':
            add_to_balance()
        elif option == '3':
            exit()
        else:
            print("Invalid option.")

menu_options()


