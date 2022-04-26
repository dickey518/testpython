pipeline {
    agent any
    stages {
        stage('Hello zhangsan') {
            script{
                if( "${myname}" == "zhangsan" ){
                 echo "hello zhangsan"   
                }else if("${myname}" == "lisi"){
                 echo "hello lisi"   
                }else{
                 echo "hello strangers"   
                }
            }
        }
        stage('get'){
            steps{
                echo 'get something'
            }
            
        }
        stage('just'){
            steps{
                echo 'get just'
            }
            
        }
    }
}
