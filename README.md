# python-auto-tests-course
Репозиторий для заданий курса автоматизация тестирования с помощью Selenium и Python.

# Для локального запуска

mkdir env

cd env

python3 -m venv selenium_env

source selenium_env/bin/activate

pip install -U pytest

pip install -U selenium

pip install allure-pytest

pytest ./python-auto-tests-course/tests/test_1.py -v --alluredir=allure-results


# Для сборки Docker образа

docker image build -t python-auto-tests-course .


# Запуск контейнера 

generate json 
docker run -v $PWD/allure-results:/python-auto-tests-course/allure-results python-auto-tests-course 

generate report
allure serve ./allure-results && allure report open -o /allure-results -p 5000 & \
    /usr/bin/open -a "/Applications/Google Chrome.app" 'http://127.0.0.1:5000'


