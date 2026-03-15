pipeline{
    agent any

    stages{
        stage('Checkout Code'){
            steps{
                echo 'Repository loaded from Github'
            }
        }

        stage('List Files'){
            steps{
                sh 'pwd'
                sh 'ls -la'
                sh 'ls -la app'
            }
        }

        stage ('Install Dependencies'){
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
        stage('Run Lint'){
            steps{
                dir('app'){
                    sh '''
                        . venv/bin/activate
                        pylint main.py || true
                    '''
                }
            }
        }
        stage('SonarQube Analysis'){
            steps{
                script{
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('SonarQube'){
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        stage('OWASP Dependency Check'){
            steps{
                dir('app'){
                    sh '''
                        dependency-check ---scan. ---format HTML --out dependency-check-report || true
                    '''
                }
            }
        }
        stage('Trivy Scan'){
            steps{
                dir('app'){
                    sh '''
                        trivy fs --format table --output trivy-report.txt .
                        '''
                }
            }
        }
        }
    }
}

post{
    always{
        echo 'Pipeline execution finished.'
    }

    success{
        echo 'Pipeline completed successfully.'
    }

    failure{
        echo 'Pipeline failed. Check the console output.'
    }

    always{
        archiveArtifacts artifacts: 'app/dependency-check-report/*, app/trivy-report.txt', fingerprint: true
    }
}