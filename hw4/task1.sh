#task1.sh 

# 找到 infinite.sh 进程并终止
PID=$(ps aux | grep '[i]nfinite.sh' | awk '{print $2}')

if [ -n "$PID" ]; then
    kill -9 $PID
    echo "Process infinite.sh (PID: $PID) has been killed."
else
    echo "No infinite.sh process found."
fi