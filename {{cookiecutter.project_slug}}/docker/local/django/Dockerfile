# References:
# https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/
FROM jetblackpope/pybuntu:latest
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

# Install requirements from apt, upgrade pip, and install pipenv
RUN apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y \
    mailutils \
    build-essential \
    ca-certificates \
    redis-server \ 
    postgresql-client \
    sudo \
    gettext \
    libpq-dev \
    gcc 

COPY Pipfile* ./

RUN python -m pip install pip pipenv --upgrade


# Run pipenv and install all packages to the systems pythons site packages folder
# --system forces pipenv to install pacakges to the systems python site packages folder
# --dev causes all dev packages to be installed as well.
# --deploy will cause docker to fail when building if your lockfile is out of date compared to your Pipfile
RUN pipenv install --dev --system --deploy

# change working directory to a mounted share, will get over-ridden from docker-comose
WORKDIR /{{cookiecutter.project_slug}}

VOLUME [ "/{{cookiecutter.project_slug}}", "/entrypoint", "/start" ]

# The following will likely get over-ridden by the docker-compose file
# It runs the server on port 8000
ENTRYPOINT [ "/entrypoint" ]