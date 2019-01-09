** consuer:
* consumer分为assign和substribe两种模式。若指定topics，默认为substribe模式。
* 每条消息只能被每个group内的多个consumer累计消费一次。可以被多个group共同消费
* 新加入的group自动处于最末偏移
* 使用for迭代的时候会在消费后自动提交偏移。poll时则不会
* 可以使用seek/seek_to_begining/seek_to_end手动更改起始偏移位置（若seek_to_begining/seek_to_end不指定分区，则会移动到assign的每个分区）
* poll时要指定第一个参数(time_out)，100左右即可。否则会立即返回，通常为空集。


** producer:
* producer是进程安全的。多个进程可以共享一个实例，并且速度会比多实例更快
* send消息后默认会等待一定时间或者字节的缓冲。可以调用flush()方法立即刷新
* ack 0:完全不确认，信息可能会丢失 1:保证写入主节点（但不保证有备份） all:等待完整的主备写入（保证不会丢失） 默认为1
* 可以指定key并映射到指定分区。(比如可以用日期等当key，之后可以方便的回溯处理。个人觉得这是最棒的一点)
* 可以在header中用tuple_list装载额外信息。（但是感觉还不如直接用一个dict）

? linger_ms的默认值为0，似乎还是不能立即发送到。要通过flush。
? 可以只指定key而不指定value。文档中说是视为'delete' 是指什么意思？ 是忽略掉？还是删掉旧文件 还是什么？

** process:
N台机器(N=3) partition数量默认可以设为(预估消费者数量M) [M/N]*N  ==> M=6or9

方案1：
    每种任务一个topic，以日期为key，写到指定partition中
    #行不通。无法中partition定位到具体某天的数据，且不方便并行消费
方案2：
    每种任务_每天一个topic。不需要指定key。随机分发到partition里
producer.send(topic, msg) --> partition
consumer --> 
