# Lusitan Blockchain

Lusitan Blockchain is a decentralized cryptocurrency system implemented in Python using Flask and Django.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Proof-of-work based consensus mechanism
- Decentralized blockchain network
- Mining and transaction functionalities
- Secure digital signatures for transactions
- Flask and Django implementations for nodes

## Prerequisites

- Python 3.x
- Flask
- Django
- Postman (for testing)

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/TUR14CUS/lusitan-blockchain.git
cd lusitan-blockchain
```

2. Run the nodes:

- For Node 1:

```bash
python lusitan.py
```

- For Node 2:

```bash
python lusitan_node_5001.py
```

...

## API Endpoints

- `/mine_block`: Mine a new block.
- `/get_chain`: Retrieve the full blockchain.
- `/is_valid`: Check if the blockchain is valid.
- `/add_transaction`: Add a new transaction to the blockchain.
- `/connect_node`: Connect a new node to the blockchain network.
- `/replace_chain`: Replace the chain with the longest one in the network.

## Contributing

Contributions are welcome! Please follow the [CONTRIBUTING.md](CONTRIBUTING.md) guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
