pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    ./venv/bin/python -m py_compile app.py
                '''
            }
        }

    }
}