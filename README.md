<img src="https://github.com/johncoleman83/AirBnB_clone/blob/master/dev/HBTN-hbnb-Final.png" width="160" height=auto />

# AirBnB Clone Phase #1

: python BaseModel Class, unittests, python CLI, & web static

## Description

Project attempts to clone the the AirBnB application and website, including the
database, storage, RESTful API, Web Framework, and Front End.

## Environment

* __OS:__ Ubuntu 14.04 LTS
* __language:__ Python 3.4.3
* __style:__ PEP 8 (v. 1.7.0)

<img src="https://github.com/johncoleman83/AirBnB_clone/blob/master/dev/hbnb_step5.png" />

## Testing


#### `unittest`

This project uses python library, `unittest` to run tests on all python files.
All unittests are in the `./tests` directory with the command:

* `python3 -m unittest discover -v ./tests/`

The bash script `init_test.sh` executes all these tests:

  * checks `pep8` style

  * runs all unittests

  * runs all w3c_validator tests

  * cleans up all `__pycache__` directories and the storage file, `file.json`

**Usage:**

```
$ ./dev/init_test.sh
```

#### CLI Interactive Tests

This project uses python library, `cmd` to run tests in an interactive command
line interface.  To begin tests with the CLI, run this script:

```
$ ./console.py
```

* For a detailed description of all tests, run these commands inside the
custom CLI:

```
$ ./console.py
(hbnb) help help
List available commands with "help" or detailed help with "help cmd".
(hbnb) help

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  airbnb  create   help  show
BaseModel  EOF   Review  User   all     destroy  quit  update

(hbnb) help User
class method with .function() syntax
        Usage: User.<command>(<id>)
(hbnb) help create
create: create [ARG]
        ARG = Class Name
        SYNOPSIS: Creates a new instance of the Class from given input ARG
        EXAMPLE: create City
                 City.create()
```

* Tests in the CLI may also be executed with this syntax:

  * **destroy:** `<class name>.destroy(<id>)`

  * **update:** `<class name>.update(<id>, <attribute name>, <attribute value>)`

  * **update with dictionary:** `<class name>.update(<id>, <dictionary representation>)`


#### Continuous Integration

Uses [Travis-CI](https://travis-ci.org/) to run all tests on all commits to the
github repo

## Authors

* MJ Johnson, [@mj31508](https://github.com/mj31508)
* David John Coleman II, [davidjohncoleman.com](http://www.davidjohncoleman.com/)

## License

Public Domain, no copyright protection
-setup_web_static.sh
-pack_web_static.py
-do_deploy_web_static.py
-deploy_web_static.py
00-clean_web_static.py
<!-- Task Body -->
  <p>Write a Bash script that sets up your web servers for the deployment of <code>web_static</code>. It must:</p>

<ul>
<li>Install Nginx if it not already installed</li>
<li>Create the folder <code>/data/</code> if it doesn&#39;t already exist</li>
<li>Create the folder <code>/data/web_static/</code> if it doesn&#39;t already exist</li>
<li>Create the folder <code>/data/web_static/releases/</code> if it doesn&#39;t already exist</li>
<li>Create the folder <code>/data/web_static/shared/</code> if it doesn&#39;t already exist</li>
<li>Create the folder <code>/data/web_static/releases/test/</code> if it doesn&#39;t already exist</li>
<li>Create a fake HTML file <code>/data/web_static/releases/test/index.html</code> (with simple content, to test your Nginx configuration)</li>
<li>Create a symbolic link <code>/data/web_static/current</code> linked to the <code>/data/web_static/releases/test/</code> folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.</li>
<li>Give ownership of the <code>/data/</code> folder to the <code>ubuntu</code> user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.</li>
<li>Update the Nginx configuration to serve the content of <code>/data/web_static/current/</code> to <code>hbnb_static</code> (ex: <code>https://mydomainname.tech/hbnb_static</code>). Don&#39;t forget to restart Nginx after updating the configuration:

<ul>
<li>Use <code>alias</code> inside your Nginx configuration</li>
<li><a href="http://stackoverflow.com/questions/10631933/nginx-static-file-serving-confusion-with-root-alias">Tip</a></li>
</ul></li>
</ul>

<p>Your program should always exit successfully.
<strong>Don&#39;t forget to run your script on both of your web servers.</strong></p>

<!-- Task Body -->
  <p>Write a Fabric script that generates a <a href="https://en.wikipedia.org/wiki/Tar_(computing)">.tgz</a> archive from the contents of the <code>web_static</code> folder of your AirBnB Clone repo, using the function <code>do_pack</code>.</p>

<ul>
<li>Prototype: <code>def do_pack():</code></li>
<li>All files in the folder <code>web_static</code> must be added to the final archive</li>
<li>All archives must be stored in the folder <code>versions</code> (your function should create this folder if it doesn&#39;t exist)</li>
<li>The name of the archive created must be <code>web_static_&lt;year&gt;&lt;month&gt;&lt;day&gt;&lt;hour&gt;&lt;minute&gt;&lt;second&gt;.tgz</code></li>
<li>The function <code>do_pack</code> must return the archive path if the archive has been correctly generated. Otherwise, it should return <code>None</code></li>
</ul>

<!-- Task Body -->
  <p>Write a Fabric script (based on the file <code>1-pack_web_static.py</code>) that distributes an archive to your web servers, using the function <code>do_deploy</code>:</p>

<ul>
<li>Prototype: <code>def do_deploy(archive_path):</code></li>
<li>Returns <code>False</code> if the file at the path <code>archive_path</code> doesn&#39;t exist</li>
<li>The script should take the following steps:

<ul>
<li>Upload the archive to the <code>/tmp/</code> directory of the web server</li>
<!-- Task Body -->
  <p>Write a Fabric script (based on the file <code>2-do_deploy_web_static.py</code>) that creates and distributes an archive to your web servers, using the function <code>deploy</code>:</p>

<ul>
<li>Prototype: <code>def deploy():</code></li>
<li>The script should take the following steps:

<ul>
<li>Call the <code>do_pack()</code> function and store the path of the created archive</li>
<li>Return <code>False</code> if no archive has been created</li>
<li>Call the <code>do_deploy(archive_path)</code> function, using the new path of the new archive</li>
<li>Return the return value of <code>do_deploy</code></li>
</ul></li>
<li>All remote commands must be executed on both of web your servers (using <code>env.hosts = [&#39;&lt;IP web-01&gt;&#39;, &#39;IP web-02&#39;]</code> variable in your script)</li>
</ul>

<p>In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =...)</p>

<!-- Task Body -->
  <p>Write a Fabric script (based on the file <code>3-deploy_web_static.py</code>) that deletes out-of-date archives, using the function <code>do_clean</code>:</p>

<ul>
<li>Prototype: <code>def do_clean(number=0):</code></li>
<li><code>number</code> is the number of the archives, including the most recent, to keep.

<ul>
<li>If <code>number</code> is 0 or 1, keep only the most recent version of your archive. </li>
<li>if <code>number</code> is 2, keep the most recent, and second most recent versions of your archive.</li>
<li>etc.</li>
</ul></li>
<li>Your script should:

<ul>
<li>Delete all unnecessary archives (all archives minus the number to keep) in the <code>versions</code> folder</li>
<li>Delete all unnecessary archives (all archives minus the number to keep) in the <code>/data/web_static/releases</code> folder of both of your web servers</li>
</ul></li>
<li>All remote commands must be executed on both of your web servers (using the <code>env.hosts = [&#39;&lt;IP web-01&gt;&#39;, &#39;IP web-02&#39;]</code> variable in your script)</li>
</ul>

<p>In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =...)</p>

