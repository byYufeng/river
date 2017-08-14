#target: pre-files
#[tab]	commands...
#如果make没有指定target 则默认使用第一个target
#每行command前须有一个tab或者指定的键

# 声明phony target 伪目标: 跳过检查，直接执行命令
.PHONY: clean

all: make_all.txt
	@# 在注释前加上@以取消输出（回声）
	# 注释2
	cp make_all.txt make_all.txt.cp

make_all.txt:
	echo 123 > make_all.txt

clean: 
	rm *.txt

