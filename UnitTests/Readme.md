# TP Software Testing
## Unit Testing 


 Unit test is a way of testing a unit - the smallest piece of code that can be logically isolated in a system.


I started by testing some isolated and independent encryption and encoding functions by creating unit tests using the unittest package. 
example : 
```python
 def test_Encode_64(self) :
        #given
        input = "hello"
        type  = "64"
        expectedoutput ="aGVsbG8="
        #when
        result = encode(input,type)
        #then
        assert result==expectedoutput
```

I then tried to create a unit test for a get_username function that depends on another DAO function that makes the actual call to the database. 
Since unit tests are supposed to test only the code of the function and not its dependency, and since they need to check if the logic function is working properly or not. i had to simulate the DAO function call. 


To do this i first patched the call using the Decorator patch so that the test will not execute the DAO function call. 

 ```python
    @patch("loginpage.DAO")
    def test_get_username(self, mocked_object) :
  ```

Then we pass the mock object and override the return value of the get-user function.



 ```python
    def test_get_username(self, mocked_object) :
        mocked_object().getuser.return_value=(1,"souheil","benslamasouheil@gmail.com","hellopassword")
 
  ```
  