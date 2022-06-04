import unittest
from unittest import TestCase, main
from unittest.mock import patch
from loginpage import  get_username

# Testing get_username function while  Mocking the call of the DAO

class GetUserTestCase(unittest.TestCase) :

    @patch("loginpage.DAO")
    def test_get_username(self, mocked_object) :
        mocked_object().getuser.return_value=(1,"souheil","benslamasouheil@gmail.com","hellopassword")
        #given
        expected_username ='souheil'
        #when
        result= get_username("benslamasouheil@gmail.com")
        print(result)
        #then
        self.assertEqual(expected_username,result)