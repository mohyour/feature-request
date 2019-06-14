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
message = b'gAAAAABdA6Xw9rCM3j4P1mFARwXzccJhD6JkAsUZ6M7NtBhBQMml6DRZNUZ05CzSax\
          6yuuk8w88qPG1HtMFI3RgMo5aXTx4J-TrVnFLdZ7f7T--aJ-gZCpU2cRCeXcPaRi6QNK\
          NqwwF5hFfLfOb7R_YfzRYROZ2s5hFgtSNEb2Ev_41itG7bxFT7S7WFvvNpCQKuOME0Sm\
          P2'


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    getString()
    main()
