import hashlib

class Cypher:
    def __init__(self, passphrase):
        self.plainText = []
        self.cypherText = []
        self.binary = []
        self.init = ""
        self.generate_init_from_words(passphrase)

    def to_binary_array(self, data):
        self.binary = []
        for byte in data:
            tmp = bin(byte)[2:]  # get binary representation and strip the '0b' prefix
            if len(tmp) < 8:
                tmp = '0' * (8 - len(tmp)) + tmp
            self.binary.append(tmp)

    def generate_init_from_words(self, words):
        # Hash the input words
        hash_object = hashlib.sha1(words.encode())
        hash_digest = hash_object.hexdigest()

        # Convert the hash digest to a binary string
        binary_hash = bin(int(hash_digest, 16))[2:].zfill(160)  # 160 bits for SHA-1

        # Truncate or extend to 40 bits
        self.init = binary_hash[:40]
        print(f"Generated initial state: {self.init}")

    def get_key(self, f_byte):
        arr = list(self.init)
        init_arr = [int(char) for char in arr]
        builder = []
        new_array = [0] * len(init_arr)

        for _ in f_byte:
            res = ((init_arr[0] ^ init_arr[19]) ^ init_arr[21]) ^ init_arr[38]
            builder.append(init_arr[0])

            for i in range(1, len(init_arr)):
                new_array[i - 1] = init_arr[i]

            new_array[-1] = res
            init_arr = new_array[:]

        key = ''.join(map(str, builder))
        self.init = ''.join(map(str, init_arr))
        return key

    def encrypt(self, data):
        self.cypherText = []
        self.to_binary_array(data)
        for binary_str in self.binary:
            self.get_cypher_value(binary_str)
        return bytes(self.cypherText)

    def get_cypher_value(self, f_byte):
        key = self.get_key(f_byte)
        f_byte_arr = list(f_byte)
        key_arr = list(key)
        builder = []

        for f, k in zip(f_byte_arr, key_arr):
            tmp = int(f) ^ int(k)
            builder.append(str(tmp))

        value = int(''.join(builder), 2)
        self.cypherText.append(value)

    def decrypt(self, data):
        # Decryption is essentially the same process as encryption in XOR
        return self.encrypt(data)