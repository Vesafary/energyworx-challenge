# Energyworx coding assignment

I used a simple Django service + PostgreSQL for this challenge, since it's fairly simple to setup. To make it easy to run, it will run via `Docker`/`docker-compose`. While in this folder, simply run `docker-compose up` to start it up.

Relevant views are found in `application/core/views.py`.

Relevant urls are found in `application/core/urls.py`.

Relevant models are found in `application/core/models.py`.

Tests are found in `tests/views`.

As I don't have a mac, that part is untested. However, since it runs in Docker, it should work without issues. For M1/M2 devices, the added `platform` tags in docker-compose should make sure everything behaves. 

## Tests
To run tests, cd to `cicd/docker/test_running` and execute `docker-compose up --remove-orphans --build --abort-on-container-exit`

Currently, due to some weird behaviour I haven't encountered before, it's not possible to run tests on all the test files at once, so in the script I run tests multiple times (for each test file separately). This makes it a bit slower and adds terminal output, so if I have some time I'll take a look to fix.

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
