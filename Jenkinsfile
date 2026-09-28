```groovy
pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '''
                    python -m venv venv
                    venv\\Scripts\\python.exe -m pip install --upgrade pip
                    venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                    venv\\Scripts\\python.exe -m py_compile app.py
                '''
            }
        }

    }
}
```
