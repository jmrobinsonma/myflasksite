pipeline {
    agent {
        dockerfile { filename 'Dockerfile'}
    }
    stages {
        stage('Checkout') {
            when {
                triggeredBy 'SCMTrigger'
            }
            steps {
                checkout scm
            }
        }
        stage('Test') {
            steps {

                sh 'python3 test.py'
            }
        }
        stage('Push Docker') {
            options {
                skipStagesAfterUnstable()
            }
            steps {

                sh  "docker push jmrobinson/myflasksite"
            }
        }
        post {
            always {
                archiveArtifacts artifacts: 'Dockerfile', fingerprint: true
                }
            }
        }
    }
}
