# AirBnB clone project! (The Holberton B&B)

The AirBnB clone project starts now until. The goal of the project is to deploy on your server a simple copy of the AirBnB website.

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, you will have a complete web application composed by:

A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
A website (the front-end) that shows the final product to everybody: static and dynamic
A database or files that store data (data = objects)
An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Starting 🚀

_In order to run the program you must make a copy of the [**repository**] (https://github.com/vasketz/AirBnB_clone.git)_

```
$ git clone https://github.com/vasketz/AirBnB_clone.git
```

### Pre requirements 📋

_All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)_


## Running the program ⚙️

_To run the program type:_

```
$ ./console.py
```
_You will access the console where you can write the help command to see the information of the commands_
```
(hbnb) help
```
_You should see this screen:_

```
Documented commands (type help <topic>):
========================================
EOF  help  quit  create  show  destroy
all  update
```
<h2> Classes to build your objects</h2>

 Class name        | Attributes |
| ----------- | ----------- |
|BaseModel   | id, created_at, updated_at.|
|BaseModel   | email, password, first_name, last_name.|
|State   | name, state_id.|
|City    | name. |
|Amenity   | name.|
|Place   | city_id, BaseModel_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night latitude, longitude amenity_ids.|
|Review   | place_id, BaseModel_id, text.|

<h2> Console Commands</h2>

 Command        | Description |
| ----------- | ----------- |
|create [Class name]  | Creates a new instance of one of the classes above, saves it into a JSON file, and prints the id of the instance you created. Ex: `$ create BaseModel`.|
|show [Class name] [id]  | Prints the string representation of the instance based on the class name and id. Ex: `$ show BaseModel 1234-1234-1234`.|
|destroy [Class name] [id]  | Deletes the instance based on the class name and id. Also, saves the changes into the JSON file Ex: `$ destroy BaseModel 1234-1234-1234`.|
|all [optional Class name]  | Prints all string representation of all instances based or not on the class name. Ex: `$ all BaseModel or $ all`.|
|update [Class name] [id] [attribute name] ["attribute value"]  | Updates an instance based on the class name and id by adding or updating attribute, saves the changes into the JSON file. Ex: `$ update BaseModel 1234-1234-1234 first_name "Marce"`. |

### Examples 🔩

_Explica que verifican estas pruebas y por qué_

## all command

```
(hbnh) all
["[BaseModel] (11c736fd-9638-4124-b034-632059325fa4) {'id': '11c736fd-9638-4124-b034-632059325fa4', 'created_at': datetime.datetime(2020, 11, 4, 23, 39, 49, 252939), 'updated_at': datetime.datetime(2020, 11, 4, 23, 39, 49, 252962)}"]
(hbnh)
------------------------------------
$ echo "all" | ./console.py
(hbnb)
["[BaseModel] (11c736fd-9638-4124-b034-632059325fa4) {'id': '11c736fd-9638-4124-b034-632059325fa4', 'created_at': datetime.datetime(2020, 11, 4, 23, 39, 49, 252939), 'updated_at': datetime.datetime(2020, 11, 4, 23, 39, 49, 252962)}"]
(hbnb)
$

```

## update command

```
(hbnh) update BaseModel 11c736fd-9638-4124-b034-632059325fa4 name "Betty"
(hbnh)
------------------------------------
$ echo "update BaseModel 11c736fd-9638-4124-b034-632059325fa4 name "Betty"" | ./console.py
(hbnb)
(hbnb)
$

```

## destroy command

```bash
(hbnh) destroy BaseModel 11c736fd-9638-4124-b034-632059325fa4
(hbnh)
------------------------------------
$ echo "destroy BaseModel 11c736fd-9638-4124-b034-632059325fa4" | ./console.py
(hbnb)
(hbnb)
$

```
## Autores ✒️

_This project was made:_

* **Marcela Areiza** - *Main Work* - [mareizaa](https://github.com/mareizaa)
* **Andrés Vásquez** - *Main Work* - [vasketz](https://github.com/vasketz)

You can see all contributors of this project [contributors](https://github.com/vasketz/AirBnB_clone.git) who have participated in this project.
