# Holiday destination generator Web-App

### Application Setup 
Three Virtual machines were instantiated for this application. They were used for the Manager-swarm, the worker-swarm and jenkins. 

### Project Overview
| Agile Methodology |
| Risk Assessment | 
| Trello Board |
| User Stories | 
| Product Backlog |
| Sprint Backlog  |
| Processes |
| Use Case Scenarios |
| CI Pipeline |
| Ansible |
| Demonstration |
| Further Improvements |

### Introduction

The project aims to create a holiday destination generator app built on the google places API that allocates holiday destinations to users based on predetermined rules and users input name. The project utilises a microservices architecture, a CI/CD pipeline and replicas for rolling updates. 

### Project
First a risk assesment was conducted allowing potential risks to be assessed and addressed. Next the initiative and epics were developed and from these the user stories. The user stories were used to create the prodoct backlog using a trello board which was further broken down into sprint backlog items. Sprint backlog items were moved from to-do to completed in the trello board as the project progressed.

#### Epic detailing use case of holiday web-app
![epic]

#### Trello board


### Development process
The source code was connected to GitHub, which allowed version control and the ability to switch between different versions by configuring the webhook to different branches. It also allowed the project to be pulled onto different machines. Ansible was used to configure the machines.

A SQL database in GCP was spun up allowing Account information and Holiday location information to be stored whilst connectivity between the different microservices and the google's api was initiated using the requests library and flask-request. 

A webhook was triggered whenever code was deployed to the selected branch on github, triggering the automated Jenkins build and deploy. 
As part of the automated deployment, the jenkins vm would ssh onto the manager swarm and deploy the webapp which is run through nginx as a reverse proxy.

### Service Orientated Architecture
![service-arch]

### App Microservice architecture
The app microservice structure was as shown below with the arrows representing HTTP requests between the services.
![micro-arch]
1. User provides name which is sent from Main Service (Service 1) to Service 4. 
2. There are 100 countries in the database. If the length of the name % 5=0 then Service 2 generates 18 random numbers between 0 and 19 then 2 random numbers between 20-40,...80-100 totalling a list of 26 random numbers. if the length of the name%5= 1 then the 18 random numbers are generated between 20-40 and so on. Therefore the length of name gives a 70% chance of the country chosen being from a particular area. This list is returned to Service 4.
3. Service 3 gets the name from Service 4 and chooses a random letter from the name. The numerical equivalent of the letter (a=1,b=2..) is returned to Service 4.
4. In Service 4 the two random objects generated are combined. The random number from Service 3 is used as an Index for the list of numbers from Service 2. A number from the list is returned.
5. This number is used as an Index for the countries in the database. This is returned from the database to service 4. 
6. The country is returned to Service 1 which again using HTTP requests communicates with the google places API to return tourist locations for that country which is displayed to the user.

### Front End Design
![signin]
![name]
![result]
![view]
![stored]













[epic]:https://i.imgur.com/lx59k72.png
[micro-arch]:https://i.imgur.com/1Ho1bsO.png?1
[service-arch]:https://i.imgur.com/iV3AiEx.png
[signin]:https://i.imgur.com/A6IlVwD.jpg?1
[name]:https://i.imgur.com/ahA3yUZ.jpg
[result]:https://i.imgur.com/3xs4jfr.jpg
[view]:https://i.imgur.com/JRCM2tD.jpg
[stored]:https://i.imgur.com/1jpsnBe.jpg
