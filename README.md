# qr-generator
generates qr code

*TODO:*

- [x] generate qr code
- [ ] qr code with rounded corners
- [ ] qr code with logo inside

## API

- **POST** `/api/v1/qr`
  *request body*

  ```json
  {
    "url": "https://github.com/gosha20777/qr-generator"
  }
  ```

  *response*
  image/jpeg, chanked image:

  ![qr-code](docs/example.jpg)

## Installation

You can build and run the service using docker. if you want to build a docker image yourself or build it into your host, see the instructions below.

### Using with Docker-Compose

1. install [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
2. install [docker-compose](https://docs.docker.com/compose/install/)
3. run commands: 

```bash
$ git clone https://github.com/gosha20777/qr-generator.git
$ cd qr-generator
$ docker-compose up
```

### Using without Docker

- install python 3.7 and python3-pip and virtualenv

```bash
$ apt install python3.7
$ apt install python3-pip
$ python3.7 -m pip install --upgrade pip
$ python3.7 -m pip install virtualenv
```

- install service

```bash
$ git clone https://github.com/gosha20777/qr-generator.git
$ cd qr-generator
$ virtualenv .virtualenv
$ source .virtualenv/bin/activate
(.virtualenv) $ pip install -r requirements.txt --log-config log-config.yaml
```

- run service

```bash
(.virtualenv) $ uvicorn server:app --host localhost --port 5000
```