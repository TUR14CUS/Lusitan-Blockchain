import datetime
import hashlib
import json

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from uuid import uuid4
from urllib.parse import urlparse

app = Flask(__name__)
api = Api(app)

class Blockchain(Resource):
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.nodes = set()

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash,
            'transactions': self.transactions
        }
        self.transactions = []
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha3_256((str(new_proof**2 - previous_proof**2)).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha3_256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        for block in chain[1:]:
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof, proof = previous_block['proof'], block['proof']
            hash_operation = hashlib.sha3_256((str(proof**2 - previous_proof**2)).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
        return True

    def add_transaction(self, sender, receiver, amount, signature):
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'signature': signature
        }
        if not self.valid_transaction(transaction):
            return "Invalid transaction", 400
        self.transactions.append(transaction)
        return self.get_previous_block()['index'] + 1

    def mine_block(self):
        previous_block = self.get_previous_block()
        previous_proof = previous_block['proof']
        proof = self.proof_of_work(previous_proof)
        previous_hash = self.hash(previous_block)
        self.add_transaction(sender=node_address, receiver='Hadelin', amount=1, signature="digital_signature")
        block = self.create_block(proof, previous_hash)
        return block

    def add_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def consensus(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)
        for node in network:
            response = requests.get(f'http://{node}/blockchain')
            if response.status_code == 200:
                length, chain = response.json()['length'], response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_length, longest_chain = length, chain
        if longest_chain:
            self.chain = longest_chain
            return True
        return False

api.add_resource(Blockchain, '/blockchain')

if __name__ == '__main__':
    node_address = str(uuid4()).replace('-', '')
    blockchain = Blockchain()
    app.run(host='0.0.0.0', port=5004)
