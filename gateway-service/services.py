import os

services = {}

movie_service = os.getenv("MOVIE_SVC_URL")
movie_service_port = os.getenv("MOVIE_SVC_PORT")
cast_service = os.getenv("CAST_SVC_URL")
cast_service_port = os.getenv("CAST_SVC_PORT")

services.update({
    "movie": {
        "url": movie_service,
        "port": movie_service_port
    },
    "cast": {
        "url": cast_service,
        "port": cast_service_port
    }
})


