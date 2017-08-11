# 声明phony target 伪目标
.PHONY: clean

#如果make没有指定target 则默认使用第一个target
all: make_all.txt
	cp make_all.txt make_all.txt.cp

make_all.txt:
	echo 123 > make_all.txt

clean: 
	rm *.txt

