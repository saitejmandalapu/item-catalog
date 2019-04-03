# Shoes Info  
## By Mandalapu Sai Teja
This is one of the project for the Udacity [FSND Course](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## About Project:
This Project display the different shoe categories with respective shoe items, Any user can view the items but only authenticated people can add an item, edit an item, delete an item. 

## Skills Required:
   * Python
   * Html5
   * CSS
   * Flask FrameWork
   * OAuth
   * SQLAlchemy
  
## How to Install :

    Step-1 --> Install [Python](https://www.python.org/downloads)
    
    Step-2 --> Install [Vagrant](https://www.vagrantup.com/downloads.html)
    
    Step-3 --> Install [VirtualBox](https://www.virtualbox.org/wiki/downloads)
    
    Step-4 --> Install [Git](https://git-scm.com/download/win) --> For Windows
    
    Step-5 --> Launch the vagrant virtual machine inside vagrant sub-directory then open Git Bash: `$vagrant up`
    
    Step-6 --> Login to vagrant virtual machine --> `$vagrant ssh`
    
    Step-7 --> Change directory to /vagrant --> `$cd /vagrant/`
    
    Step-8 --> Install the requirement project modules are:
    
        * `sudo pip install flask`
        * `sudo pip install oauth2client`
        * `sudo pip install sqlalchemy`
        * `sudo pip install requests`
    
     Step-9 --> Create application database:`$python database_setup.py`
    
     Step-10 --> Inserting application data in database -->`$python database_init.py`
     Step-11 --> Run the main project file -->`python shoeland.py`
    
     Step-12 --> Access the application any local browser[http://localhost:5000](http://localhost:5000)

 ### JSON EndPoints: In this project we create json endpoints using REST architecture

 1. Display the all Categories with Items : `http://localhost:5000/category/JSON`

 2. Display the item of given category: `http://localhost:5000/category/1/items/JSON`

 3. Display the all Items : `http://localhost:5000/category/items/JSON`

 4. Display the categories: `http://localhost:5000/category/category/JSON`
 












