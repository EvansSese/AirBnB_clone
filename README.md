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
<p>Create an oject<br>
Usage: create [class-name]</p>
<p><code>
(hbnb) create BaseModel
3ea77gbc-efb3-4121-bfw5-3dc9847181d8
(hbnb)
</code></p> <br>
<p> Show an object <br>
Usage: show [class-name]</p>
<code>
(hbnb) show BaseModel 7efdb940-d6e9-4b00-b266-3e35a1f14d9c
[BaseModel] (7efdb940-d6e9-4b00-b266-3e35a1f14d9c) {'id': '7efdb940-d6e9-4b00-b266-3e35a1f14d9c', 'created_at': datetime.datetime(2023, 8, 13, 13, 49, 25, 422462), 'updated_at': datetime.datetime(2023, 8, 13, 13, 49, 25, 422475)}</code></p><br>
<p>Update an object<br>
Usage: update [class-name] [uuid]</p>
<code>
(hbnb) update User a194b66b-f15a-4c76-964e-9e7fa1cc938a first_name "Evans"
(hbnb) show User a194b66b-f15a-4c76-964e-9e7fa1cc938a
[User] (a194b66b-f15a-4c76-964e-9e7fa1cc938a) {'id': 'a194b66b-f15a-4c76-964e-9e7fa1cc938a', 'created_at': datetime.datetime(2023, 8, 13, 13, 53, 32, 878599), 'updated_at': datetime.datetime(2023, 8, 13, 13, 56, 21, 202954), 'first_name': '"Evans"'}
(hbnb)</code></p><br>
<p>Destroy an object<br>
Usage: update [class-name] [uuid]</p>
<code>
(hbnb) destroy BaseModel 7efdb940-d6e9-4b00-b266-3e35a1f14d9c
(hbnb) show BaseModel 7efdb940-d6e9-4b00-b266-3e35a1f14d9c
* no instance found *
(hbnb)</code></p><br>
</body>
</html>
