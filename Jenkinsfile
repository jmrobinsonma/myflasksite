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
    }
}
