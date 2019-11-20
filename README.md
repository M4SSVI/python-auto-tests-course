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
docker run \
-v $PWD/allure-report:/allure-report \
-v $PWD/allure-results:/python-auto-tests-course/allure-results \
test  allure report generate -o /allure-report


