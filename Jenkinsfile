pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building application'
                sh 'python3 --version'
                sh 'python3 -m py_compile app.py test_app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests'
                sh 'python3 -m unittest -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application'
                sh '''
                    mkdir -p deployed
                    cp app.py deployed/app.py
                    python3 deployed/app.py
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully!'
        }
        failure {
            echo 'CI/CD pipeline failed. Check the logs.'
        }
    }
}
