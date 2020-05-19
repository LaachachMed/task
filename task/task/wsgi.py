"""
WSGI config for task project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import pandas as pd
import task.app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task.settings')

application = get_wsgi_application()

# when the application will be lunched it will be shown a message that if you want to transfer data from CSV file to Database?
# if the answer is no nothing will be happen and the other tasks (get data ...) still function normally
# if the answer is yes it will be ask you to Enter the CSV relative path for our case is simply : task_data.csv and the data will be load to Database

if input("Do you want to transfer data from CSV file to Database? \n") == "yes":
    df = pd.read_csv(input("Enter your CSV file Path : "))
    print(df)
    for row in df.itertuples():
        # print(row[1])
        data = task.app.models.task_data()
        data.id = row[1]
        data.timestamp = row[2]
        data.temperature = row[3]
        data.education = row[4]
        data.save()