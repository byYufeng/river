"注释

"语法高亮 搜索高亮 显示行号和底部标尺 底部显示文件名
syntax on
set hlsearch
set number
set ruler
set ls=2

"粘贴模式
set paste
autocmd InsertEnter * setlocal paste
autocmd InsertLeave * setlocal nopaste

"检测文件类型并根据类型自动缩进 使用空格代替tab shiftwidth自动缩进宽度 tabstop空格数量 删除tab时删除空格数量
filetype indent on
set expandtab
set sw=4
set ts=4
set sts=4


"根据缓冲区文件，自动生成模板和更新代码
func SetComment()
    if expand("%:e") == "sh"
        call setline(1, '#!/bin/bash')
        call append(1, '#Author: fsrm')
        call append(2, '')
        call append(3, '')
    endif
    if expand("%:e") == "py"
        call setline(1, '#!/usr/bin/env python')
        call append(1, '#coding:utf-8')
        call append(2, '"""')
        call append(3, 'Author: fsrm')
        call append(4, 'Create Time: ' . strftime('%Y-%m-%d %H:%M:%S'))
        call append(5, 'Last modify: ' . strftime('%Y-%m-%d %H:%M:%S'))
        call append(6, '"""')
        call append(7, '')
        call append(8, 'import sys')
        call append(9, 'reload(sys)')
        call append(10, 'sys.setdefaultencoding("utf-8")')
        call append(11, '')
        call append(12, 'import os, time')
        call append(13, 'import traceback, json')
        call append(14, '')
        call append(15, 'def main():')
        call append(16, '     ')
        call append(17, '')
        call append(18, 'if __name__ == "__main__":')
        call append(19, '    main()')
    endif
endfunc
autocmd BufNewFile *.sh exec ":call SetComment()" | normal 4G
autocmd BufNewFile *.py exec ":call SetComment()" | normal 17G

"自动维护修改时间
function UpdateTime()
    call cursor(5, 1) 
    if search('Last modify:') != 0
        let line = line('.')
        call setline(line, 'Last modify: ' . strftime('%Y-%m-%d %H:%M:%S'))
    endif
endfunction
:autocmd FileWritePre,BufWritePre *.py ks | call UpdateTime() | 's

"F5运行python脚本
map <F5> :w<CR> : call RunPython()<CR>
function RunPython()
      let mp = &makeprg
      let ef = &errorformat
      let exeFile = expand("%:t")
      setlocal makeprg=python\ -u
      set efm=%C\ %.%#,%A\ \ File\ \"%f\"\\,\ line\ %l%.%#,%Z%[%^\ ]%\\@=%m
      silent make %
      copen
      let &makeprg = mp
      let &errorformat = ef
endfunction

" 当光标一段时间保持不动了，就禁用高亮
autocmd cursorhold * set nohlsearch
" 当输入查找命令时，再启用高亮
noremap n :set hlsearch<cr>n
noremap N :set hlsearch<cr>N
noremap / :set hlsearch<cr>/
noremap ? :set hlsearch<cr>?
noremap * *:set hlsearch<cr>