# Energyworx coding assignment


This project uses `Docker`/`docker-compose` to run. While in this folder, simply run
`docker-compose up`

Relevant views are found in `application/core/views.py`
Relevant urls are found in `application/core/urls.py`
Relevant models are found in `application/core/models.py`

## Tests
To run tests, cd to `cicd/docker/test_running` and execute `docker-compose up --remove-orphans --build --abort-on-container-exit`

Currently, due to some weird behaviour I haven't encountered before, it's not possible to run all the tests at once, so I run them for each test file separately.

## Functionality:

### Creation

#### Without given shortcode
- request:
    - url: `POST localhost:8000/shorten`
    - body:
        ``` json
            {
                "url": "http://www.energyworx.com"
            }
        ```
- response:
    - status: 201
    - body: 
    ``` json
        {
            "shortcode": "mfzyyh"
        }
    ```

#### With given shortcode (6 chars, alphanumeric and `_`)
- request:
    - url: `POST localhost:8000/shorten`
    - body:
        ``` json
            {
                "url": "http://www.energyworx.com",
                "shortcode": "abc_12"
            }
        ```
- response:
    - status: 201
    - body: 
    ``` json
        {
            "shortcode": "abc_12"
        }
    ```

#### Duplicate shortcode
- request:
    - url: `POST localhost:8000/shorten`
    - body:
        ``` json
            {
                "url": "http://www.energyworx.com",
                "shortcode": "abc_12"
            }
        ```
- response:
    - status: 409
    - body: 
    ``` json
        {
            "error": "Shortcode already in use"
        }
    ```

#### Invalid shortcode (not 6 characters or invalid ones)
- request:
    - url: `POST localhost:8000/shorten`
    - body:
        ``` json
            {
                "url": "http://www.energyworx.com",
                "shortcode": ":"
            }
        ```
- response:
    - status: 412
    - body: 
    ``` json
        {
            "error": "The provided shortcode is invalid"
        }
    ```

### Redirection

#### Valid shortcode
- request: `GET localhost:8000/abc_12`
- response: 302 + redirect location header

#### Invalid shortcode
- request: `GET localhost:8000/abcdef`
- response: 404

### Stats

- request:
    - url: `GET localhost:8000/abc_12/stats`
- response:
    - status: 200
    - body: 
    ``` json
        {
            "created": "2022-07-17T11:44:01.887Z", 
            "lastRedirect": "2022-07-17T11:49:04.491Z", 
            "redirectCount": 1
        }
    ```
