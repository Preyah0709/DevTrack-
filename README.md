DevTrack - Engineering Issue Tracker

Overview: 
Dev'Track is a lightweight backend API built using Django for tracking engineering issues. 
The application allows reporters to create bug reports, assign priorities, track statuses, and retrieve issue information through API endpoints.
The project demonstrates:
    Object-Oriented Programming (00P)
    Inheritance and Method Overriding
    Abstract Base Classes
    Django Views and URL Routing
    JSON File Storage
    API Endpoints
    Request Validation
    
Design approach: The Assignment required implementing OOP concept before building API.

OOP Design: All entities were places inside/models.py.
    
    BaseEntity 
        |---> Reporter
        |---> Issue
                |---> CriticalIssue
                |---> CriticalIssue
  
Why this design?:
Instead of placing validation and business logic inside views.py, I kept them inside the appropriate classes.
This separation makes the code easier to maintain and follows object-oriented design principles..
For example:
    - Reporter handles reporter validation.
    - Issue handles issue validation.
    - CriticalIssue and LowPriorityIssue override the describe() method to provide different behavior based on priority.
    - Views are responsible only for handling requests and responses.

Data Storage: 
    In two seperate JSON Files.
    Reporters.json - stores reporter Info.
    Issues.json - stores issues 

How to Run Project: [shell]
  Clone the Repository
  git Clone <https://github.com/Preyah0709/DevTrack->
  Navigate to the main folder - cd DevTrack 
  Install Django - "pip install django"
  Run the server - "python manage.py run server"
  Open API "http://127.0.0.1:8000/"  
  Note: To access issues http://127.0.0.1:8000/api/issues
        To access Reporters http://127.0.0.1:8000/api/reporters

EndPoints:
  Created Reporter - Error:
  <img width="1632" height="967" alt="req-1" src="https://github.com/user-attachments/assets/08d0d6e0-8e03-43cc-b9f1-381aa15443c8" />
  Created Reporter - Successful:
  <img width="1633" height="955" alt="req-2" src="https://github.com/user-attachments/assets/1264dba2-56e1-4adf-87f4-91ac0ae21c7a" />
  Getting all Reporters:
  <img width="1627" height="978" alt="req-3" src="https://github.com/user-attachments/assets/e68cbe35-dc96-4124-836f-d8e98b4c13bc" />

  Creating Issue - Error:
  <img width="1640" height="982" alt="issue-1" src="https://github.com/user-attachments/assets/f295146d-f4e9-449f-8bd1-db71a8bcde08" />
  Creating Issue - Successful 
  <img width="1630" height="983" alt="issue 2" src="https://github.com/user-attachments/assets/3f5bc6ab-5c0e-43b4-b5b9-73366b826e36" />

  Filtering with Status:
  <img width="1627" height="986" alt="filter-status" src="https://github.com/user-attachments/assets/7c6d508f-7cdc-4a1e-959a-f462af5f4ea7" />
  Getting Issue with ID:
  <img width="1638" height="955" alt="filter-id" src="https://github.com/user-attachments/assets/0e17afcb-b984-43b1-99c7-96839fb54521" />



  




  
  
