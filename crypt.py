# модуль для шифрования и дешифровки json при общении с базой данных

import rsa

pubkey_pem = b'-----BEGIN RSA PUBLIC KEY-----\nMEgCQQCKLRf5ksOaYURJrbBR/TMDTqHH5OF2H+/Ez4dyYLyQpsrMWRUPFd9PTpnG\nhj9g/oLGkL6Vpak8OECBIOE9MF2RAgMBAAE=\n-----END RSA PUBLIC KEY-----\n'
privkey_pem = b'-----BEGIN RSA PRIVATE KEY-----\nMIIBPAIBAAJBAIotF/mSw5phREmtsFH9MwNOocfk4XYf78TPh3JgvJCmysxZFQ8V\n309OmcaGP2D+gsaQvpWlqTw4QIEg4T0wXZECAwEAAQJAPbl/KEHjlyc0NiWcykNt\ncmDB7GXWQcpqdWSvgOytYSB9YhXlR3DWkSN0T6rTrMaUZBmIkhDo7NsSUGnzQQOY\nAQIjAPcVizgwsIAYu1AC9XqXor8VXVOj4sNldUMooOCANFkJ77ECHwCPKYFCV+vm\neWwDkbAgeG1P374FWEOZF5rIujoHo+ECIwDG9FcE6NfGXaO+WpOVojIO0UIzzhwT\nIEgaysU34KPGKmURAh5B5oEx4PceaNZn7jB9QfJPylbWbwLu/gaqT89WpQECIl39\n7dG4cT+e8QNojEf6RrNvuR+hMYa5y83/jccDiZK5KdI=\n-----END RSA PRIVATE KEY-----\n'
pubkey = rsa.PublicKey.load_pkcs1(pubkey_pem, 'PEM')
privkey = rsa.PrivateKey.load_pkcs1(privkey_pem, 'PEM')


def encrypt_dict(dictionary):
    encrypted_dict = {}
    for key in dictionary:
        encrypted_dict[key] = rsa.encrypt(str(dictionary[key]).encode('utf8'), pubkey)
    return encrypted_dict


def decrypt_dict(dictionary):
    decrypted_dict = {}
    for key in dictionary:
        item = rsa.decrypt(dictionary[key], privkey)
        decrypted_dict[key] = item.decode('utf8')
    return decrypted_dict


