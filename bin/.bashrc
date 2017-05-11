# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific aliases and functions
alias rm='trash'
trash()
{
    # I quote this path last time and suffers a lot...
    if [ ! -d ~/.trash ]; then
        mkdir ~/.trash
    fi
    mv $@ ~/.trash
}
