https://accounts.builder.ai/users/sign_in

tarunkumar.chinni@mml.local
djc3hS7q

AKIAQQ3JAW5VGJNLT6H3
8is9VTG9hLMF9o+bqTaVwIJ5lY+g4+3o8SG41r+O
https://iihtedu.cloud.builder.ai/prepaid/user/dashboard

tarunkumar.chinni21@mml.local
meN-4iSe
https://iihtedu.cloud.builder.ai/

writexo.com/shyamu

AKIAQQ3JAW5VFVYOXZQS
RxbIG4RpI4c1Qm5PuRWa+gok+Cucr2S2+nIDVenN
AKIAQQ3JAW5VPZRTHXP7
7SS5JyJ++K8gSswawguOU86+xesqpP3ubyCFm76w

  first create new folder

  unzip and import those two maven projects in eclipse

  loggin to aws console

check the region is placed in mumbai.

on aws console 

typy  iam, then  - security credentials - download csv file

  open cmd and type 

  aws configure  

(>aws configure

AWS Access Key ID [None]: AKIAV23OUO3ICXM4EUU7 (from downloaded csv file)

AWS Secret Access Key [None]: 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 (from downloaded csv file)

Default region name [None]: ap-south-1

Default output format [None]: json)

  then in aws console type ecr  then  - create repository tweetAppEcr

copy the URI of our repo

  Go to tweet-api maven project in that DockerFile show in system folder 

  and open it in cmd 

check whether docker is running

in cmd >docker images 

>docker build -t tweetapp-ecs .

output- Successfully built b1af8a339e67

Successfully tagged tweetapp-ecs:latest

>aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin url link from repo(401274599120.dkr.ecr.ap-south-1.amazonaws.com)

output-Login Succeeded

>docker tag tweetapp-ecs:latest 401274599120.dkr.ecr.ap-south-1.amazonaws.com/tweetapp_ecr

output- use command docker images to check your repo is added

>docker push 401274599120.dkr.ecr.ap-south-1.amazonaws.com/tweetapp_ecr

output-pushes

in aws open ecr , click on your repo.

copy image URI

click on Clusters ( top right under Amazon Ecs)

create cluster (OnlyCLuster Namer should give )

Viewcluster-> Go to task definitions  on te top left.

create task definition 

step 1 : Fargate

step 2 : Taskdefintionname,taskrole : none,  task memory(1GB) task CPU (0.5) 

-> Add Container : Container name, image URI,  Hard Limit (1024),  Port Mappings : 8080, 80., add

create

View TaskDefinition -> Clusters : Uner yur cluster -> ttasks ->

run new task  ->Forgate , task definition,cluster VPC (select first one),subnets(select first one), security group : edit (add ports All Tps, All Traffic)

create task, run task 

 refresh till the tasks gets running state ...

open  task copy Public IP 

open post man run ur URLs under ur IP.

post http://ur ip(13.235.80.203):8682/api/v1.0/tweets/register

{ 

"username": "test@gmail.com",

"firstName": "test",

"lastName": "test",

"email": "test@gmail.com",

"contactNum": "9876543210",

"password": "123456"

}

get http://3.6.43.149:8682/api/v1.0/tweets/user/search/cherry@gmail.com





  http://13.235.80.203:8682/api/v1.0/tweets/register



http://52.66.234.205:8682/api/v1.0/tweets/register



  http://localhost:8682/api/v1.0/tweets/register



  http://localhost:8682/api/v1.0/tweets/all



  http://localhost:8682/api/v1.0/tweets/{​​​​​​​​test0@gmail.com}​​​​​​​​/add



{

  "username" : "test0@gmail.com",

  "tweetText" : "meee" ,

  "firstName" : "Deepthi",

  "lastName" : "SriSai",

  "tweetDate" : "20-05-2021"

}





  http://13.235.80.203:8682/api/v1.0/tweets/user/search/deeps@gmail.com



http://13.235.80.203:8682/api/v1.0/tweets/deeps@gmail.com/add



{

  "username" : "test0@gmail.com",

  "tweetText" : "meee" ,

  "firstName" : "Deepthi",

  "lastName" : "SriSai",

  "tweetDate" : "20-05-2021"

}





  http://13.235.80.203:8682/api/v1.0/tweets/register









https://accounts.builder.ai/users/sign_in 
