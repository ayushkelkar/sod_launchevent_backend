# Backend for SOD Club
This is the readme for the whole backend system.
NOTE: "[WIP]" means "Work in Progress"
## Files/Modules and their Functions
### `admin_conn.py` [WIP]:
- This handles authentication for admin access
- This isn't for regular use

### `backup.py` [WIP]:
- This handles periodic database backups of all the databases on the deployed server
- May or may not go through `flask_main`, but its up to future decision

### `config.py`:
- This is the main configuration file for the server.
It handles the following:
1. PostgreSQL Credentials (Port, Name, etc.)
2. Flask settings
3. Secret Key(s)
4. `bcrypt` Cost Factor

### `db_mgmt.py`:
- This is the connection between the main backend server and the database server.
- No other module is allowed access to the database server and needs to go through this module for I/O.

### `flask_main.py`:
- This is the main module in the server
- It handles handshakes between frontend and the backend server, and co-ordinates every task on the server
- Master I/O go through this module. Slave I/O may or may not.

### `pass_encryption.py`:
- This handles encryption of the user passwords using the python `bcrypt` module
- It hashes the password and hands it over to `db_mgmt` which takes it further
- Current cost factor decided is 12. It offers a good balance between security and performance.
- Note: Actual text of the password isn't stored in the database. Only the hash will be.

### `requirements.txt`:
- This is a text file which contains any required dependencies before running the deployment to ensure all the dependencies are met
- Format: `package_name==version`

### `utils.py`:
- This contains helper functions which are usable across any module
- May also contain repetitive functions used across different modules

## Instructions
### Dependencies
- The required modules are listed in `requirements.txt`
- Install the required modules using pip and the file using:
```bash
pip install -r requirements.txt
```
