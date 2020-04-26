pipeline {
    agent none
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
        post {
            always {
                archiveArtifacts "testing.Dockerfile"
                }
                }
                }
    stage('Deliver') {
        agent {
            dockerfile {
                filename 'Dockerfile'
                }
                }
        steps {
            sh "docker push jmrobinson/myflasksite"
                }
                }
        post {
            success {
                archiveArtifacts "Dockerfile"
                }
                }
                }
                }

