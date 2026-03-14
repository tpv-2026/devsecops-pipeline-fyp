pipeline {
    agent any

    stages{
        stage('Checkout Code'){
            steps{
                echo 'Repository loaded from GitHub'
            }
        }
        stage('List Files'){
            steps{
                sh 'pwd'
                sh 'ls -la'
                sh 'ls -la app'
            }
        }

        stage('Install Dependencies'){
            steps{
                dir('app'){
                    sh '''
                        python3 --version
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests'){
            steps{
                dir('app'){
                    sh '''
                        . venv/bin/activate
                        pytest test_main.py
                    '''
                }
            }
        }
    }
}