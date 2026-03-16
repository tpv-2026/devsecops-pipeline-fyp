pipeline {
    agent any

    stages{
        stage{'Checkout code'}{
            steps{
                echo 'Repository loaded from GitHub'
            }
        }

        stage{'List Files'}{
            steps{
                sh 'pwd'
                sh 'ls -la'
                sh ' ls -la app'
            }
        }

        stage{'Install Dependencies'}{
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
                        pytest test main.py
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

        stage{'SonarQube Analysis'}{
            steps{
                script{
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('SonarQube'){
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('OWASP Dependency Check'){
            steps{
                dir('app'){
                    sh '''
                        mkdir -p dependency-check-report#
                        echo "OWASP Dependency Check placeholder report" > dependency-check-report/report.txt
                    '''
                }
            }
        }

        stage('Trivy Scan'){
            steps{
                dir('app'){
                    sh '''
                        echo "Trivy placeholder scan report" > trivy-report.txt
                    '''
                }
            }
        }
    }

    post{
        always{
            archiveArtifacts artifacts: 'app/dependency-check-report/*, app/trivy-report.txt', fingerprint: true
        }

        success{
            echo 'Pipeline completed successfully.'
        }

        failure{
            echo 'Pipeline failed. Check the console output.'
        }
    }
}