![Logo](/app/static/img/logo1.png)
## CLEAN COVID 19 

The current project is a website with the purpose of providing clear and reliable information related to the novel Codiv-19 pandemic. 
It consists of: 
**Index** Updated Dashboard from Tableau Public linked to John Hopkins database.
**About Covid** Flexbox with accurate information about Coronavirus, provided by World Health Organization, Harvard Medical School, John Hopkins.
**Infographics** Curated infographics about Stay Home, Prevention, Symptoms. This series take part of the author's portfolio in the Infographcis Module at Code University.
**Charts** Charts created using the reported numbers of the World Health Organization, from the source https://ourworldindata.org/coronavirus .
**Chatbot** A chatbot has been included. It's built with a template in Dialogflow. Basic functions providing information are active. Some functions are not operational.

Development Status: Deployed.
Deployed Domain: **www.cleancovid19.net**

It is as a student project at Code University of Applied Sciences. 

### Run The Code On Your Local Machine
In order to run the code you will need to:

1. Clone the repository.

      `git clone https://github.com/cardox6/cc19.git `

2. It is recommended to create a Virtual Enviroment for the directory.

     `python3 -m venv`

3. Activate the venv.

    `source venv/bin/activate`
    
4. Install the requirements.

    `pip install requirements.txt`
    
5. Run The Web with Flask or Gunicorn.

    * `flask run`
    * `gunicorn --bind 0.0.0.0:5000 wsgi:app`

### Technologies 
Built with HTML, CSS (styling and animation), JavaScript, Python, Flask, Dialogflow, JupyterNotebooks.

### Deployment 
The project has been conceived in an environment, therefore Requirements should be met in order to avoid incompatibilities. The website has been deployed on a Google Cloud Server (Ubunt 18). Files are  dinamically handled by Gunicorn, calling on Nginx for static files.
It is secured 'HTTPS' with Certificates provided by Let's Encrypt.

### Responsive
The web is built responsive for Desktop, Mobile (Iphone X), Tablet(Ipad). 

#### Desktop 
![Desktop](/captions/Desktop.png)

#### Iphone
![Iphone](/captions/Iphone.png)

#### Ipad
![Ipad](/captions/Ipad.png)

### Thank you 
Special appreciation to Adam Roe, Fabian Volkers and my fellow colleagues for all their support.

