ps -ef | grep postgresql | grep -v grep
[ $?  -eq "0" ] && echo "PostgreSQL check!" || echo "process is not running"
