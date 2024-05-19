#Importing base image Ubuntu
FROM ubuntu:latest

#Updating and Upgrading Ubuntu
RUN apt -y update \
&& apt -y upgrade

#Clear cache
RUN apt clean

#Jenkins Prerequisites
RUN  apt search openjdk

#Install Java version 11 as prerequisite
RUN apt -y install openjdk-11-jdk wget default-jre-headless

RUN wget https://github.com/allure-framework/allure2/releases/download/2.27.0/allure_2.27.0-1_all.deb &&\
    dpkg -i allure_2.27.0-1_all.deb &&\
    rm -fr allure_2.27.0-1_all.deb

#Jenkins installation
#Download & add repository key
RUN wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key

#Getting binary file into /etc/apt/sources.list.d
RUN echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
https://pkg.jenkins.io/debian-stable binary/ | tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

# Install Selenium and Selenium Wire dependencies
RUN apt update && \
    apt install -y python3-pip curl && \
    pip3 install selenium selenium-wire behave python-dotenv allure-behave webdriver-manager

# Install Chrome and Chromedriver for Selenium tests
RUN apt install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm ./google-chrome-stable_current_amd64.deb && \
    wget -N http://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/local/bin/ && \
    rm chromedriver_linux64.zip && \
    chmod +x /usr/local/bin/chromedriver &&\
    ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

#Updating packages
RUN  apt update
#Installing Jenkins
RUN  apt -y install jenkins

#Expose port 8080
EXPOSE 8080

ENTRYPOINT /etc/init.d/jenkins start && tail -f /var/log/jenkins/jenkins.log
