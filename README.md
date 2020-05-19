# # How to Install and use
<ul>
<li>clone the repository</li>
<li>open another command prompt in the <code>root</code> folder and use <code>python install -r requirements.txt</code> to install the server dependencies</li>
<li>use <code>python manage.py runserver</code> to run the application</li>

<li><b>task/wsgi.py</b> Contains code to transform data from CSV file to Database</li>
<li><b>task/app/models.py</b> Contains code of our models </li>
<li><b>task/app/serializers.py</b> Contains code of our serializer</li>
<li><b>task/app/views.py</b> Contains code of our methods (GET data...) and the callback of our rendred HTML web page</li>
<li><b>task/urls.py</b> Contains the declaration of the URL paths</li>
<li><b>task/app/web_app/index.html</b> Contains code  the HTML web page for showing data from Database</li>
<li><b>task/app/web_app/show_data_from_csv.html</b> contains code of the HTML web page for showing data from a CSV file 'task_data.csv'</li>
</ul>
