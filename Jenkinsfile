pipeline {
    agent any

    stages {
        stage('vault_connection') {
            steps {
                echo 'connection started'
                withVault(configuration: [timeout: 60, vaultCredentialId: '463bca46-0f13-408e-b1ab-7a555bc85a13', vaultUrl: 'http://ec2-54-219-53-11.us-west-1.compute.amazonaws.com:8200'], vaultSecrets: [[path: 'kv/pranab_aws_creds', secretValues: [[envVar: 'ACCESS_KEY', vaultKey: 'access_key'], [envVar: 'SECRET_KEY', vaultKey: 'secret_key'], [envVar: 'AWS_REGION', vaultKey: 'aws_region']]]]) {
                echo 'connection successful'
                sh 'echo $ACCESS_KEY'
                }
            }
            }
        stage('Running python script'){
            steps {
                sh 'echo $ACCESS_KEY'
                //sh 'python3 script.py --access_key $ACCESS_KEY --secret_key $SECRET_KEY --aws_region $AWS_REGION'
            }
        }
  
    }
}