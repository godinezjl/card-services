# card-services

Card Services provides tools for validating credit card or debit card numbers by using the Luhn Algorithm.

## Getting Started

Download the code directly from github by cloning this repo.

### Prerequisites

Card Services was built with Python 3.7.4 and DJango 2.0.3. Before you can rund this application, please follow the installation instructions for both Python and DJango based on your operating system.

#### Helpful References
  * https://appdividend.com/2018/03/28/how-to-install-django-in-mac/
  * https://docs.python-guide.org/starting/install3/osx/
  * https://docs.python-guide.org/starting/install/win/#install-windows

### Installing on Mac
To get started, lets begin by setting up the python3 environment. By default, MacOS ships with Python2. We should not uninstall it as many programs rely on that version.

#### Open terminal and type the following command

```
brew install python3
```
#### Check for Python 3 Version
To check the proper version was installed, type the following command and ensure the output is Python 3.x.x, where x stands for some version of the Python 3 release.

```
python3 --version
Python 3.7.4

```

#### Install PIP Package Management System
Now that python is installed, we need to install the PIP package management system. In your terminal type the following command.
```
sudo easy_install pip
```

#### Install VirtualEnv for Python
Now, let's install the VirtualEnv to allow us to run multiple version of python3 in our system.
```
sudo pip install virtualenv
```

Once installed, we need to create the virtual environment inside the folder where we will keep our application. For me, my folder is under /users/jose/credit_card_service. 

```
jose$ cd /users/jose/credit_card_service
jose$ virtualenv --python=python3 venv
```
This should create the vurtual environment folder called venv. Now lets activate the virtual environment by executing the following command:
```
source venv/bin/activate
```
Note that the promt will now change to inclue (venv) at the begining. This is an indication that you are running in the virtual environment.

#### Install Django
Now lets install the django framework in the virtual environment. Stay in that folder and execute the following command.
```
sudo pip install Django==2.0.3
```

#### Install Django Framework
Now lets install the django framework by executing the following command.
```
sudo pip install djangorestframework
```

#### Create your Django Project
Once the framework is installed, it is time to create a new django project by executing the following command. Note that the project can be called whatever you want. For this project, I called it API. Also note the dot at the end of the command. That tells the django admin to installed it in the current location.
```
django-admin.py startproject api .
'''
This should create a new folder called api. That's where the project data will be hosted. Now we can verify that django got installed properly by running the following command.
```
python manage.py runserver
```
if everything is working well, you will see a url that you can go to and will see the home page of your website. Quit running the server, by typing control x, so that we can create the application.

#### Create Your Application
With django installed, run the following command
```
django-admin.py startapp credit_card
```

#### Copy This App to the application Location
Now that you have created the application, clone the contents of this application to the credit_card folder.

#### Run The Server
Now it's time to run your server so that you can host the application. Run the following command.
```
python manage.py runserver
```

## Running the tests

  

Explain how to run the automated tests for this system

  

### Break down into end to end tests

  

Explain what these tests test and why

  

```

Give an example

```

## Deployment

  

Add additional notes about how to deploy this on a live system
  

## Contributing

  

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.
  

## Authors
* **Jose Godinez** 

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
