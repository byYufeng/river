"注释

"基础：语法高亮/搜索高亮/显示行号/显示底部标尺/底部显示文件名
syntax on
set hlsearch
set number
set ruler
set ls=2

"基础：检测文件类型并根据类型自动缩进/使用空格代替tab/shiftwidth自动缩进宽度/tabstop空格数量/删除tab时删除空格数量
filetype indent on
set expandtab
set shiftwidth=4
set tabstop=4
set softtabstop=4

"设置粘贴模式 似乎容易由于冲突而不生效并导致语法缩进异常 此处改为键盘映射更为方便
"set paste
"autocmd InsertEnter * setlocal paste
"autocmd InsertLeave * setlocal nopaste
"
"set smartindent
"set showmatch

" 键盘映射: 快捷键后记得加空格 否则不生效
map <F9> :set nu!<CR>
map <F10> :set paste!<CR>

" 配合bashrc:stty -xion,实现Ctrl-S 保存,Ctrl-x 保存后退出
nmap <C-S> :w!<CR>
vmap <C-S> <C-C>:w!<CR>
imap <C-S> <Esc>:w!<CR>i

nmap <C-X> :wq<CR>
vmap <C-X> <C-C>:wq<CR>
imap <C-X> <Esc>:wq<CR>

"根据缓冲区文件，自动生成模板和更新代码
func SetComment()
    if expand("%:e") == "sh"
        call setline(1, '#!/bin/bash')
        call append(1, '#Author: fsrm')
        call append(2, '')
        call append(3, '')
    endif
    if expand("%:e") == "php"
        call setline(1, '<?php')
        call setline(2, '    #Author: fsrm')
        call setline(3, '     ')
        call setline(4, '?>')
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
        call append(8, 'import sys, os')
        call append(9, 'reload(sys)')
        call append(10, 'sys.setdefaultencoding("utf-8")')
        call append(11, 'sys.path.append(".")')
        call append(12, '')
        call append(13, 'import time, json, traceback')
        call append(14, '')
        call append(15, '')
        call append(16, 'def main():')
        call append(17, '     ')
        call append(18, '')
        call append(19, '')
        call append(20, 'if __name__ == "__main__":')
        call append(21, '    main()')
    endif
endfunc
autocmd BufNewFile *.sh exec ":call SetComment()" | normal 4G
autocmd BufNewFile *.php exec ":call SetComment()" | normal 3G
autocmd BufNewFile *.py exec ":call SetComment()" | normal 18G

"自动维护修改时间
function UpdateTime()
    call cursor(5, 1) 
    if search('Last modify:') != 0
        let line = line('.')
        call setline(line, 'Last modify: ' . strftime('%Y-%m-%d %H:%M:%S'))
    endif
endfunction
":autocmd FileWritePre,BufWritePre *.py ks | call UpdateTime() | 's

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
