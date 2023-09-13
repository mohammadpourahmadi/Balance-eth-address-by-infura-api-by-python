import pyetherbalance
#Please register for free on the infura.io site and get the api url to get the balance of Ethereum and other networks and replace its address below.
infura_url = "YOUR INFURA API URL"
balance = pyetherbalance.PyEtherBalance(infura_url)

input_filename = "listha.txt"
output_filename = "final_balance.txt"
progress_filename = "progress.txt"

# Load progress if available
try:
    with open(progress_filename, "r") as progress_file:
        last_checked_index = int(progress_file.readline())
except FileNotFoundError:
    last_checked_index = 0

with open(input_filename, "r") as input_list, open(output_filename, "a") as output_balance:
    addresses = input_list.readlines()
    total_addresses = len(addresses)
    checked_count = 0

    for index, line in enumerate(addresses):
        if index < last_checked_index:
            continue  # Skip addresses that were already checked

        ethereum_address = line.strip()
        ether_balance = balance.get_eth_balance(ethereum_address)
        print(f"Checked {index + 1}/{total_addresses}: {ethereum_address}")

        if 'balance' in ether_balance and ether_balance['balance'] > 0:
            print(f"{ethereum_address}: {ether_balance['balance']}")
            output_balance.write(f"{ethereum_address} {ether_balance['balance']}\n")

        checked_count += 1
        progress = (index + 1)  # Update progress to the current index

        # Save progress
        with open(progress_filename, "w") as progress_file:
            progress_file.write(str(progress))

print("Done! Check the 'final_balance.txt' file for results.")
