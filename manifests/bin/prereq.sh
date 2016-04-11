#!/bin/bash

if [ -z "$TSP_EMAIL" -o -z "$TSP_API_TOKEN" -o -z "$TSP_API_HOST" ]
then
    if [ -z "$TSP_EMAIL" ]
    then
        echo 'Environment variable $TSP_EMAIL not set'
    fi

    if [ -z "$TSP_API_TOKEN" ]
    then
        echo 'Environment variable $TSP_API_TOKEN not set'
    fi

    if [ -z "$TSP_API_HOME" ]
    then
        echo 'Environment variable $TSP_API_HOME not set'
    fi
    exit 1
fi

