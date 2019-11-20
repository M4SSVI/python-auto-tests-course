FROM python:3.7

COPY . /python-auto-tests-course 
WORKDIR /python-auto-tests-course


# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

# upgrade pip
RUN pip install --upgrade pip

# install pytest
RUN pip install -U pytest

# install selenium
RUN pip install selenium

#install allure
RUN pip install allure-pytest

#install allure options 
RUN wget https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.0.0/allure-2.0.0.tgz
RUN tar -xf allure-2.0.0.tgz 
RUN rm allure-2.0.0.tgz
ENV PATH="/allure/bin:${PATH}"
ENV ALLURE_CONFIG="/allure-config/allure.properties"

ENTRYPOINT ["/python-auto-tests-course/start.sh"]

CMD allure generate /allure-2.0.0