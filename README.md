# Mashgin Full-Stack Assignment

## Tech Stack

### Frontend

 * Vue 3
 * Vuex (for state managment)
 * VueRouter
 * Production Deployment uses nginx

### Backend

 * Flask
 * Flask-Restful (for API and it documentation)
 * Flask-SqlAlchemy (with migrations using alembic)
 * Production Deployment uses gunicorn

API documentation is published on `/api/doc` endpoint.

## Caveats

### Image upload

This is not handled at all, it is assumed that the `image_id` represents an existing file in `web/public/images`.

### Authentication

For simplicity this was not implemented, neither on frontend or backend.

## Running

The easiest way to run is to execute `docker-compose build` then `docker-compose up` in root directory.

## Developing

To ensure all devs have the same environment, (VS Code Remote Containers)[https://code.visualstudio.com/docs/remote/containers] are used.

Open `api` directory with `VS Code`, hit `Ctrl+P` for command input and run `Remote-Containers: Rebuild and Reopen in Container`.

Repeat for `web`.

Both `VS Code` instances will use the same `docker-compose` environment, so you can debug both applications easily.

## Test credit cards for checkout

```
Card Number          Brand
4242 4242 4242 4242  Visa
5555 5555 5555 4444  Mastercard
3782 822463 10005    Am Ex
6011 1111 1111 1117  Discover
3056 9309 0259 04    Diners Club
3566 0020 2036 0505  JCB
6200 0000 0000 0005  UnionPay
```
