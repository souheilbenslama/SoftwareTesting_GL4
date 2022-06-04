import pytest
from dbconnection import DAO

@pytest.fixture(scope='session' ,)
def test_DAO() :
    # creating a new db connection
    DAO_obj=DAO()
    # in case you need to create table in database
    #DAO_obj.createTable()
    # add a new user to database
    #DAO_obj.register( 'souheil' , 'souheil' , 'benslamasouheil@gmail.com' , '73ceb15f18bb0a313c8880abe54bf61a529dd8f1e75b084dd39926a1518d3d2f','99728986')
    yield DAO_obj
    # close the data base cnx after finishing all tests
    DAO_obj.db.close()

def test_add_user(test_DAO):
    # given boolean because our register methode doesn't return the new user who needs to login after register
    expected_user= True
    # when
    result = test_DAO.register( 'souheil23' , 'souheil23' , 'benslamasouheil2233@gmail.com' , '73ceb15f18bb0a313c8880abe54bf61a529dd8f1e75b084dd39926a1518d3d2f','99728986')
    print(result)
   # then
    assert(result,expected_user)



def test_get_user(test_DAO):
    # given
    expected_user= (1, 'souheil', 'souheil', 'benslamasouheil@gmail.com', '99728986', '73ceb15f18bb0a313c8880abe54bf61a529dd8f1e75b084dd39926a1518d3d2f', None)
    # when
    result = test_DAO.getuser("benslamasouheil@gmail.com")
    print(result)
   # then
    assert(result,expected_user)
