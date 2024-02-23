# CodeLeapApi

Test built using Django and Django Rest Framework, core rest api features are located in the `CodeLeapApp/` folder.

> Online Url: https://gldevbr.pythonanywhere.com/carrers/

# Requirements

* Python 3.12.2

# Running locally

assuming you're on a virtual environment of your preference, just type:
```
pip install -r requirements.txt
```
after installing dependencies, run migrations with:
```
python manage.py migrate
```
then you are ready to go, run the project with this command:
```
python manage.py runserver
```

# Running tests

As we are using generated routes we used the `drf_test_generator` package to bootstrap our tests then adapted them to meet the api criterias.

The tests are located in the **CodeLeapApp** folder in the `tests.py` file.

The tests verifies all the Key Concepts above, including username that cannot be changed and all CRUD logic.

You can run the tests with the command above:

```
python manage.py test
```

# Key concepts

- The project itself is built using Django and DNF
- **id**, **username**, **created_datetime** cannot be changed on update (for reference in how username is skipped from the update process please refer to the views.py file)
- For best performance we are using paginated results, **10 results per page** (for reference on pagination details, please refer to the settings.py file)
- Delete should not return any data
- built using a virtual environment
- Api tests we're done using **Postman**

# Example response

```
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "username": "@testnow",
            "created_datetime": "2024-02-21T22:10:47.897422Z",
            "title": "This title is amazing too, oh... edited",
            "content": "Well the content goes here you know..."
        },
        {
            "id": 3,
            "username": "@testnow2024",
            "created_datetime": "2024-02-21T22:15:57.175008Z",
            "title": "This title is amazing too!",
            "content": "My content is a bit wider, see? wideeeeeeeeeeeer, :D"
        },
        {
            "id": 4,
            "username": "@testnow2024",
            "created_datetime": "2024-02-21T22:18:02.963786Z",
            "title": "Curious one title",
            "content": "I mean looks like someone deleted our friend at the second id, the number 2, those times I miss authentication, 👍"
        }
    ]
}
```

# License

[MIT](https://github.com/gldevbr/CodeleapApi/blob/main/LICENSE)