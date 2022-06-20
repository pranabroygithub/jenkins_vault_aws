pipeline {
    agent any

    stages {
        stage('vault_connection') {
            steps {
                echo 'connection started'
                withVault(configuration: [timeout: 60, vaultCredentialId: '463bca46-0f13-408e-b1ab-7a555bc85a13', vaultUrl: 'http://ec2-54-219-53-11.us-west-1.compute.amazonaws.com:8200'], vaultSecrets: [[path: 'kv/pranab_aws_creds', secretValues: [[vaultKey: 'access_key'], [vaultKey: 'secret_key'], [vaultKey: 'aws_region']]]]) {
                echo 'connection successfull'
                }
            }
            }
        stage('editing file'){
            steps {
                sh 'python3 script.py --access_key $access_key --secret_key $secret_key --aws_region $aws_region'
            }
        }
  
    }
}