## SENG2011 Project Vampire

### DafnyDuk Blood Management System

#### Data
- `data/deposits.json` - stores information for all blood deposits the system is responsible for
- `data/donors.json` - stores information for all blood donors the system is responsible for
- `data/requests.json` - stores information for all blood requests the system is responsible for

#### Modules
- `run.py` - initialises a blood deposit system using information contained in `data/*.json` files
- `model/system.py` - defines a `System` class i.e. top-level attributes and behaviours for the blood management system
- `model/deposits.py` - defines `Deposit` class i.e. a blood deposit
- `model/requests.py` - defines `Request` class i.e. a blood request
- `model/user.py` - defines `User` abstract class
- `model/donor.py` - defines `Donor` class (type of User)
- `model/hospital.py` - defines `Hospital` class (type of User)
- `model/administrator.py` - defines `Administrator` class (type of User)


#### Usage
- run `python run.py` from the root directory to initialise the blood management system i.e. load all the blood deposits from `data/deposits.json` into the `blood_bank` list and wait for user to enter a command

