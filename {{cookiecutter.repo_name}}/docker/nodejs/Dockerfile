FROM {{cookiecutter.repo_name}}-base
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -
RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
       apt-get install -y --force-yes --no-install-recommends nodejs

WORKDIR /react/
