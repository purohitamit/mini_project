# mini_project
** Project Objective: **
The objective of this project is to create a web app using flask micro framework and to implement the CRUD (Create, Read, Update and Delete) functionality. The information is stored in the MySQL database which comprises to two tables with one to many relationship.  
![design](https://user-images.githubusercontent.com/87416941/157236242-2422fb12-6552-4a13-a58d-159110a81867.png)  
** Entity Relation Diagram **  
I used two tables to store data name Author and Book with id as the Primary Key in both the tables and author_id as the Foreign Key in the Book table.  
![erd](https://user-images.githubusercontent.com/87416941/157238303-01548447-e7b5-4a6e-98d5-14449e470c54.PNG)  
** Project Tracking **  
I used git for the version control and as the repository was hosted on Github,  I used it's Project feature for the project tracking. The whole project was broken down into 6 tasks so 6 issues were created. Every time the task was completed and was pushed to github repo, the issue was automatically closed which was linked to the project. Below are the pictures taken at the start and after completing all the tasks.  
![Projects](https://user-images.githubusercontent.com/87416941/157239702-ca831326-8eed-4c31-8ea5-70b3141c3cd5.PNG)  
![projectboard](https://user-images.githubusercontent.com/87416941/157240397-57d526e3-376e-468d-a567-fd86550f8295.PNG)  
The standard application structure was created for the project as per the below:  
![structure](https://user-images.githubusercontent.com/87416941/157240134-ce2e5772-a321-4d38-aa79-1f745257a8c8.PNG)  
A standard risk assessment was carried out at the start of the project as per the below:  
![risk](https://user-images.githubusercontent.com/87416941/157242441-e90dcbef-f771-432d-8c4d-9cc150684af7.PNG)  
The development environment used is a python3 virtual environment (venv) hosted on a virtual machine running Ubuntu operating system. Python is used as Flask is a python-based framework. A venv allows pip installs to be performed and the app to be run without affecting any conflicting pip installs on the same machine.
Jenkins was used as a build server, providing automation of building and testing. This automation is achieved by setting up a freestyle project which executes the test.sh script when it recieves a webhook from github upon pushing a commit. Below are the images of the live app running on the VM.  
![img1](https://user-images.githubusercontent.com/87416941/157241029-0ea90bfe-c008-42b3-8f6f-3eec61d37831.PNG)  
![img2](https://user-images.githubusercontent.com/87416941/157241054-40a0b88f-6d2c-4683-8d72-4488bcea6801.PNG)  
![img3](https://user-images.githubusercontent.com/87416941/157241093-ed130f59-04cb-4ddc-9fef-ac550f594e44.PNG)  
![img4](https://user-images.githubusercontent.com/87416941/157241143-3755356d-3892-4cc0-b16f-26f840c6727f.PNG)  
Test cases were run both in Visual studio code and by Jenkins automated free style job via a webhook and achieved a 100% coverage with a 100% pass.
![img4](https://user-images.githubusercontent.com/87416941/157241997-9758e88a-cd66-404d-b16d-54496e0a7e0c.PNG)  
![img5](https://user-images.githubusercontent.com/87416941/157242032-7d241cf0-8e39-4ea3-9abe-849b9f41dc91.PNG)  
![img6](https://user-images.githubusercontent.com/87416941/157242090-266e6963-4c8b-4af6-a678-596e61281fd5.PNG)  
As a stretch goal for the project, I also used Jenkins to depoly the app on another server.  
![another_server](https://user-images.githubusercontent.com/87416941/157431544-63f66ed4-789e-48f0-a6cd-80010ea53e1d.PNG)
![Jenkins_server](https://user-images.githubusercontent.com/87416941/157431642-77065f4c-9755-4399-b21d-b56db2655e77.PNG)








     












