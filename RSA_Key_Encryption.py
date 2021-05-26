publickey = input()

class encryption:
    keyvalues = publickey

    def __init__(self):
        self.message = message
        self.byte_message = byte_message

    @classmethod
    def inputKeys(cls, key):
        cls.keyvalues = key


''''#Encrypt your message using the RSA Algorith
message = bytes(input("Type message you want encrypted:"), "utf-8")

the_int = int.from_bytes(message, "big")

print(the_int)

#input the public key for encryption
print("Input the public key:")
public_key1, public_key2 = int(input("Part 1:")), int(input("Part 2:"))

#encrypt message with RSA
encryption = (int(message)**public_key1) % public_key2


print("Your encrypted message is:")
print(encryption)'''