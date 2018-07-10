-  start
    - python官方库使用pika

    - 链接https://www.rabbitmq.com/tutorials/tutorial-one-python.html
- work queue

    - 每个consumer轮流获取消息（round-robin算法）
    - 不能redefine一个queue（比如增加durable属性）
    - channel.basic_consume.no_ack | channel.basic_consume.callback.basic_ack：consumer处理完消息后是否发送回应以通知rabbitmq安全删除，保证即使没处理完的时候worker die掉消息也不丢失
    - queue_declare.durable & channel.basic_publish.dilivery_mode : 分别持久化queue和message，保证rabbitmq die掉消息也不丢失
    - channel.basic_qos.prefetch_count=1 使每个consumer 处理和发送ack回应前不接受新的消息（每次只处理一条）
    - *TTL
-  publish/subscribe
    - rabbitmq实际模型：producer-exchange-queue-[consumer1, consumer2...]
    - queue_name  = channel.queue_declare(exclusive=True) 随机生成一个queue名并在consumer退出时删除

    - 在consumer中把queue binding在 exchange上
- routing
    - fanout-exchange会ignore掉binding key
    - direct-exchange可以binding多个key
- topics
    - 发消息的时候producer指定exchange。每个consumer建一个queue，绑定好routing_keys之后即可。
        -一个exchange可以绑定多个queue，一个queue可以绑定多个routing_key规则。每个queue独立平行消费
    - topic-exchange的binding key由word.word.word...形式组成。其中word可以是两种通配符： * 代表 恰好一个词， #(hash) 代表没有或多个词
    - topic的binding key 为"#"时，表现为"fanout"；为"*"时，表现为"direct"
- rpc
    - 其实就是建立两个queue:call和callback。client携带一个uuid publish请求到server监听的call_queue，server处理后publish到client监听的callback_queue。client持续获取消息，验证uuid后拿到结果

- 总结
    - 在声明queue时设置duable=True即可实现消息的存储（produce时consumer不必在线）
    - exchange 共有fanout direct topic 三种模式,一切通信都是直接从queue中、或间接的通过exchange-queue的途径获取消息
    - 这个rpc会锁定queue，所以不支持并发。。。怎么解决后续再研究吧
    - 官网拉的这个镜像把所有端口都映射了也没法在容器外访问。。。很烦 只能把代码目录挂载进去然后用个python容器link到rabbitmq容器再运行代码。后续再看看怎么解决把。更烦了。。。
        --已解决 原来是host没写对 写成镜像的名称了 改成localhost就好 妈的 真是智障 
