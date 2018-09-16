"""
 This is a simple BlockChain demo.
 Author: victordo
 Date: 2018-09-15
"""

import hashlib
import datetime

class Block:
	"""
	this is a class for blocks in BlockChain.
	pre_hash: the hash value of the previous block in the BlockChain
	data: the context contain in the block
	"""
	def __init__(self, data, pre_hash):
		self.pre_hash = pre_hash
		self.data = data
	
	# compute the hash of the block
	@property
	def hash(self):
		hash_value = hashlib.sha256()
		hash_value.update(self.data.encode('utf-8'))
		return hash_value.hexdigest()
		
def create_first_block():
	"""
	create the very first block in a BlockChain. so it have not previous hash.
	"""
	return Block(data="The first block", pre_hash="")
	
# define the construct of BlockChain
class BlockChain:
	"""
	BlockChain:[ block01-->block02-->...-->blockN]
	"""
	def __init__(self):
		self.blocks =[create_first_block()]
		
	def add_block(self, data):
		pre_block = self.blocks[-1]
		new_block = Block(data, pre_block.hash)
		self.blocks.append(new_block)
		return new_block

if __name__=='__main__':
	blockchain = BlockChain()
	
	block01 = blockchain.add_block("A borrow B $100 at" + str(datetime.datetime.now()))
	block02 = blockchain.add_block("C borrow B $100 at" + str(datetime.datetime.now()))
	
	for b in blockchain.blocks:
		print("Previous Hash: {}".format(b.pre_hash))
		print("Data: {}".format(b.data))
		print("Hash value: {}".format(b.hash))
		print("\n")
		
"""
Result: 

Previous Hash:
Data: The first block
Hash value: 978d890577d94e71777675e9db4e12884c4e7d59dd02fd75e64f3a604d56806f


Previous Hash: 978d890577d94e71777675e9db4e12884c4e7d59dd02fd75e64f3a604d56806f
Data: A borrow B $100 at2018-09-16 10:33:43.954711
Hash value: aeac14fbf1fa60c66bfeadf17ca7320e8e259fbac2a572d589e758f2e59d735e


Previous Hash: aeac14fbf1fa60c66bfeadf17ca7320e8e259fbac2a572d589e758f2e59d735e
Data: C borrow B $100 at2018-09-16 10:33:43.974712
Hash value: ddb1ab724ea9126e74e940bfd6895f7d0f3fc3b20b9e6870719ead053a54bf25
"""
