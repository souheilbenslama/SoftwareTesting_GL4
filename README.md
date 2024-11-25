# PentRacker
A desktop application in python that provides some security functionalities.
## Functionalities
- Double factor authentification
- Encoding / Decoding (Base 64, Base 32, Base 16)
- Hashing / Cracking (MD5, SHA1, SHA256)
- Symetric encryption / decryption (DES, AES)
- Asymetric encryption / decryption (EL GAMAL, RSA)
- Secure chat room (AES based)
## Requirements
- MySQL server (dbconnection.py)
- Run SQL commands : 
   ```
  create table users (id  integer PRIMARY KEY AUTO_INCREMENT , nom varchar(50) NOT NULL , prenom  varchar(50),email varchar(50) NOT NULL UNIQUE ,numero varchar(8) NOT NULL , password varchar(256) NOT NULL ,  code varchar(6) NOT NULL );
  create table clepubs (id  integer PRIMARY KEY AUTO_INCREMENT , nom varchar(50) NOT NULL , clepub varchar(50) NOT NULL );
  create table messages (id  integer PRIMARY KEY AUTO_INCREMENT , nom varchar(50) NOT NULL , message varchar(150) NOT NULL );
  create table asymmessages (id  integer PRIMARY KEY AUTO_INCREMENT , nom varchar(50) NOT NULL , message varchar(150) NOT NULL ,reciever varchar(50) NOT NULL );
  create table active (id  integer PRIMARY KEY AUTO_INCREMENT , nom varchar(50) NOT NULL );
  INSERT INTO `active`(`nom`) VALUES('nouser');
   ```

# PentRacker - Testing Documentation

## Project Overview
PentRacker is a desktop application in Python that provides various security functionalities. This documentation focuses on the testing aspects of the application.

## Application Features
- Double factor authentication
- Encoding / Decoding (Base 64, Base 32, Base 16)
- Hashing / Cracking (MD5, SHA1, SHA256)
- Symmetric encryption / decryption (DES, AES)
- Asymmetric encryption / decryption (EL GAMAL, RSA)
- Secure chat room (AES based)

## Testing Documentation

This project includes three levels of testing:

### 1. Unit Tests (`/UnitTests`)
Located in the `UnitTests` directory, these tests verify individual components:

- **User Authentication Tests** (`test_get_user.py`)
  - Tests the user retrieval functionality
  - Uses mocking to isolate the DAO layer
  
- **Encoding/Decoding Tests** (`test_encode.py`)
  - Tests Base64 encoding and decoding
  - Tests Base32 encoding and decoding
  - Tests Base16 encoding and decoding
  
- **Encryption Tests** (`test_des_encryption.py`)
  - Tests DES encryption functionality

### 2. Integration Tests (`/IntegrationTests`)
Located in the `IntegrationTests` directory:

- **Database Integration Tests** (`test_main.py`)
  - Tests user registration functionality
  - Tests user retrieval from database
  - Uses pytest fixtures for database connection management

### 3. End-to-End Tests (`/End2endTesting`)
Located in the `End2endTesting` directory:

- **UI Automation Tests** (`test_end2end.py`)
  - Tests the complete registration and login flow
  - Uses PyAutoGUI for UI automation
  - Simulates user interactions with the application interface

## Test Environment Setup

### Prerequisites
- MySQL server
- Python test dependencies:
  - `unittest` (for unit tests)
  - `pytest` (for integration tests)
  - `pyautogui` (for end-to-end tests)
  - `pyperclip` (for end-to-end tests)

### Database Setup
Run the following SQL commands to set up the test database:
```sql
create table users (
    id integer PRIMARY KEY AUTO_INCREMENT,
    nom varchar(50) NOT NULL,
    prenom varchar(50),
    email varchar(50) NOT NULL UNIQUE,
    numero varchar(8) NOT NULL,
    password varchar(256) NOT NULL,
    code varchar(6) NOT NULL
);

create table clepubs (
    id integer PRIMARY KEY AUTO_INCREMENT,
    nom varchar(50) NOT NULL,
    clepub varchar(50) NOT NULL
);

create table messages (
    id integer PRIMARY KEY AUTO_INCREMENT,
    nom varchar(50) NOT NULL,
    message varchar(150) NOT NULL
);

create table asymmessages (
    id integer PRIMARY KEY AUTO_INCREMENT,
    nom varchar(50) NOT NULL,
    message varchar(150) NOT NULL,
    reciever varchar(50) NOT NULL
);

create table active (
    id integer PRIMARY KEY AUTO_INCREMENT,
    nom varchar(50) NOT NULL
);

INSERT INTO `active`(`nom`) VALUES('nouser');
```

## Running Tests

### Unit Tests
```bash
# Run all unit tests
python -m unittest discover UnitTests

# Run specific test file
python -m unittest UnitTests/test_encode.py
```

### Integration Tests
```bash
# Run integration tests
pytest IntegrationTests/test_main.py
```

### End-to-End Tests
```bash
# Run end-to-end tests
# Note: Ensure the application is running and don't move the mouse during tests
python End2endTesting/test_end2end.py
```

## Important Notes

1. For End-to-End tests:
   - The application must be running before starting the tests
   - Don't move the mouse during test execution as it may interfere with UI automation
   - The application window will be moved to the top-left corner during testing

2. For Integration tests:
   - Ensure the database is properly set up and accessible
   - The tests use pytest fixtures to manage database connections

3. For Unit tests:
   - Some tests use mocking to isolate components
   - Database-related tests are mocked to avoid actual database operations
