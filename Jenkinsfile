pipeline {
    agent any

    environment {
      DO_TOKEN = credentials('DigitalOcean API Key')
    }

    parameters {
      choice(choices: 'nyc1\nnyc3', description: 'Which region to recycle?', name: 'region')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..${params.REGION}'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
