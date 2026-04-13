pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Repository loaded from GitHub'
            }
        }

        stage('List Files') {
            steps {
                sh 'pwd'
                sh 'ls -la'
                sh 'ls -la app'
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('app') {
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

        stage('Run Tests') {
            steps {
                dir('app') {
                    sh '''
                        . venv/bin/activate
                        pytest test_main.py
                    '''
                }
            }
        }

        stage('Run Lint') {
            steps {
                dir('app') {
                    sh '''
                        . venv/bin/activate
                        pylint main.py || true
                    '''
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('OWASP Dependency Check') {
            steps {
                script {
                    def dcHome = tool 'DependencyCheck'

                    dir('app') {
                        sh """
                            mkdir -p ../reports
                            ${dcHome}/bin/dependency-check.sh \
                            --scan . \
                            --format JSON \
                            --out ../reports \
                            --disableAssembly
                        """
                    }
                }
            }
        }

        stage('Trivy Scan') {
            steps {
                dir('app') {
                    sh '''
                        mkdir -p ../reports
                        trivy fs --format json --output ../reports/trivy-report.json .
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: false
                }
            }
        }

        stage('Generate Dashboad Summary') {
            steps {
                sh '''
                python scripts/generate_summary.py
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*, gui/data/summary.json', fingerprint: true
            echo 'Pipeline execution finished.'
        }

        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
