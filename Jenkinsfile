
pipeline {
    agent any

    stages {
        stage('Build image') {
            steps {
                sh 'docker build -t jenkins:v1 .'
            }
        }

        stage('Remove old container') {
            steps {
                sh 'docker rm -f jenkinsfsh || true'
            }
        }

        stage('Run new container') {
            steps {
                sh 'docker run -d --name=jenkinsfsh --restart unless-stopped -p 1235:5000 jenkins:v1'
            }
        }
    }
}
