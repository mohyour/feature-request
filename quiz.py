# Debugging solution
from cryptography.fernet import Fernet

chars = [104, 116, 116, 112, 115, 58, 47, 47, 101, 110, 103, 105, 110, 101,
         101, 114, 105, 110, 103, 45, 97, 112, 112, 108, 105, 99, 97, 116,
         105, 111, 110, 46, 98, 114, 105, 116, 101, 99, 111, 114, 101, 46, 99,
         111, 109, 47, 113, 117, 105, 122, 47, 115, 100, 102, 103, 119, 114,
         52, 52, 104, 114, 102, 104, 102, 104, 45, 119, 115]


def getString():
    string = ''
    for i in chars:
        string += chr(i)
    print(string)

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='


# Oh no! The code is going over the edge! What are you going to do?
message =b'gAAAAABc6v8QRsDcKfRDbpBYP1XmZ0_9sO-QkTONDYIyqoN6P9OOAFuBuA9jSIxcG\
    CQNI-VBwqiOlMhO09IwHU7zbznZqaDq4YPO1As7KJL20JxQzwbm2aDqtR-jneit7CPNd9EZFHv\
    7I4uE2GbeTBvy7g0vMt9lytJ466mIh3kHCZVrHdpZ3bp6PxVeSFurQ0NZ6oublJD2'


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    getString()
    main()
