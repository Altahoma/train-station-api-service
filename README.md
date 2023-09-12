## Train Station API Service

![Django](https://img.shields.io/badge/Django-4.2.4-brightgreen.svg)
![Django Rest Framework](https://img.shields.io/badge/Django%20Rest%20Framework-3.14-blue.svg)
![Docker Compose](https://img.shields.io/badge/Docker%20Compose-3.9-brightgreen.svg)

Train Station API Service is a Django Rest Framework (DRF) application that provides a comprehensive API for managing
train station information.

1. Train Station CRUD API: Manages all ticket data including creation, retrieval, update, and deletion of records.
2. To allow users to interact with the API securely, Train Station API Service provides user registration and JWT
   authentication. Users can register and obtain a JWT token to authenticate themselves.

### Installation

1. Clone this repository to your local machine:

```
    git clone https://github.com/Altahoma/train-station-api-service
```

2. Copy the `.env.sample` file to `.env` and configure the environment variables:

```
    cp .env.sample .env
```

3. Run command:

```
    docker-compose up --build
```

4. For temporary access to the API, you can use the following admin user account:

- **Email:** admin@mail.com
- **Password:** admin


- Please note that this is a temporary account and should be used only for testing and evaluation purposes. It is
  recommended to create your own user accounts for production use.

### Usage

To access the API, navigate to http://localhost:8000/api/ in your web browser or use a tool like curl or Postman.

### Endpoints

Station CRUD API:

- `/station/stations/`
- `/station/train-types/`
- `/station/crews/`
- `/station/trains/`
- `/station/orders/`
- `/station/routes/`
- `/station/journeys/`

User API:

- `/user/register/`
- `/user/token/`
- `/user/token/refresh/`
- `/user/token/verify/`

Documentation:

- `/doc/swagger/`: To access the API documentation, you can visit the interactive Swagger UI.
