# Book Reading Lists
The project is aimed for users that like to read books and make reading lists of books that they wish to read or have read or any other custom reading list.  
The website is build using Flask backend frameworks and Bootstrap front end with a relational database for storing the data and python for processing data.
[Hosted on Heroku](https://book-reading-lists.herokuapp.com/index)
## UX
 The user that is visiting the page can browse the list of all books that are stored in the database. In order to create or add any new data, the user must be registered. This allows users to create individual reading lists and add new books to a database that are not there yet.
#### User Stories
* As a user can, I can browse all the books on the website so I can see all of them without registering an account.
* As a user, I can sort books by an author so I can see all the books form this author.
* As a user, I can sort books by a category so I can see all the books form this category.
* As a user, I can sort books by a publisher so I can see all the books form this publisher.
* As a user, I can register an account so I have full access to the website.
* As a registered user, I can create reading lists so I can add books I want to the list.
* As a registered user, I can add new books to a system so I can populate the website with books that I like.
* As a registered user, I can edit the book in the website so that the information is correct about it.
* As a registered user, I can remove books from my reading lists so I can update my list of book.
* As a registered user, I can delete my reading lits so I can keep my reading lists up to date.
* As a registered user, I can delete books from the website.
* As a registered user, I can edit author, publisher and category names so that information is accurate. 
* As a registered user, I can delete the not needed author, category and publisher from the system. 
* As a registered user, I can edit my username and name so I can keep it up to date.

1. [Database diagram](https://drive.google.com/open?id=1j0UP4XqsVJo1R9Kl4x5HZoPStTtNp1Dv)
1. Wireframes
    * [Home page](https://drive.google.com/open?id=1YhuBULbfWzTDGhsomG4-VlxaHWRhDB6q) 
    * [Add New Book](https://drive.google.com/open?id=1FPFYq6xU7FQ1nRRBzU2sVq_DN8K7ti8X)
    * [Single Book](https://drive.google.com/open?id=19ff_65vNKQX-IGkrEqFQ5aqwZRcHTD3C)
    * [Mobile Screen Home Page](https://drive.google.com/open?id=17XR_ASwvoWiTM0_TUkjZ3ZCrZvkqcK9e)

## Features
Unregister users can browse list off book in the database. 
Register users can add/edit/delete: books, authors, publishers, category, reading lists and they own account. Books in reading lists can be added or deleted, but not edited.
### Existing Features
- Add/Edit/Delete.
    - User can add new book only if logged in the system or creating a new user account. 
    - Editing a book can be done only by logging into the account or creating a new user account. 
    - The book can be deleted from the database. If this book was in any of the reading lists it will be deleted from it as well.
- Add/Edit/Delete author, category or publisher.
 	- The components mentioned above of the book can be deleted, by deleting one of them will delete all related books of a particular author, publisher or category. 
	- The new component can be added in new book form, if the one of the above mentioned is not in the system it can be added by adding a new button in the form.
	- The edit button in menu allowed to edit one of the components from the list if needed.
- Create a new user account and be able to edit it and delete.
- Add/Edit/Delete reading lists
	-	Reading lists can be added under my Reading Lists button in menu.
	-	Reading list name can be edited by clicking the pencil icon in reading lists page next to the list name.
	- Delete list will delete all books in the list, but not in the database. 
	- Add or remove books from the reading list, will update the reading list page.
- Sorting books
 	- The books can be sorted by author, category or publisher. Each of these components mentioned is a link in the book view, by clicking it will bring it to a new page that will show all books from the selected author, category, publisher. 
### Features Left to Implement
- Share the reading lists with other website users or in social networks (Facebook, Twitter, etc.)
- Add to Reading lists button in all book view, the user doesn't need to open a single book in order to add it to the reading list.
- Display all reading lists from currently logged in user under My Reading List dropdown menu (dynamic dropdown list menu).
## Technologies Used
- **HTML**, **CSS**
  - Base languages used to create a website
- [Bootstrap](https://getbootstrap.com/)
  - The **Boostrap** was used to give the website a simple, responsive layout.
- [Flask](http://flask.pocoo.org/)
   - The **Flask** was used to as backend micro-framework to handle database requests from user inputs.
- [SQLAlchemy](https://www.sqlalchemy.org)
  - The **SQL Alchemy** was used to map the database tables to have the full power of SQL with the help of Python.
- [WTForms](https://wtforms.readthedocs.io/)
  - Using **WTForms** to validate and render forms in the website.
- [Jinja2](jinja.pocoo.org/)
  - Use **Jinja2** to render python code in HTML pages.
- [Python](https://www.python.org/)
  - Using **Python3** for backend development to interact with the database.
- [SQLite](https://www.sqlite.org/index.html)
  - The **SQLite** was used as main database engine as it is small and fast.
  
## Testing
- All code used on the site has been tested to ensure everything is working as expected
- The website was tested on different size screens to ensure all page components are changing its positions as intended. 
- Site viewed and tested in the following browsers:
  - Google Chrome
  - Mozilla Firefox
1. Register form:
    1. Click the "Register" button in the navigation menu
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with a one letter user name and verify that a relevant error message appears
     4. Try to submit the form with a two-letter password and verify that a relevant error message appears
    5. Try to submit the form with all inputs valid and verify that a success message appears.
1. Login form:
    1. Click the "Login" button in the navigation menu
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with a one letter user name and verify that a relevant error message appears
     4. Try to submit the form with an incorrect password and verify that a relevant error message appears
    5. Try to submit the form with all inputs valid and verify that a success message appears.
1. Reading Lists form:
    1. Click the "My Reading Lists" button in the navigation menu
    1. Click the "+" button in the right-hand top corner on the page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an existing list name and verify that a relevant error message appears
    5. Try to submit the form with all inputs valid and verify that a success message appears.
1. Edit reading list form:
    1. Click the "My Reading Lists" button in the navigation menu
    1. Click the pencil button next to the list name.
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an existing list name and verify that a relevant error message appears
    5. Try to submit the form with all inputs valid and verify that a success message appears.
1. Author form:
    1. Click the "New Book" button in the navigation menu
    1. Click the "new author" button in new book form
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an existing author name and verify that a relevant error message appears
    5. Try to submit the form with all inputs valid and verify that a success message appears.
1. Edit author form: (this test will apply to publisher and category as the forms are identical)
    1. Click the "Edit -> Author" button in the navigation menu
    1. Click the pencil button next to the author name.
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an existing author name and verify that a relevant error message appears
    5. Try to submit the form with all inputs valid and verify that a success message appears.
1. New Book form:
    1. Click the "New Book" button in the navigation menu
    2. Try to submit the empty form and verify that an error message about the required fields appears
    5. Try to submit the form with all inputs valid and verify that a success message appears.
1. Edit book form: 
    1. Click the "pencil"  button in the single book page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    5. Try to submit the form with all inputs valid and verify that a success message appears.
### Interesting bugs
When editing the book, if any of dropdown lists are left empty the form will not be submitted and the page will crash as by default empty list object is still an object without id that is not saved in database.
## Deployment
#### Heroku
 1. Install Heroku on a local terminal sudo (Linux OS)
``` sudo snap install --classic heroku```
2. After you install the CLI, run the ``` heroku login -i ``` command. You’ll be prompted to enter your email and password for heroku
3. Create a new heroku app by typing this command in terminal ``` heroku create```
4. In order to push a new app to heroku, we need requirements.txt, this file has all versions of all installed packages in a local virtual environment and Procfile file. With this command ```git push heroku master``` we push the new app to heroku hosting server. 
5. In heroku dashboard under Settings -> Config Vars we need to add 
	- IP : 0.0.0.0
	- Port: 500
 	- SQLALCHEMY_DATABASE_URI : sqlite:///db/bookLibrary.db
	- SECRET_KEY : ```user adds this```
#### Run app Locally
1. Clone repo from gitHub ```git clone https://github.com/edgar183/book-reading-list.git```
2. Install requirements: ```pip install -r requirements.txt``` (may require ```sudo```)
3. Run the local development server: ```python manage.py runserver```
4. Navigate to http://0.0.0.0:8080 - you will be redirected to the home page

**Differenc** between development and production versions are:
- ```debug=True``` in run.py file,  development version
- ```debug=False``` in run.py file,  productions version

## Credits
- [Blog from](https://blog.miguelgrinberg.com/index) Miguel to help with some parts of flask application. 
### Content
- The books and the content was found on [book Depository](https://www.bookdepository.com/) website

### Media
- The photos used in this site were obtained from [Pexels](https://www.pexels.com/)




