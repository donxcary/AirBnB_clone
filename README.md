AirBnB clone project! - The console Group project

![AirBnB Logo](https://github.com/Cassyeh/AirBnB_clone/assets/117908223/d96cef53-9dfd-4703-a155-d12adb55fbeb)

## Description
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration...

We did the following:
* Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* Created a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* Created all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* Created the first abstracted storage engine of the project: File storage.
* Created all unittests to validate all our classes and storage engine

## The command interpreter
Our command interpreter is limited to a specific use-case. In our case, we want to be able to manage the objects of our project with some of the following operations:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Installation

You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.

```
git clone https://github.com/Cassyeh/AirBnB_clone.git
```

## Execution
The shell works like this in **interactive** mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in **non-interactive** mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
## Commands and Their Sample Usage
---
 Commands  | Sample Usage                                                        | Description                                
 --------- | ---------------------------------------------                       | ------------------------------------------ 
 `help`    | `help`                                                              | displays all commands available            
 `create`  | `create <class>`                                                    | creates new object (ex. a new User, Place) 
 `update`  | `User.update('123', {'name' : 'Cassyeh_n_Paul'})`                   | updates attribute of an object             
           | `update <class name\> <id\> <attribute name\> "<attribute value\>"` |                                            
           | `<class name\>.update(<id\>, <attribute name\>, <attribute value\>)`|                                            
           | `<class name\>.update(<id\>, <dictionary representation\>)`         |                                            
 `destroy` | `User.destroy('123')`                                               | destroys specified object                  
           | `destroy <class name\> <id\>`                                       |                                            
 `show`    | `User.show('123')`                                                  | retrieve an object from a file, a database 
           | `show <class name\> <id\>`                                          |                                            
 `all`     | `User.all()`                                                        | display all objects in class               
           | `all <class name\>`                                                 |                                            
 `count`   | `User.count()`                                                      | returns count of objects in specified class
 `quit`    | `quit`                                                              | exits                                      


## Authors

Ebubechukwu Ijezie | Email: [cassandraijezie](mailto:cassandraijezie@gmail.com)
Michael Ozioma | Email: [okonisaozioma](mailto:okonisaozioma@gmail.com)
