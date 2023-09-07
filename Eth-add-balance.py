import pyetherbalance

# Sign up for https://infura.io/ and get the URL to an Ethereum node
infura_url = 'https://mainnet.infura.io/v3/16b9f5ae825c496a9399139ec5549865'

# Create an pyetherbalance object, pass the infura_url
ethbalance = pyetherbalance.PyEtherBalance(infura_url)

# Read Ethereum addresses from 'output_addresses.txt' and calculate and save their balances
with open('output_addresses.txt', 'r') as input_addresses, open('output_balances.txt', 'w') as output_balances:
    for line in input_addresses:
        ethereum_address = line.strip()
        balance_eth = ethbalance.get_eth_balance(ethereum_address)
        balance_omg = ethbalance.get_token_balance('OMG', ethereum_address)
        
        # Print and save the results
        print(f"Ethereum Address: {ethereum_address}")
        print(f"ETH Balance: {balance_eth}")
        print(f"OMG Token Balance: {balance_omg}")
        
        output_balances.write(f"Ethereum Address: {ethereum_address}\n")
        output_balances.write(f"ETH Balance: {balance_eth}\n")
        output_balances.write(f"OMG Token Balance: {balance_omg}\n\n")
