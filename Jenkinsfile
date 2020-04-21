pipeline {
    agent {
        dockerfile { filename 'Dockerfile'}
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup') {
            steps {

                sh """
                python3 -m venv venv &&\
                . venv/bin/activate &&\
                pip install -r requirements.txt
                """
            }
        }
        stage('Test') {
            steps {

                sh 'python3 test.py'
            }
        }
        stage('Deploy') {
            steps {

                sh 'git push https://heroku:$HEROKU_API_KEY@git.heroku.com/$HEROKU_APP_NAME.git master'
            }
        }
    }
}
