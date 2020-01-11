# Color_Palettes
A web app to create, manage, and share color palettes.

### Prerequisite
* Python 3

### Run on Local Machine

* Clone the repository
* Open your command prompt/ Terminal on this folder
* Create a virtualenv
* Start virtual environment by `virtualenv env_name\Scripts\activate` [Windows]
* Install the dependencies with requirements.txt
* Install Crispy Forms by `pip install django-crispy-forms`
* For migrations
  * Run the command `python manage.py makemigrations`
  * Run `python manage.py migrate`
* Above command will create migrations file.
* Create superuser `python manage.py createsuperuser`
  * Provide `username`, `email`, `password` 
* After creating super user start the project by `python manage.py runserver` 
* Open browser and go to `http://127.0.0.1:8000/`
  * It will redirect you to login page
  * Provide username and password to login
  
### Working Features
Currently the web app is only working with manual input from admin page.

## N.B.
* Every features are not present at this moment.
* Note: type="color" is not supported in Internet Explorer 11 and earlier versions or Safari 9.1 and earlier versions.

### Future Updates
* Create Color palettes.
* Update Color palettes.
* Make The palettes public or private.
* Add to favourites.
* Search by User's name or color palettes' name
* Share on social media
* User Registration (Manual, gmail, facebook etc.)
