#Decrypt messageusing RSA Algorithm
message = int(input("Input encryption:"))

print("Input the private key:")
private_key1, private_key2 = int(input("Part 1:")), int(input("Part 2:"))

decryption = (int(message)**private_key1) % private_key2

print(decryption)