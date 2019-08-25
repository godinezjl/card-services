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

### Deployment on Mac
Please note that the following instructions are to deploy this application in a MacOS local environment. For Windows or Linux, please follow the setup instructions on the links provided above.

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
```

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
#### Supported APIs
To access the APIs, use your favorite Terminal application like curl or Httpie. The below examples are using Httpie.

#### Response Parameter
 * check_digit = The Luhn digit calcualted for this card
 * full_credit_card_number = The full credit card number 
 ** Supported formats: xxxx-xxxx-xxxx or xxxx xxxx xxxx or xxxxxxxxxxxx
 * issuer = The issuing authority
 ** Supported issuers: American Express, Discover, Master Card, and Visa)
 * issuer_identification_number = the iin associated with the issuer
 * major_industry_identifier = The mii associated with the issuer
 * personal_account_number = The account number assigned to the individual card holder
 
##### Check If A Credit/Debit Card Number Is Valid
To check if a given credit or debit card is valid, simply call your local server and set the full_credit_card_number parameter as follows.
``` Bash
http --form POST http://127.0.0.1:8000/ \full_credit_card_number="4147202220927584"
```

You should see an output similar to the below.
```javascript
HTTP/1.1 200 OK
Allow: POST, GET, OPTIONS
Content-Length: 182
Content-Type: application/json
Date: Sun, 25 Aug 2019 14:00:09 GMT
Server: WSGIServer/0.2 CPython/3.7.4
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "check_digit": 4,
    "full_credit_card_number": "4147202220927584",
    "issuer": "Visa",
    "issuer_identification_number": 4,
    "major_industry_identifier": 4,
    "personal_account_number": 14720222092758
}
```

##### Valid Request
Note that a valid request will return HTTP 200 OK, to tell the calling program that the card number is valid.

If the card is not valid, you will get a HTTP 400 status like the one below
``` javascript
HTTP/1.1 400 Bad Request
Allow: POST, GET, OPTIONS
Content-Length: 2
Content-Type: application/json
Date: Sun, 25 Aug 2019 14:03:32 GMT
Server: WSGIServer/0.2 CPython/3.7.4
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN
```

## Running the tests
Tests can be executed by running unittest on the credit_card_service/ directory, and using the path Test_* to find all tests. In Terminal, ensure you are in the credit_card_service directory, and run the following command
```Bash
python -m unittest discover -s api -p "test_*.py"
```

If all tests pass, you should see a similar outout to the one below
```Bash
----------------------------------------------------------------------
Ran 30 tests in 0.003s

OK

```
If one or more of the tests fail, you should see a trace of the test that failed and the location.

## Contributing

  

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.
  

## Authors
* **Jose Godinez** 

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
