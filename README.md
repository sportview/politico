# Politico
The general elections are around the corner,hence its a political season.Get into the mood of the season and help build a platform which both the politicians and citizens can use. Politico enables citizens give their mandate to politicians running for different government offices while building trust in the  process through transparency.

### Requirements to install
 Python
 
### Installation steps
.clone the repository from Github

from cmd run git clone https://github.com/sportview/politico/develop

.change directory to myapp

cd myapp

.create a virtual environment

 virtualenv venv

.Activate the virtual environment for windows
  
  cd venv\scripts\activate 
  
## Start the server and run the application 

python app.py

     API Endpoints


---------------------------------------------------------------------------------------
API Endpoints
---------------------------------------------------------------------------------------
              Method	Route	Functionality
---------------------------------------------------------------------------------------
POST	/api/v1/parties	 Creates new political party
---------------------------------------------------------------------------------------
GET	/api/v1/parties 	Get all political parties
---------------------------------------------------------------------------------------
GET	/api/v1/parties/<int:party_id	 Get a specific political party
---------------------------------------------------------------------------------------
DELETE	/api/v1/parties/<int:party_id	 Delete a specific political party
---------------------------------------------------------------------------------------

PATCH	/api/v1/parties/<int:party_id/name	Edit the name of a specific political party

POST	/api/v1/offices	   Create a new political office

GET	/api/v1/offices	  Get all political offices

GET	/api/v1/offices/<int:office_id	Get a specific political office

## Test The API 
Use any REST client such as Postman or Insomnia

## Author
Charles Kamau

## 
Acknowledgements

Andela Pre-bootcamp cycle team








  
  
  
