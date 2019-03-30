# RFI CDT–ADPQ–0117 Response

[USDS Playbook 1-5](https://github.com/ibmbluemixgarage/caliconnects/wiki/USDS-Playbook-Usage-%28Play-1-to-5%29)
 
[USDS Playbook 6-10](https://github.com/ibmbluemixgarage/caliconnects/wiki/USDS-Playbook-Usage-%28Play-6-to-10%29)
 
[USDS Playbook 11-13](https://github.com/ibmbluemixgarage/caliconnects/wiki/USDS-Playbook-Usage-%28Play-11-to-13%29)
 
[USDS Technical References](https://github.com/ibmbluemixgarage/caliconnects/wiki/Technical-References)

##Tweets & Blog
> Product Owner, Marquis Cabrera - Tweets at #ADPQrefresh & Blogs at (in progress).

##Prototype Process
> [Start Here](https://github.com/ibmbluemixgarage/caliconnects/wiki)

##Prototype 
> Placeholder for final prototype link

![alt tag](./documentation/general-images/Cover1.png)

## Technical Approach

- Access [the prototype](https://caliconnects.mybluemix.net/) for resident user (create a new account) 
- Access prototype for [admin user](https://caliconnects.mybluemix.net/users/sign_in#1) (email: "alan@example.com" password: "password")
- Install locally (see [technical_setup.md](https://github.com/ibmbluemixgarage/caliconnects/blob/master/technical_setup.md))
- See [our journey](https://github.com/ibmbluemixgarage/shiny-fawn/wiki) and how we met the [requirements](https://github.com/ibmbluemixgarage/shiny-fawn/wiki/USDS-Playbook-Usage) (see our Twitter Hashtag: #ADPQRefresh)

At the IBM Bluemix Garage, we believe in innovating with speed and incrementally delivering impressive solutions. To build a working prototype in three weeks, we enabled our autonomous, multidisciplinary team of experienced business, technology, and process innovation experts and product owner to learn, build, and iterate, using the labor categories in the RFI:

- Marquis - Product Manager / Owner
- Andrew - Agile Coach
- HT - Delivery Manager
- Mary-Sara - Business Analyst
- Kirk - Technical Architect
- Adam - Interaction Designer
- Pier - Writer
- Rebekah and Lisa - Visual Designers
- Alex - Front-end Web Developer
- Savannah - DevOps Engineer
- Andrew - QA
- Erin - Digital Performance Analyst

Overall: The resident-user logs in, some Jquery Javascript code will run, data is retrieved from the Rails server, which it gets from Postgres. A good example of this is the admin section, which has Javascript enabled pages in the hazard .js files, calls the admin campaigns and admin alerts rails controllers, which in turn use the active record library to reference the campaigns and alerts tables. Here’s the links to show code flow from client UI, to JavaScript library, to REST service to database, pointing to code in the GitHub repository: 

- client-side html files: app/views 
- js: ./app/assets/javascripts/ 
- rails code: ./app/controllers 
- connection to the database: ./app/models


## THINK: Planning, Discovery, and Concept
When the RFI dropped, our team co-located in San Francisco at our Bluemix Garage to discuss the RFI requirements and determine which challenge we should select. Although we thoroughly researched Prototype 1 and found Open Data to use online, we chose Prototype 2 based on the resident focus and appeal of building a solution for California residents.  

Our team started with a workshop using design thinking methods of ideation, storyboarding, and to-be scenario mapping to understand the problem space.  We  developed a taxonomy of emergency (https://github.com/ibmbluemixgarage/caliconnects/blob/master/documentation/IBM%20Design%20Thinking%20Workshop/DesignThinking_Ideation_Alerts_Emergency.JPG) and non-emergency alert types (https://github.com/ibmbluemixgarage/caliconnects/blob/master/documentation/ IBM Design Thinking Workshop/DesignThinking_Ideation_Alerts_NonEmergency.JPG) that we, as California residents, would want to receive. Then we developed personae and empathy maps (https://github.com/ibmbluemixgarage/caliconnects/blob/master/documentation/IBM%20Design%20Thinking%20Workshop/DesignThinking_EmpathyMap_Brenda.JPG) for the admin and resident user to understand the pain points and, ultimately, test and validate them through research.  Our personae were Alan, the Admin user, and Brenda, the California resident.  We created to-be scenarios to understand and envision the user experiences of our personae (admin:  https://github.com/ibmbluemixgarage/caliconnects/blob/master/documentation/IBM%20Design%20Thinking%20Workshop/DesignThinking_DesignThinking_Alan_Admin_Personna.jpg), resident: https://github.com/ibmbluemixgarage/caliconnects/blob/master/documentation/IBM%20Design%20Thinking%20Workshop/DesignThinking_DesignThinking_Brenda_CA_Personna.jpg) as they interact with the solution. Then we consolidated the individual persona mapping into a single group scenario maP (https://github.com/ibmbluemixgarage/caliconnects/blob/master/documentation/playbook-images/W1n-storyboard.jpg)
.  Finally, we developed the Vision and MVP Statements. 

Each team member designed low-fidelity wireframe sketches (https://github.com/ibmbluemixgarage/caliconnects/blob/master/documentation/playbook-images/W3h-Playback3.jpg)
to explore solutions; then we iterated on a Vision Statement (https://github.com/ibmbluemixgarage/caliconnects/blob/master/documentation/IBM%20Design%20Thinking%20Workshop/DesignThinking_Vision_Statement_Brenda.JPG
) that led us to a value stream map to evaluate user assumptions, risks, and value (https://github.com/ibmbluemixgarage/caliconnects/blob/master/documentation/playbook-images/W1p-assumptions-a.jpg).  We kicked off our inception, which included developing a hypothesis statement (https://github.com/ibmbluemixgarage/caliconnects/blob/master/documentation/IBM%20Design%20Thinking%20Workshop/DesignThinking_Hypothesis.JPG), discussing goals, and future goals (https://github.com/ibmbluemixgarage/caliconnects/blob/master/documentation/IBM%20Design%20Thinking%20Workshop/DesignThinking_Goals_FutureGoals.JPG), and developing Backlog Epics of our initial user stories told from the perspective of the customer. Our inception ended with a retrospective to evaluate processes and identify bottlenecks, and improvement opportunities.

The product owner sent out materials on disaster preparedness to the larger team, via Slack, to familiarize the team with the process. The product owner also took a course on FEMA’s Integrated Public Alert and Warning System (IPAWS) to learn more about the admin user and how he might sends notifications and explored the tools the state currently uses to send alerts, such as: Everbridge/Nixle and MyHazards.  At the same time, we  explored opportunities to engage with actual admin users and scheduled an interview with a California County Administrator. 

## CODE: Design, Build, Deploy

Design:     Our designers reviewed the following libraries and our developers integrated them into our code base: https://github.com/18F/web-design-standards and https://github.com/thoughtbot/bourbon Our designers also researched and review U.S. web standards. In compliance with Section 508 of the Americans with Disabilities Act and WCAG 2.0, we used the guidelines from this checklist, http://webaim.org/standards/508/checklist, as well as the IBM Web Accessibility Checklist (http://www-03.ibm.com/able/guidelines/web/ibm508wcag.html ). 
 
Our designers recommended the inclusion of a Conversational UI to provide a warmer more person-centered experience for the user and convey a fun, hip feel.  To develop the front-end UI, we used Rails ERB, Jquery, and Sass.

Development: Our IBM Garage uses a continuous delivery and extreme programming approach to reduce errors, including re-factoring in real time, to take ideas from concept to reality with speed. Using this approach, our developers embraced a mindset of continuous experimentation and were ready to pivot to meet the user needs captured in our stories. In addition, we used extreme programming to deliver tiny bits of code, working each week to iterate and build faster, instead of a Scrum Method, which maintains a consistent delivery cycle.  

To build Prototype B, we first had to work on some tasks, such as setting up the Bluemix pipeline service, which is built on Jenkins, an open source technology, to use for staging and master environments; Bourbon and Neat, which provide a responsive grid framework for both desktop and mobile; GitHub, New Relic, and Docker for the development environment and the Cloud Foundry container for production.

Our full stack included the following open source technologies, each of which has had a major releases within the last five years: Ruby, Rails, Postgres, Rspec, Devise, Capybara, Docker, Bourbon and Neat, Jquery, Bundler, Dotenv, Swagger UI, and Cloud Foundry. 

DevOps: We developed the prototype on Bluemix and Cloud Foundry, which is a PaaS.  In our DevOps continuous delivery environment, no code is delivered without automated tests. We developed and implemented automated unit tests, including automated security tests, for code using the Rspec/Capybara libraries. The test framework was already set up and integrated with the CI pipeline, with an example spec located in the spec directory. We set up Capybara to provide security testing related to user authorization and authentication, and the Application Security on Cloud Bluemix service will allow us to run scans for major security vulnerabilities. 
We used the following configuration management tools to manage our application environment: the Dotenv Ruby Gem, Cloud Foundry’s VCAP services, and Ruby’s Gemfile. We also used the continuous (real-time and historical) monitoring tools: the New Relic, ELK stack logging, and Bluemix Availability Monitoring and Active Deploy and Autoscale services to manage the roll out of the application changes in an automated and controlled fashion to ensure an uptime of 99.999% availability and high user-satisfaction.  

Geolocation: We used Google API for active geolocation and for our resident user, Brenda, to input an address.  When the resident user clicks share location, it narrows it down, but she must still start inputting the address before autocomplete is initiated. 

Configured Mobile and Email Messages: For our admin user, Alan, to send notifications to the resident user (Brenda), we configured SendGrid, a Bluemix platform item, to send emails, and Twilio to deliver SMS. 

Swagger API: We are using one library (https://github.com/fotinakis/swagger-blocks) for the swagger documentation, which will generate the documentation for us, and we are using another (https://github.com/d4be4st/swagger-ui_rails) to give us a URL to present that documentation.  Here is the API endpoint documentation for alerts https://caliconnects.mybluemix.net/apidocs .

## Building Process  
We prioritized the backlogs to deliver a minimum viable product and meet the RFI requirements for Prototype B.  Upon building, we had to spike out the data sources required by the RFI to learn how to incorporate them. 

The development process started with a spike story to assess the data sources provided by the State. Ultimately, we learned that the data sources provided were not true APIs, with the exception of the earthquakes data, meaning they only yielded map legends and images.  Our product owner called Esri, owner of the APIs, who confirmed their APIs yield only maps and drill down tools, so users have to bring in their own data.  So we pulled XML feeds from NOAA and USGS. 

In Week 1 of development, we released incremental functionality as we sought an admin user to interview. We coded select alert types, input a notification, visualized map data, and performed a data dump of all of the XML and other data (including calling API) sources.

Week 1 - Learnings: We talked with an admin user from Ventura County (https://github.com/ibmbluemixgarage/caliconnects/blob/master/documentation/Prototype%20Testing/Usability_Testing_Brenda_Notes.JPG) while the design team developed the wireframes for the resident user to support the two user types required for the prototype. We revised the alert types and notification types based on our interview.  For example, the Ventura County Emergency Alert System Program Manager told us they use Advisory, Voluntary Evacuation, and Emergency Evacuation.  In addition, campaign notifications are named based on the street where the event is occurring.  We also learned the pain points from an admin perspective, which include limited characters for notifications, inclusion of landlines, and the public does not know the source of the alerts. We focused on the resident user initially since we had more data points for the resident persona.  

In Week 2 of development, we had a working resident user prototype. We integrated Twilio, and the admin-user was able to send SMS notifications that the resident user would receive, while the design team worked on the admin wireframes. 

Learnings: 
We talked again with the Program Manager from Ventura County to learn more about the alert types, analytics, and public education.  Based on our discussion, we scoped and included some basic analytics functions, specifically around penetration rate.  We also added a link to provide users access to additional details, and allow the admin to track and confirm if alerts are read. 
We tested our wireframes with residents (https://github.com/ibmbluemixgarage/caliconnects/blob/master/documentation/Prototype%20Testing/Usability_Testing_Brenda_Notes.JPG) and admin users from Ventura County (https://github.com/ibmbluemixgarage/caliconnects/blob/master/documentation/Prototype%20Testing/Usability_Testing_Brenda_Notes.JPG) while the development team built the log-in pages. Our resident users told us to provide some education around alert types.  And, our admin user gave us great insights around the functionality of selecting alert type tabs and to changing ‘Archive’ Campaign to ‘End’ Campaign for greater clarity. 

In Week 3 of development, we produced log-ins, managed the profile, styled the view for both admin and resident users, integrated Swagger, and developed email notifications and XML data feeds and visualization functionality.

Learnings: We tested the working prototype with resident users working at a retail store in San Francisco. While we weren’t able to make changes due to a short timeline, we included their input as future recommendations ( https://github.com/ibmbluemixgarage/caliconnects/blob/master/documentation/Prototype%20Testing/UserTest_WorkingPrototype-MLC-Notes.pdf)



Tools: 
- Trello: We used Trello to manage sprints and backlogs, feature requests, and tasks. 
- Github Issues: Used to report security and system issues. 
- Slack: A collaboration tool used to capture daily team communication. 


## DELIVER: Test, Re-Test, Test Again
Our strong focus on the user is the key ingredient to building a beautifully designed digital product that meets user needs.  To gain user insights early in the process, we tested our Invision user experience prototypes and wireframes (see Design Artifacts) with users in the Galvanize working space and with a Program Manager responsible for the Ventura County Emergency Response System.  Additionally, we sent out a survey to California IBMers, essentially “sponsor users,” who could share their experiences to learn more about resident users. Ultimately, we drove findings to the backlog and made changes to our prototype based on the user’s needs.  For example, for the resident user, we tried to account for copywriting and educating them on the types of alerts they would receive, and for the admin user, we changed how he would select alert colors. Ultimately, we used iterative design to evolve our working prototype in real time based on a series of ever-improving designs (https://github.com/ibmbluemixgarage/caliconnects/blob/master/documentation/playbook-images/W2f-StreetInterview.jpg).  With more time, we would be able to evolve our working prototype to provide greater functionality to delight the user.

