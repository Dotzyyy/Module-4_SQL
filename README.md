# Module-4_SQL
## python-flask-app w/ postgres sql
Flask Blog 2
Render Url: https://module-4-sql.onrender.com/
Github Url: https://github.com/Dotzyyy/Module-4_SQL
Test User: username: testuser
           password: testing123 

## Concept

This app was made to act as an online blog where users can register for an account and sign into the blog. This is an expansion of my previous project
which did not allow actual logins to due to a lack of a database. Connecting the flask app to postgresql we are able to store user information such as username, email, passwords and each of their blogposts.

### Languages and Technology Used

Featured Languages:

* HTML5

* CSS3

* JavaScript

* Python3

* SQL

Featured Technologies:

* Postgresql

* pgadmin

* Bootstrap 

* Flask

* Render (For deploying the app)

### Features



* Forms are available to help register, login, edit information and make blog posts on the site.

* A navbar that shrinks into a 'hamburger' when seen on smaller screens.

* An explore page which allows users to view all posts made, not just their own or those of their followers.

* A task list is available so that the user can creat their own 'to-do' list.

* The user can see a real-time clock underneath the Navbar.




### Future Updates

I would love to add more functionality and QOL features for user in the future.

## How to run the database on render

### Step 1:

Sign in or create an account on https://render.com/

### Step 2:

On the Dashboard, create new PostgreSQL database and fill in the various details.

### Step 3:

Once created, download a database management software such as Postgresql and PgAdmin.

### Step 4: 

Create a new server node, click properties and navigate to the connection tab.
Enter the following from the render database:

* Host name/address. For example: dpg-cpisitkf7o1s73bm97o0-a.frankfurt-postgres.render.com

* Port should be automatic but look something like: 5432

* Maintenance database. For example: flask_project_db_e6in

* Username. For example: davidsexton

If entered correctly, the render database should appear in your servers.

### Step 5:

Return to render and copy the Internal and External URL to the this website's config.py folder, the internal one being placed under the 'Render' environ and the external being placed under the 'else' statement.

* note: the urls will start with 'postgres' but make sure they start with 'postgresql' instead.

### Step 6:

Use the flask shell to type db.create_all() and perform all the neccesary migrations and upgrades to the models.

### Step 7:
At this point you'll need to have created to webservice so return to this step once that is complete.

Place an environment variable in the web service's environment tab called 'DATABASE_URL' and paste the Internal URL from the render database.
Do not forget that the address should begin with 'postgres'!

*Example: 'postgresql://davidsexton:hFNESpygwyQd4DMpWiBliSWZRbmwibRY@dpg-cpisitkf7o1s73bm97o0-a/flask_project_db_e6in' NOT ''postgres://davidsexton:hFNESpygwyQd4DMpWiBliSWZRbmwibRY@dpg-cpisitkf7o1s73bm97o0-a/flask_project_db_e6in'
            


## How to Deploy/Access the main website

### Step 1:

One of three options:

* Upload the project folder to your own github.

* Clone this git repository at https://github.com/Dotzyyy/Module-4_SQL

* Access via the provided URL https://module-4-sql.onrender.com/

### Step 2:
    
   Sign in or create an account on https://render.com/

### Step 3:

    Link your github account

### Step 4:

   Once logged in and on the main dashboard, select "New" > "Web Service".

### Step 5:

    Connect to this repository or a clone of it.

### Step 6:

On the following form, ensure that:

* You select an appropriate name for the web service

* Select your closest region (Frankfurt for Europe)

* Branch should be 'main'

* Make sure not to change any of the pre-loaded flask options such as 'build command'

* Start Command '$ gunicorn run:app' (make sure 'Flask' and 'Gunicorn' are listed in requirements.txt)

* Select Instance Type 'free

### Step 7:

Use the provided Url to access the website!:
    https://module-4-sql.onrender.com/







