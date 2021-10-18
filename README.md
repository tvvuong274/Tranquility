<!-- PROJECT LOGO -->
<div align="center"><br />
<p align="center" style="width: 100%">
    <img src="http://minerva.vn/wp-content/uploads/2020/06/logo.png" alt="Logo" style="-webkit-user-select: none;margin: auto;">

<h3 align="center">IDM</h3>
</p>
</div>

Identity Management & Access Management

## I. Requirements:
    - python >= 3.8.10

## II. Setup environment:
- How to setup environment:
    1. Install [cx_oracle](https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html)
    2. Setup Python virtual environment:
        
        For Linux:
        ```sh
        cd base-django
        virtualenv env -p python3
        source env/bin/activate
        pip install -r requirements.txt
        ```

        For Windows:
        ```powershell
        cd base-django
        virtualenv env -p py3
        env/Scripts/activate
        pip install -r requirements.txt
        ```
        
    4. In folder `idm_config`
        - Copy a content of file `database.py.yml` to `database.py` file and config some parameters in it if necessary (`already configured`).
        - Copy a content of file `root_local.py.yml` to `root_local.py` file and config some parameters in it if necessary (`already configured`).
            **NOTE**:
            - CHANGE `LOCAL_DEBUG=False` FOR PRODUCTION: Whether or not run the application in DEBUG mode. This should be set to `False` in production.

    5. Run
        - For local development: type command `python manage.py runserver <host>:<port>`
            ```sh
            python manage.py runserver 127.0.0.1:8000
            ```
        - For production: Use [`Gunicorn`](https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/gunicorn/) to start server.
        
    6. Documentation
        - Swagger: `http://127.0.0.1:8000/api/v1/docs/`
        - Redoc: `http://127.0.0.1:8000/api/v1/redoc/`
    

## III. Note for developers:
- Cách lấy bearer token để dùng cho các api trong BaseAPIView:
    -  Gọi api `/api/v1/users/login/` dùng Basic Auth
        -  username mặc định:  `admin`
    	-  password mặc định:  `123`
    -  Hoặc chạy đoạn cUrl sau:
        ```curl
        curl --location --request POST 'http://127.0.0.1:8000/api/v1/users/login/' --header 'Authorization: Basic YWRtaW46MTIz'
        ```

