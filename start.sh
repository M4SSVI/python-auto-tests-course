#!/usr/bin/env bash

# Declaring pytest arguments
export PYTEST_ARGUMENTS=${@:-tests/cheast.py}

# Set tag names to folders
export PROJECT_IMAGE=python-auto-tests-course

export ALLURE_RESULTS_DIR=allure-results
export PROJECT_DIR=python-auto-tests-course

# Create tags for selenium-base-image and the project folder
docker build selenium-base-image -t ${AUTOMATION_IMAGE}
docker build ${PROJECT_DIR} -t ${PROJECT_IMAGE}

# pull allure report image from docker hub
ALLURE_IMAGE=beeete2/docker-allure2

# create relevant folder structure for allure report
ALLURE_CONFIG_DIR=allure-config
ALLURE_REPORT_DIR=allure-report
ALLURE_RESULTS_DIR=allure-results
PROJECT_DIR=python-auto-tests-course

# Delete any previous allure reports
rm -rf $PROJECT_DIR/$ALLURE_REPORT_DIR

# run allure image to generate allure report based on latest test results
docker run --rm \
    -v $(pwd)/$PROJECT_DIR/$ALLURE_REPORT_DIR:/$ALLURE_REPORT_DIR \
    -v $(pwd)/$PROJECT_DIR/$ALLURE_RESULTS_DIR:/$ALLURE_RESULTS_DIR \
    -v $(pwd)/$PROJECT_DIR/$ALLURE_CONFIG_DIR:/$ALLURE_CONFIG_DIR \