<!DOCTYPE html>
<html>
<head>
</head>
<body>
<h1>AirBnB - Console</h1>
<h2>Project Description</h2>
<p>The repository contains the team project which  is the first step towards building your first full web application: the AirBnB clone. Console commands allow the user to:
<ol>
<li>Create</li>
<li>Update</li>
<li>Destroy objects</li>
<li>Manage file storage</li>
</ol>
Using a system of JSON to create simple flow of serialization/deserialization and create file storage engine of the project.</p>
<h1>Command Interpreter Description</h1>
<p>In our case, we want to be able to manage the objects of our project:
<ul>
<li>Create a new object (ex: a new User or a new Place)</li>
<li>Retrieve an object from a file, a database etc…
<li>Do operations on objects (count, compute stats, etc…)</li>
<li>Update attributes of an object</li>
<li>Destroy an object</li>
</ul>
</p>
<h2>How to Start</h2>
<ol>
<li>Clone the repository.</li>
<li>On the cloned repository locate the "console.py" file </li>
<li>When run the prompt command should appear</li>
<li>The prompt gets you to the "hbnb" console.</li>
</ol>
<h2>How to Use</h2>
<p>
To use the console, you can run the following commands
</p>
<ol>
<li>create - This command creates an instance of a class</li>
<li>destroy - This command destroys an instance of a class based on UUID</li>
<li>show - Shows an object based on given class and UUID</li>
<li>all - Shows all instances of each class</li>
<li>update - Updates an instance based on UUID provided</li>
<li>quit - Exits the console appropriately</li>
</ol>
<h2>Examples</h2>
<p>Here are some examples on how to use the console</p>
###### Create an oject
<p>Usage: create <class_name></p>
```
(hbnb) create User
```
```
(hbnb) create BaseModel
3ea77gbc-efb3-4121-bfw5-3dc9847181d8
(hbnb)
```
</body>
</html>
