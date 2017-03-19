pipeline {
    agent any

    environment {
      DO_TOKEN = credentials('DigitalOcean API Key')
    }

    parameters {
      choice('REGION', ['nyc1', 'nyc3'], 'Which region to recycle?')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..$REGION'
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
