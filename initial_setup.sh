#!/bin/sh

function startprogram(){
    echo ""
    echo "#############################################################################"
    echo "1) Makemigrations"
    echo "2) Migrate"
    echo "3) Createsuperuser"
    echo "4) Runserver"
    echo "press any the key number to perform that operation or type 'all' to perform all or type 'exit' to go out"
    read input
    echo ""

     case $input in
        "1" )
            makemigrations;;
        "2" )
            migrate;;
        "3" )
            createsuperuser;;
        "4" )
            runserver;;
        "all" )
            all_commands;;
        "exit" )
            exit;;
        "*" )
            continue;;
    esac

    startProgram
}

function makemigrations() {
    echo "Applying migrations"
    echo "#############################################################################"
    python manage.py makemigrations
    echo "#############################################################################"
}

function migrate() {
    echo "Please Be sure you have done makemigrations before this"
    echo "#############################################################################"
    python manage.py migrate
    echo "#############################################################################"
    echo "Database Setup task complete"
}

function createsuperuser() {
    echo "Please create super user"
    python manage.py createsuperuser
    echo "#############################################################################"
}

function runserver() {
    echo "Running server if everything is okai server will run"
    echo "#############################################################################"
    python manage.py runserver
    echo "#############################################################################"
}

function all_commands() {
    makemigrations
    migrate
    load_initial_data
    createsuperuser
    setup_log
    runserver
}
startProgram