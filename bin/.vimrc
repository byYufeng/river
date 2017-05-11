"注释
"语法高亮 显示行号和底部标尺
syntax on
set number
set ruler

"底部显示文件名
set ls=2

"检测文件类型并根据类型自动缩进 使用空格代替tab shiftwidth自动缩进宽度 tabstop空格数量 删除tab时删除空格数量
filetype indent on
set expandtab
set sw=4
set ts=4
set sts=4

"新文件自动生成代码模版
autocmd BufNewFile *.* exec ":call SetComment()" | normal 12G
func SetComment()
    if expand("%:e") == 'py'
        call append(0, '#!/usr/bin/env python')
        call append(1, '#coding:utf-8')
        call append(2, "#Created by baiyufeng")
        call append(3, '')
        call append(4, 'import sys')
        call append(5, 'reload(sys)')
        call append(6, 'sys.setdefaultencoding("utf-8")')
        call append(7, '')
        call append(8, 'import os')
        call append(9, '')
        call append(10, 'def main():')
        call append(11, '     ')
        call append(12, '')
        call append(13, 'if __name__ == "__main__":')
        call append(14, '    main()')
    endif
endfunc

