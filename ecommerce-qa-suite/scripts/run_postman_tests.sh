#!/bin/bash
newman run ecommerce-qa-suite/postman/ecommerce.postman_collection.json \
    --environment=ecommerce-qa-suite/postman/ecommerce.postman_environment.json \
    --reporters cli,junit \
    --reporter-junit-export postman-results.xml
