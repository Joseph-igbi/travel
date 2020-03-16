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
The app was 
![micro-arch]
### Front End Design














[epic]:https://i.imgur.com/lx59k72.png
[micro-arch]:https://i.imgur.com/k5OyVbv.png?1
[service-arch]:https://i.imgur.com/iV3AiEx.png
