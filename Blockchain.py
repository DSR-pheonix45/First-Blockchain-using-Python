import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block", self.calculate_hash(0, "0", int(time.time()), "Genesis Block"))

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = self.calculate_hash(new_block.index, new_block.previous_hash, int(time.time()), new_block.data)
        self.chain.append(new_block)

    def calculate_hash(self, index, previous_hash, timestamp, data):
        value = str(index) + str(previous_hash) + str(timestamp) + str(data)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != self.calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Create a blockchain and add some blocks
my_blockchain = Blockchain()
my_blockchain.add_block(Block(1, my_blockchain.get_latest_block().hash, int(time.time()), "Transaction 1", ""))
my_blockchain.add_block(Block(2, my_blockchain.get_latest_block().hash, int(time.time()), "Transaction 2", ""))
my_blockchain.add_block(Block(3, my_blockchain.get_latest_block().hash, int(time.time()), "Transaction 3", ""))

# Print the blockchain
for block in my_blockchain.chain:
    print(f"Block Index: {block.index}")
    print(f"Block Timestamp: {block.timestamp}")
    print(f"Block Data: {block.data}")
    print(f"Block Hash: {block.hash}")
    print(f"Previous Block Hash: {block.previous_hash}")
    print()

# Validate the blockchain
print(f"Blockchain is valid: {my_blockchain.validate_chain()}")
