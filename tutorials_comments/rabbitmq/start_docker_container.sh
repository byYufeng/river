#sudo docker run -d --name rabbit -p 5672:5672 -p 4369:4369 -p 5671:5671 -p 15671:15671 -p 15672:15672 -p 25672:25672 rabbitmq:3-management
sudo docker run --name rabbit -d -p 5672:5672 -p 15672:15672 rabbitmq:management
