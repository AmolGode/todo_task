# How to setup project - In Ubuntu 20.04 LTS

1] create virtual env variable
> virtualenv env  [env is name]

2] Activate env
> source env/bin/activate

3] install django and django-rest-framework
> pip install django
> pip install django-rest-framework

4] install mysqlclient 
> pip install mysqlclient

5] install corsheaders
> pip install django-cors-headers

6] migrate database changes
 - go to directory : /todo_list_task/todo_task/ where manage.py file is present
 
 > python manage.py makemigrations
 ...
 > python manage.py migrate

7] Run the project
 > python manage.py runserver
 

# APIs
1] http://127.0.0.1:8000/user_api/add_user/
make post request with username, email, password, first_name, last_name,mobile

2] http://127.0.0.1:8000/user_api/login_user/
make post request with email adn password

3] http://127.0.0.1:8000/task_api/add_task/
make post request with task_title, task_desc, user

4] http://127.0.0.1:8000/task_api/delete_task/<task_id>/
make delete request with task_id

5] http://127.0.0.1:8000/task_api/complete_task/<task_id>/
make patch request with task_id

5] http://127.0.0.1:8000/task_api/get_all_tasks/<user_id>/
make get request with task_id

