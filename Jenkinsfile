def loginDockerHub(){
    withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'password', usernameVariable: 'username')]) {
        sh "echo $password | docker login -u $username --password-stdin"
    }
}

node {
    stage('Check out'){
        checkout scm
        sh "env | sort"
    }

    stage('Build'){
        sh "docker build -t django:dev ."
    }

    stage('Push to registry'){
        loginDockerHub()
        sh "docker tag django:dev wing0805/taolao:dev"
        sh "docker push wing0805/taolao:dev"
    }
}
