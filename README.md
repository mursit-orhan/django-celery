# django-celery

Celery is a convieniet tool to use if we have to do some big works taking long time such as
reporting, Video/Image processing, time consuming ML operations, or Big data sets
Celery.

offload execution of a heavy task to other 
parts of your entire system architecture instead of tackling them on your main thread. 
1.Periodic tasks
2.Third-party tasks — The web app must serve users quickly without waiting for other 
actions to complete while the page loads, e.g., sending an email or notification or propagating updates to internal tools (such as gathering data for A/B testing or system logging).
3. Long-running jobs 
graph generation, Map-Reduce like tasks, and serving of media content (video, audio).

-task/process manager - (Task Queues)
offloading taks execution 
-execute process on demand or periodically 
that way we gain the capabity of having distrubuted workloads
Message Broker:
RabbitMQ/Reddis 
Django send and receive mesasges to Mesasge Broker sends Celery
Django going to generate tasks. task messages passes to RabbitMQ. RabbitMQ delivers messages
accross the application/network. Celery executes tasks 

docker run --rm -it --hostname my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management

localhost:15672 - rabbitmq management site
username guest
password guest

celery -A core worker -l info

RUN rabbitmq-plugins enable --offline rabbitmq_management

flower -A core --port=5555

If you want to run it on Docker execute this:

$ docker run -d -p 6379:6379 redis

