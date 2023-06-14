A national car dealership with local branches spread across the United States recently conducted a market survey. One of the suggestions that emerged from the survey was that customers would find it beneficial if they could access a central database of dealership reviews across the country.

You are a new hire at the company. You are assigned the task of building a website that allows new and existing customers to look up different branches by state and look at customer reviews of the various branches. Customers should be able to create an account and add their review for any of the branches. The management hopes this will bring transparency to the system and also increase the trust customers have in the dealership.

After thorough research and brainstorming, the team developed use cases for anonymous, authorized, and admin users.

Use cases for anonymous users:

View the "Contact Us" page.

View the "About Us" page.

View the list of dealerships.

Filter the list of dealerships by state.

Click on a dealership to view the reviews for that dealership on the details page.

Log in using their credentials.

Use cases for authorized users: In addition to the above, authorized users should be able to write a review for any dealership on the dealership's page. In order to enable authorized users to write their reviews:

A Review button should be provided against each dealer listed in the dealership table.

Clicking on the Review button should take the user to the review page.

Filling the form on the review page and submitting it should add the review. 

```{ "user_id": 1, 

"name": "Berkly Shepley", => from Django "dealership": 15, => from the form "review": "Total grid-enabled service-desk", => form textbox "time": "", => current time "purchase": true, => form checkbox "purchase_date": "07/11/2020", => form calendar (bootstrap) "car_make": "Audi", => from django dropdown "car_model": "A6", => from django dropdown "car_year": 2010 => form django dropdown } 

```

On submission, user should be taken back to the dealership detail page with the submitted review featured at the top of the reviews list, sorted on time.

Use cases for admin users:

Log in to the admin site with a predefined username and password.

Add new make, model, and other attributes.

Your organization has assigned you as the Lead Cloud Application Developer on this project. Your job is to develop this portal as part of your Capstone project by following best practices for cloud application development.

# Final Project Template

The final project for this course has several steps that you must complete. 
To give you an overview of the whole project, all the high-level steps are listed below. 
The project is then divided into several smaller labs that give the detailed instructions for each step. 
You must complete all the labs to successfully complete the project.

## Project Breakdown

**Prework: Sign up for IBM Cloud account and create a Watson Natural language Understanding service**
1. Create an IBM cloud account if you don't have one already.
2. Create an instance of the Natural Language Understanding (NLU) service.

**Fork the project Github repository with a project then build and deploy the template project**
1. Fork the repository in your account
2. Clone the repository in the theia lab environment
3. Create static pages to finish the user stories
4. Deploy the application on IBM Cloud

**Add user management to the application**
1. Implement user management using the Django user authentication system.
2. Set up continuous integration and delivery

**Implement backend services**
1. Create cloud functions to manage dealers and reviews
2. Create Django models and views to manage car model and car make
3. Create Django proxy services and views to integrate dealers, reviews, and cars together
 
**Add dynamic pages with Django templates**
1. Create a page that shows all the dealers
2. Create a page that show reviews for a selected dealer
3. Create a page that let's the end user add a review for a selected dealer

**Containerize your application**
1. Add deployment artifacts to your application
2. Deploy your application

**Deployed Url**
http://3.91.35.26:8000/djangoapp/
The application was deployed in amazon ec2 instance.
Steps followed to run a docker container in EC2 instance:
-- Log in to aws console and create a EC2 instance with default vpc.
-- Connect to the instance using EC2 instance Connect.
-- Execute the following commands:

sudo yum update -y
sudo yum install docker -y
sudo usermod -aG docker ec2-user
sudo service docker start
sudo chkconfig docker on
sudo yum install git -y
git clone https://github.com/srividya-sundaravadivelu/agfzb-CloudAppDevelopment_Capstone.git
cd agfzb-CloudAppDevelopment_Capstone/server
sudo service docker restart
------- exit and log back

docker build -t my-app .
docker run -d -p 8000:8000  my-app:latest
---- Also make sure to add the public IP address of the EC2 instance to the ALLOWED_HOSTS list in your Django application settings.py file.


