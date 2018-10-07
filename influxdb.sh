cd /sys/class/net/enp4s0/statistics
out=$(echo "STATUS" | nc 10.83.186.72 1234)
/srv/graphana.py --rx $(cat rx_bytes) --tx $(cat tx_bytes) --mp $(echo $out | cut -d# -f2) --ps $(echo $out | cut -d# -f3) --con $(echo $out | cut -d# -f1)