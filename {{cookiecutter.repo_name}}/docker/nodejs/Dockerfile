FROM {{cookiecutter.repo_name}}-base
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -
RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
       apt-get install -y --force-yes --no-install-recommends nodejs

WORKDIR /react/
# RUN npm install \
#       browserify@13.0.0 \
#       watchify@3.7.0 \
#       react@0.14.7 \
#       react-dom@0.14.7 \
#       react-router@1.0.3 \
#       history@1.17.0 \
#       babelify@7.2.0 \
#       babel-preset-react@6.5
