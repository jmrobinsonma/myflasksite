node {
    stage('SCM Checkout'){
        git 'git@github.com:jmrobinsonma/myflasksite.git'
    }
    stage('Test'){
        sh 'python3 test.py'
    }
    stage('Docker build'){
        sh 'docker build -t jmrobinson/site-testpipe .'
    }
    stage('Push Docker image'){
        withCredentials([string(credentialsId: 'dockerpass', variable: 'DOCKERPWD')]) {
            sh "docker login -u jmrobinson -p ${DOCKERPWD}"
        }
        sh 'docker push jmrobinson/site-testpipe'
    }
}
