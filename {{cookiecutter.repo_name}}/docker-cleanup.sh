#! /bin/bash
echo "Docker image cleanup"
echo "--------------------"
docker rmi `docker images --filter 'dangling=true' -q --no-trunc`
