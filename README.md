<section class="Intro">
	<h1 align="center">HBNB - The Console</h1>
		    <p align="justify">This repository contains the second stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization. Now is added a DB to manege the information using MySql.</p>
	<hr>
</section>
<section class="prerequisities">
	<h2 align="center">Prerequisites</h2>
    	<p>This prerequisites is necesary for manage the database by MySql:</p>
        <ol>
		<details>
			<summary>Install MySql Server</summary>
	                <ul>
	                    <li><pre>$ sudo apt update</pre></li>
	                    <li><pre>$ sudo apt install mysql-server</pre></li>
	                </ul>
		</details>
		<details>
            		<summary>Install necesary modules</summary>
			<ul>
				<li>MySQLdb:</li>
			                <ul>
			                    <li><pre>$ sudo apt update</pre></li>
			                    <li><pre>$ sudo apt-get install python3-dev</pre></li>
			                    <li><pre>$ sudo apt-get install libmysqlclient-dev</pre></li>
					    <li><pre>$ sudo apt-get install zlib1g-dev</pre></li>
					    <li><pre>$ sudo pip3 install mysqlclient</pre></li>
			                </ul>
				<li>SQLAlchemy:</li>
			                <ul>
			                    <li><pre>$ sudo apt update</pre></li>
			                    <li><pre>$ sudo pip3 install SQLAlchemy</pre></li>
			                </ul>
			</ul>
		</details>
		<details>
			<summary>Prepares a MySQL server</summary>
	                <ul>
	                    <li><pre>/holbertonschool-AirBnB_clone_v2$ cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p</pre></li>
	                </ul>
		</details>
        </ol>
    <hr>
</section>
<section class="General_use">
    <h2 align="center">General Use</h2>
    <ol>
        <li>First clone this repository.</li>
             <pre>$ git clone https://github.com/Jsosholberton/holbertonschool-AirBnB_clone_v2</pre>
        <li>Once the repository is cloned locate the "console.py" file and run it as follows:</li>
            <p>-For FileStorange:</p>
	    <pre>/holbertonschool-AirBnB_clone_v2$ ./console.py</pre>
	    <p>-For DataBase:</p>
	    <pre>/holbertonschool-AirBnB_clone_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</pre>
        <li>When this command is run the following prompt should appear:</li>
            <pre>(hbnb)</pre>
        <li>This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.</li>
    </ol>
    <h2 align="center">Commands</h2>
    <ul>
        <li><code>create</code> - Creates an instance based on given class</li>
        <li><code>destroy</code> - Destroys an object based on class and UUID</li>
        <li><code>show</code> - Shows an object based on class and UUID</li>
        <li><code>all</code> - Shows all objects the program has access to, or all objects of a given class</li>
        <li><code>update</code> - Updates existing attributes an object based on class name and UUID</li>
        <li><code>quit</code> - Exits the program (EOF will as well)</li>
    </ul>
<hr>
</section>
<section class="Examples">
<h2 align="center">Examples</h2>
    <h3>Primary Command Syntax:</h3>
                <details>
                    <summary><b>Example 0: Create an object</b></summary>
                    <p>Usage: <code>create &lt;class_name&gt;</code></p>
                    <pre>(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)</pre>
                </details>
                <details>
                    <summary><h4>Example 1: Show an object</h4></summary>
                    <p>Usage: <code>show &lt;class_name&gt; &lt;_id&gt;</code></p>
                    <pre>(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)</pre>
                </details>
                <details>
                    <summary><h4>Example 2: Destroy an object</h4></summary>
                    <p>Usage: <code>destroy &lt;class_name&gt; &lt;_id&gt;</code></p>
                    <pre>(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)</pre>
                </details>
                <details>
                    <summary><h4>Example 3: Update an object</h4></summary>
                    <p>Usage: <code>update &lt;class_name&gt; &lt;_id&gt;</code></p>
                    <pre>(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)</pre>
                </details>
</section>
