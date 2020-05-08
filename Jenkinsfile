pipeline {
    agent { dockerfile true }
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Test') {
            agent {
                dockerfile {
                    filename 'testing.Dockerfile'
            }
        }
            steps {
                sh "python3 test.py"
            }
        }
        stage('Deliver') {
            agent {
                dockerfile {
                    filename 'Dockerfile'
                }
            }
            steps {
                sh "docker push jmrobinson/site-testpipe"
            }
        }
    }
}
