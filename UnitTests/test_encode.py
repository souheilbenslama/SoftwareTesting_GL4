import unittest

from encodepage import encode
from decodepage import decode

class EncodeDecodeTestCase(unittest.TestCase) :
    def test_Encode_64(self) :
        #given
        input = "hello"
        type  = "64"
        expectedoutput ="aGVsbG8="
        #when
        result = encode(input,type)
        #then
        assert result==expectedoutput

    def test_Encode_32(self) :
        #given
        input = "welcome"
        type  = "32"
        expectedoutput ="O5SWYY3PNVSQ===="
        #when
        result = encode(input,type)
        #then
        assert result==expectedoutput

    def test_Encode_16(self) :
        #given
        input = "nice"
        type  = "16"
        expectedoutput ="6E696365"
        #when
        result = encode(input,type)
        #then
        assert result==expectedoutput

    def test_Decode_64(self) :
        #given
        input = "d2F0ZXI="
        type  = "64"
        expectedoutput ="water"
        #when
        result = decode(input,type)
        #then
        assert result==expectedoutput

    def test_Decode_32(self) :
        #given
        input = "O5QXIZLS"
        type  = "32"
        expectedoutput ="water"
        #when
        result = decode(input,type)
        #then
        assert result==expectedoutput

    def test_Decode_16(self) :
        #given
        input = "7761746572"
        type  = "16"
        expectedoutput ="water"
        #when
        result = decode(input,type)
        #then
        assert result==expectedoutput


