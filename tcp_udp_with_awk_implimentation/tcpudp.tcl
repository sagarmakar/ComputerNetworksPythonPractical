set ns [new Simulator]


$ns color 1 Red
$ns color 2 Blue
$ns color 3 Green
$ns color 4 Purple
$ns color 5 Yellow

set nf [open out.nam w]
set tracefile [open out.tr w]
$ns namtrace-all $nf
$ns trace-all $tracefile
$ns rtproto DV

proc finish {} {
        global ns nf
        $ns flush-trace
        close $nf
        exec awk -f throughput.awk out.tr > throughput.xg &
        exec awk -f packetsdropped.awk out.tr > packetsdropped.xg &
        exec awk -f Avg_delay.awk out.tr > Avg_delay.xg &
        exit 0
        exec xgraph throughput.xg &
        exec xgraph packetsdropped.xg &
        exec xgraph Avg_delay.xg &

}






set n 20
for { set i 0 } { $i < $n} { incr i } {
    set nod($i) [$ns node]
}
#setting the connections
for { set i 0 } { $i < $n} { incr i } {
    if {$i < [expr $n/2] } {
        $ns duplex-link $nod($i) $nod([expr ($i+1)%[expr $n/2]]) 2Mb 10ms DropTail
    } else {
        $ns duplex-link $nod([expr $i-1 ]) $nod($i) 2Mb 10ms DropTail 
        for { set j [expr $n/2] } {$j < $n } {incr j} {
            if { $i != $j } {
                $ns duplex-link $nod($i) $nod($j) 2Mb 10ms DropTail 
            } 
        }
    }
}
#a few extra ones
$ns duplex-link $nod(0) $nod([expr $n/2]) 2Mb 10ms DropTail
$ns duplex-link $nod(9) $nod(15) 2Mb 10ms DropTail

set udp [new Agent/UDP]
$ns attach-agent $nod(0) $udp
set cbr [new Application/Traffic/CBR]
$cbr set packetSize_ 500
$cbr set interval_ 0.005
$cbr attach-agent $udp
set null [new Agent/Null]
$ns attach-agent $nod(15) $null
$ns connect $udp $null

set udp1 [new Agent/UDP]
$ns attach-agent $nod(9) $udp1
set cbr1 [new Application/Traffic/CBR]
$cbr1 set packetSize_ 500
$cbr1 set interval_ 0.005
$cbr1 attach-agent $udp1
set null1 [new Agent/Null]
$ns attach-agent $nod(18) $null1
$ns connect $udp1 $null1

set tcp [new Agent/TCP]
$ns attach-agent $nod(2) $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $nod(19) $sink
$ns connect $tcp $sink

set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP

set tcp1 [new Agent/TCP]
$ns attach-agent $nod(2) $tcp1
set sink1 [new Agent/TCPSink]
$ns attach-agent $nod(16) $sink1
$ns connect $tcp1 $sink1

set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp1
$ftp1 set type_ FTP

$udp set fid_ 1
$udp1 set fid_ 2
$tcp set fid_ 3
$tcp1 set fid_ 4

$ns at 0.25 "$cbr start"
$ns at 0.35 "$cbr1 start"
$ns at 0.45 "$ftp start"
$ns at 0.55 "$ftp1 start"

$ns rtmodel-at 1.0 down $nod(0) $nod(10)
$ns rtmodel-at 2.5 up $nod(0) $nod(10)

$ns rtmodel-at 1.0 down $nod(0) $nod(1)
$ns rtmodel-at 2.5 up $nod(0) $nod(1)

$ns rtmodel-at 1.0 down $nod(10) $nod(15)
$ns rtmodel-at 2.5 up $nod(10) $nod(15)

$ns rtmodel-at 1.0 down $nod(2) $nod(3)
$ns rtmodel-at 2.5 up $nod(2) $nod(3)

$ns rtmodel-at 1.0 down $nod(11) $nod(12)
$ns rtmodel-at 2.5 up $nod(11) $nod(12)

$ns at 5.25 "$cbr stop"
$ns at 5.35 "$cbr1 stop"
$ns at 5.45 "$ftp stop"
$ns at 5.55 "$ftp1 stop"
$ns at 6.0 "finish"

$ns run 
