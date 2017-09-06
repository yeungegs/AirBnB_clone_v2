0-hello_route.py
__init__.py
1-hbnb_route.py
2-c_route.py
3-python_route.py
4-number_route.py
5-number_template.py
	templates/5-number.html
6-number_odd_or_even.py
	templates/6-number_odd_or_even.html
models/engine/file_storage.py
	models/engine/db_storage.py
	models/state.py
web_flask/7-states_list.py
web_flask/templates/7-states_list.html
web_flask/8-cities_by_states.py
	web_flask/templates/8-cities_by_states.html
web_flask/9-states.py
web_flask/templates/9-states.html
web_flask/10-hbnb_filters.py
	web_flask/templates/10-hbnb_filters.html
	web_flask/static/
web_flask/100-hbnb.py
	web_flask/templates/100-hbnb.html
	web_flask/static/
<!-- Task Body -->
  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &quot;Hello HBNB!&quot;</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<!-- Task Body -->
  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &quot;Hello HBNB!&quot;</li>
<li><code>/hbnb</code>: display &quot;HBNB&quot;</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<!-- Task Body -->
  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &quot;Hello HBNB!&quot;</li>
<li><code>/hbnb</code>: display &quot;HBNB&quot;</li>
<li><code>/c/&lt;text&gt;</code>: display &quot;C &quot; followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<!-- Task Body -->
  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &quot;Hello HBNB!&quot;</li>
<li><code>/hbnb</code>: display &quot;HBNB&quot;</li>
<li><code>/c/&lt;text&gt;</code>: display &quot;C &quot;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display &quot;Python &quot;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is &quot;is cool&quot;</li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<!-- Task Body -->
  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &quot;Hello HBNB!&quot;</li>
<li><code>/hbnb</code>: display &quot;HBNB&quot;</li>
<li><code>/c/&lt;text&gt;</code>: display &quot;C &quot;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display &quot;Python &quot;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is &quot;is cool&quot;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &quot;<code>n</code> is a number&quot; <strong>only</strong> if <code>n</code> is an integer</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<!-- Task Body -->
  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &quot;Hello HBNB!&quot;</li>
<li><code>/hbnb</code>: display &quot;HBNB&quot;</li>
<li><code>/c/&lt;text&gt;</code>: display &quot;C &quot;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display &quot;Python &quot;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is &quot;is cool&quot;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &quot;<code>n</code> is a number&quot; <strong>only</strong> if <code>n</code> is an integer</li>
<li><code>/number_template/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 

<ul>
<li><code>H1</code> tag: &quot;Number: <code>n</code>&quot; inside the tag <code>BODY</code> </li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<!-- Task Body -->
  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &quot;Hello HBNB!&quot;</li>
<li><code>/hbnb</code>: display &quot;HBNB&quot;</li>
<li><code>/c/&lt;text&gt;</code>: display &quot;C &quot;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display &quot;Python &quot;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is &quot;is cool&quot;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &quot;<code>n</code> is a number&quot; <strong>only</strong> if <code>n</code> is an integer</li>
<li><code>/number_template/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 

<ul>
<li><code>H1</code> tag: &quot;Number: <code>n</code>&quot; inside the tag <code>BODY</code></li>
</ul></li>
<li><code>/number_odd_or_even/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 

<ul>
<li><code>H1</code> tag: &quot;Number: <code>n</code> is <code>even|odd</code>&quot; inside the tag <code>BODY</code></li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<!-- Task Body -->
  <p>Before using Flask to display our HBNB data, you will need to update some part of our engine:</p>

<p>Update <code>FileStorage</code>: (<code>models/engine/file_storage.py</code>)</p>

<ul>
<li>Add a public method <code>def close(self):</code>: call <code>reload()</code> method for deserializing the JSON file to objects</li>
</ul>

<p>Update <code>DBStorage</code>: (<code>models/engine/db_storage.py</code>)</p>

<ul>
<li>Add a public method <code>def close(self):</code>: call <code>remove()</code> method on the private session attribute (<code>self.__session</code>) <a href="http://docs.sqlalchemy.org/en/latest/orm/contextual.html#sqlalchemy.orm.scoping.scoped_session.remove">tips</a></li>
</ul>

<p>Update <code>State</code>: (<code>models/state.py</code>)</p>

<ul>
<li>If your storage engine is not <code>DBStorage</code>, add a public getter method <code>cities</code> to return the list of <code>City</code> objects from <code>storage</code> linked to the current <code>State</code></li>
</ul>

<!-- Task Body -->
  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/states_list</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li><code>H1</code> tag: &quot;States&quot;</li>
<!-- Task Body -->
  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:

<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/cities_by_states</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li><code>H1</code> tag: &quot;States&quot;</li>
<!-- Task Body -->
  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:

<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/states</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li><code>H1</code> tag: &quot;States&quot;</li>
<!-- Task Body -->
  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:

<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/hbnb_filters</code>: display a HTML page like <code>6-index.html</code>, which was done during the project <a href="https://intranet.hbtn.io/projects/268">0x01. AirBnB clone - Web static</a>

<ul>
<li>Copy files <code>3-footer.css</code>, <code>3-header.css</code>, <code>4-common.css</code> and <code>6-filters.css</code> from <code>web_static/styles/</code> to the folder <code>web_flask/static/styles</code></li>
<li>Copy files <code>icon.png</code> and <code>logo.png</code> from <code>web_static/images/</code> to the folder <code>web_flask/static/images</code></li>
<li>Update <code>.popover</code> class in <code>6-filters.css</code> to allow scrolling in the popover and a max height of 300 pixels.</li>
<li>Use <code>6-index.html</code> content as source code for the template <code>10-hbnb_filters.html</code>:

<ul>
<li>Replace the content of the <code>H4</code> tag under each filter title (<code>H3</code> States and <code>H3</code> Amenities) by <code>&amp;nbsp;</code></li>
</ul></li>
<li><code>State</code>, <code>City</code> and <code>Amenity</code> objects must be loaded from <code>DBStorage</code> and <strong>sorted by name</strong> (A-&gt;Z)</li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
<li>Import this <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql">10-dump</a> to have some data</li>
</ul>

<p><strong>IMPORTANT</strong></p>

<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (<a href="https://intranet.hbtn.io/tasks/1609">Task</a>)</li>
<li>Make sure all tables are created when you run <code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>

<!-- Task Body -->
  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:

<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/hbnb</code>: display a HTML page like <code>8-index.html</code>, done during the <a href="https://intranet.hbtn.io/projects/268">0x01. AirBnB clone - Web static</a> project

<ul>
<li>Copy files <code>3-footer.css</code>, <code>3-header.css</code>, <code>4-common.css</code>, <code>6-filters.css</code> and <code>8-places.css</code> from <code>web_static/styles/</code> to the folder <code>web_flask/static/styles</code></li>
<li>Copy all files from <code>web_static/images/</code> to the folder <code>web_flask/static/images</code></li>
<li>Update <code>.popover</code> class in <code>6-filters.css</code> to enable scrolling in the popover and set max height to 300 pixels.</li>
<li>Update <code>8-places.css</code> to always have the price by night on the top right of each place element, and the name correctly aligned and visible (i.e. screenshots below)</li>
<li>Use <code>8-index.html</code> content as source code for the template <code>100-hbnb.html</code>:

<ul>
<li>Replace the content of the <code>H4</code> tag under each filter title (<code>H3</code> States and <code>H3</code> Amenities) by <code>&amp;nbsp;</code></li>
<li>Make sure all HTML tags from objects are correctly used (example: <code>&lt;BR /&gt;</code> must generate a new line)</li>
</ul></li>
<li><code>State</code>, <code>City</code>, <code>Amenity</code> and <code>Place</code> objects must be loaded from <code>DBStorage</code> and <strong>sorted by name</strong> (A-&gt;Z)</li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
<li>Import this <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb.sql">100-dump</a> to have some data</li>
</ul>

<p><strong>IMPORTANT</strong></p>

<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (<a href="https://intranet.hbtn.io/tasks/1609">Task</a>)</li>
<li>Make sure all tables are created when you run <code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>

[![Holberton logo](https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png)](https://www.holbertonschool.com/)
# NAME OF PROJECT

### Author: Elaine Yeung [<img src="https://user-images.githubusercontent.com/23224088/27935507-4e614b68-6260-11e7-8b20-d0352ef3ff53.png" height="18px"/>](https://twitter.com/egsy) 

## Synopsis
This project introduces **INSERT DESCRIPTION HERE**

### At the end of this project students should be able to explain to anyone, **without the help of Google**:

### Resources

### Project Requirements
-   Allowed editors: `vi`, `vim`, `emacs`
-   All your Bash script files will be interpreted on Ubuntu 14.04 LTS
-   All your files should end with a new line
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   Your Bash script must pass `shellcheck` without any error
-   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
-   The second line of all your Bash scripts should be a comment explaining what is the script doing

The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash` for instance is that it will make your script portable for different OS where Bash might be in a different location.

## Project Breakdown
Task # | Type | Short description | File name and link |
---: | --- | --- | --- |
0 | **Mandatory** | | 
1 | **Mandatory** | | 
2 | **Mandatory** | | 
3 | **Mandatory** | | 
4 | **Mandatory** | | 
5 | **Mandatory** | | 

