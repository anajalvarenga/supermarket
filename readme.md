1. Set up a Local programming environment for python 3  ([tutorial](https://www.digitalocean.com/community/tutorial_series/how-to-install-and-set-up-a-local-programming-environment-for-python-3))
2. Active your virtual environment
    ```
    source my_env/bin/activate
    ```
3. Install flask
    ```
    pip install Flask Flask-SQLAlchemy
    ```
4. Set the app package as the place where Flask should look for the create_app() factory function:
    ```
    export FLASK_APP=app
    ```
5. Set the FLASK_ENV environment variable to run the application in development mode:
    ```
    export FLASK_ENV=development
    ```
6. Open the Flask shell:
    ```
    flask shell
    ```
7. Start the database by copying the information from the db_init.py file and pasting it into the terminal
8. Exit the shell by running
    ```
    exit()
    ```
9. Run the application
    ```
    flask run
    ```