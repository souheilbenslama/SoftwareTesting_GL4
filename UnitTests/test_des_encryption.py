import unittest

from encryptingdes import encrypt

class DesEncryptionTestCase(unittest.TestCase) :
    def test_DES_encryption(self) :
        #given
        message = "hello world !"
        key  = "hello"
        expectedoutput =b"RK2V6BQ22UALSHNH5YGKQRMPF4======"
        #when
        result = encrypt(message,key)
        #then
        assert result== expectedoutput


