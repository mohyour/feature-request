# Debugging solution
from cryptography.fernet import Fernet

chars = [ 104, 116, 116, 112, 115, 58, 47, 47, 101, 110, 103, 105, 110, 101,
          101, 114, 105, 110, 103, 45, 97, 112, 112, 108, 105, 99, 97, 116,
          105, 111, 110, 46, 98, 114, 105, 116, 101, 99, 111, 114, 101, 46, 99,
          111, 109, 47, 113, 117, 105, 122, 47, 115, 100, 102, 103, 119, 114,
          52, 52, 104, 114, 102, 104, 102, 104, 45, 119, 115 ]


def getString():
    string = ''
    for i in chars:
        string += chr(i)
    print(string)

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcHLYPf3S-szfPRYhB1fLWMkyoVb_YNcYONtoM1tMCY5XhpDwN6YejQD_3F2ubuQ7_7ZFiTUOOgPrkKg9IGlz5xs2bXwtIhmYlwrEYw14K2DRIBnB7UIeo1P9Z9k7LHLX9tbU08cbjUQZNmt9txLcHfEXcqjEGGR3xqpUDJhIsDDJo_SOWaHQq3QWAJaPxsmFQbAYQ'

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    getString()
    main()
