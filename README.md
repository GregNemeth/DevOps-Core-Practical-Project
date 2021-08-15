# DevOps-Core-Practical-Project

## **Contents**

 * [Introduction](#introduction)
   * [Objective](#objective)
   * [Proposal](#proposal)
*  [Architectue](#architecture)
   * [Jira board](#project-tracking)
   * [Risk assessment](#risk-assessment)
   * [Test Analysis](#test-analysis)
*  [Infrastructure](#infrastructure)
   * [Jenkins](#jenkins)
   * [Entity diagrams](#entity-diagram)
   * [Docker Swarm](#docker-swarm)
   * [The services](#services)
*  [Development](#development)
   * [Unit testing](#unit-testing)
   * [Frontend Desing](#front-end)
*  [Footer](#footer)

## **Introduction**

### **Objective**

The objective of this project is to create an application that is composed of at least 4 services: 
* service-1: should host the frontend
* service-2 & service-3 both generate a random object
* service-4 : receives the objects generated by 2 & 3 , perform a logic and returns an object to service-1, to be displayed on the home-page.

There are certain tools to be implemented in order to demonstrate what we leart in the past weeks:
* Project tracking with kanban or scrum board
* Version control: git
* CI server: jenkins
* Configuration management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration tool: Docker Swarm
* Reverse proxy: NGINX

### **Propsal**

For my project I decided to create a simple magic 8 ball app, as the focus is not the application itself but the pipeline.
* Service-1: Front-end
* Service-2: Generate random number within 1 and 4
* Service-3: Generate a random number within 1 and 3
* Service-4: multiplies numbers and uses result as ID to fetch the answer

## **Architecture**

### **Jira board**

For project tracking, I chose to go with a Scrum board in Jira. This tool was used for user stories, tracking tasks from in-progress to done. I also used it to record some difficulties to be worked out. You can see the board below.

![Jira_board](https://github.com/GregNemeth/DevOps-Core-Practical-Project/blob/main/images/Jiraboard.png)

### **Risk Assessment**

My risk assessment can be seen below. I started of with a base and tried to expand as further issues were encountered or came to mind. Risk assessment is an important part of every project as countermeasures and reactions to certain situations can be documented in advance, which can result in decreased down-time, in case difficulties arise.

![Risk_assessment](https://github.com/GregNemeth/DevOps-Core-Practical-Project/blob/main/images/risk-assessment.png)

### **Test analysis**

As this project is about creating a CI/CD pipeline , and cultivating a devops mentality, testing was one of the main pillars of this process. Since code is continuously pushed to the VCS it is vital that testing is present as early in the process as possible. Considering the scope of the project, I have decided to follow the concept of MVP which inculed automated testing of the functions through unit testing , and left integration testing as a manual process.(In the future more complex testing can be implemented, which could include security and systems testing as well) I understand this was only viable, because I was the only person working on the project. To achieve a Test-Driven-Development, I started off by creating a sheet, following the concept of the project outlining what each function should do, writing the test first and making sure it runs before any push occured.You can observe the sheet below:

![Test_sheet](https://github.com/GregNemeth/DevOps-Core-Practical-Project/blob/main/images/Testing%20Reqs.png)

## **Infrastructure**

To achieve a short time between development and deployment, Continuous Deployment methods have been implemented in this project.

### **Jenkins**

The VCS (git & github) have been set to send a webhook to the Jenkis server, whenever new content is pushed to the development branch. It instructs the build server to do the following things:

* **The first step is testing.** As outlined earlier this step is going to run the unit tests. I set up the jenkins server with the Cobertura coverage plugin, that gives an easy to digest report of the testing results.
* **The second step** makes sure that docker and ansible is installed on the server to allow for the following tasks.
* **In the third stage** we take advantage of Jenkins' ability to store sensitive information safely to be able to build the images , log in to our dockerhub account and push the images there.
* **The following job** runs Ansible, to configure the deployment VMs. It check whether NGINX is present on the external load-balancer and using the templates makes sure , that NGINX is running with the correct configuration. It then continues to install docker & docker-compose on the other vm's, initiate a swarm , and join in the workers.
* **The last step** uses rsync and ssh to copy the docker-compose file on the deployment vm, and runs a docker stack deploy command.

The jenkins file is stored on the VCS and can be seen [here].

![Pipeline_Diagram](https://github.com/GregNemeth/DevOps-Core-Practical-Project/blob/main/images/pipeline.png)

### **Entity Diagram**
This project utilizes two tables. It is important that during the planning project that the tables and their attributes are clearly defined , so later on valdiations and tests can be written accordingly. Even though an abstracted one-to-many relationship can be drawn between these tables, in reality they are unrelated, and for the proper working of the application it is not needed to implement unnecessary code to join these tables.

![entity_diagram](https://github.com/GregNemeth/DevOps-Core-Practical-Project/blob/main/images/ed_diagram.png)

### **Interactions**

The infrastructure of the environment after deployment can be observed below. This shows what resource are used when a user connects.

![Inf_diagram](https://github.com/GregNemeth/DevOps-Core-Practical-Project/blob/main/images/infrastructure.png)


### **The services**

As i mentioned earlier, I created an app, where services 2 & 3 provide a random number within a range through a GET request. Service-1 sends those numbers to service-4 via a POST request. Service-4 multiplies the numbers and uses the result to fetch the prophecy of the magic 8 ball from one of the 2 tables found within a container running MySQL. The response json object contains a list of the last 5 prophecies, the current prediction as well as the result of the multiplication. The second table is responsible for storing the previous results. See the service diagram below.

![service_diagram](https://github.com/GregNemeth/DevOps-Core-Practical-Project/blob/main/images/services.png)

### **Refactoring**


## **Development**

### **Unit Testing**
Unit testing was implemented throughout the project. The tool used for this was pytest, flask-test, and mock requests. These tests were designed to check every line at least once, in some cases (because of use of random numbers) 20 times. Jenkins runs these tests after every push to the code-repository, with the current setup stopping the following steps in the pipeline if the test fails. As mentioned earlier I used Cobertura to generate the reports on these tests, and if need be, further plug-ins can be used to send reports of the result via email, or RSS feed.
Test results and coverage report can be seen below. The lines ran by jenkins are as follows:
```bash
#!/bin/bash

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

python3 -m pytest --cov=. --cov-report xml -v
```
![Coverage](https://github.com/GregNemeth/DevOps-Core-Practical-Project/blob/main/images/test_reports.png)

### **Front-end Desing**
When navigating to the address of the load-balancer on the default HTTP port (80) the previously described processes take place, and present us with the following information. Html templating and Jinja-2 was used to visualize the information

![home_page]()


## **Footer**

### **Future improvements**

### **Acknowledgements**
Ryan Wright

Oliver Nichols

### **Author**
Gergely Nemeth