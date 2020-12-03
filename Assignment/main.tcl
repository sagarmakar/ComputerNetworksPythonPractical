set val(chan)   Channel/WirelessChannel    ;# channel type
set val(prop)   Propagation/TwoRayGround   ;# radio-propagation model
set val(netif)  Phy/WirelessPhy            ;# network interface type
set val(mac)    Mac/802_11                 ;# MAC type
set val(ifq)    Queue/DropTail/PriQueue    ;# interface queue type
set val(ll)     LL                         ;# link layer type
set val(ant)    Antenna/OmniAntenna        ;# antenna model
set val(ifqlen) 1000                       ;# max packet in ifq
set val(nn)     30                         ;# number of mobilenodes
set val(rp)     DSR                        ;# routing protocol
set val(x)      500                        ;# X dimension of topography
set val(y)      500                        ;# Y dimension of topography
set val(stop)   100.0                       ;# time of simulation end
set val(new0)   100
set val(new1)   45
set val(new2)   30 

set ns [new Simulator]


set topo       [new Topography]
$topo load_flatgrid $val(x) $val(y)
create-god $val(nn)


set tracingfile [open tracingfile.tr w]
$ns trace-all $tracingfile
$ns use-newtrace


set namfile [open tracingfile.nam w]
$ns namtrace-all $namfile
$ns namtrace-all-wireless $namfile $val(x) $val(y)
set chan [new $val(chan)];#Create wireless channel


$ns node-config -adhocRouting  $val(rp) \
                -llType        $val(ll) \
                -macType       $val(mac) \
                -ifqType       $val(ifq) \
                -ifqLen        $val(ifqlen) \
                -antType       $val(ant) \
                -propType      $val(prop) \
                -phyType       $val(netif) \
                -channel       $chan \
                -topoInstance  $topo \
                -agentTrace    ON \
                -routerTrace   ON \
                -macTrace      ON \
                -movementTrace ON


#for {set i 0} {$i < $val(nn) } { incr i } {
#	set n$i [$ns node]	
#}

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]


$n0 set X_ 200.0
$n0 set Y_ 0.0
$n0 set Z_ 0.0

$n1 set X_ 0.0
$n1 set Y_ 200.0
$n1 set Z_ 0.0

$n2 set X_ 200.0
$n2 set Y_ 200.0
$n2 set Z_ 0.0

#$ns at 10.0 "$n0 setdest 250.0 250.0 3.0"
#$ns at 15.0 "$n1 setdest 45.0 285.0 5.0"
#$ns at 110.0 "$n0 setdest 480.0 300.0 5.0" 

$ns at 0.0 "$n0 setdest 200.0 2.0 0.0"
$ns at 0.0 "$n1 setdest 2.0 200.0 0.0"
$ns at 0.0 "$n2 setdest 200.0 200.0 0.0" 

#for {set i 0} {$i < $val(nn) } { incr i }  {
#	$ns at 0.0 "\$n$i setdest $val(new0) $val(new1) $val(new2)"
#	incr val(new0) 10
#	incr val(new1) 10
#	incr val(new2) 10
#}
  
#Setup a UDP connection
set udp0 [new Agent/UDP]
#$ns attach-agent $n28 $udp0
$ns attach-agent $n0 $udp0
#$n28 color red
$n0 color red
#set null3 [new Agent/Null]
#$ns attach-agent $n18 $null3
#$ns connect $udp0 $null3
$udp0 set packetSize_ 1024


set udp1 [new Agent/UDP]
#$ns attach-agent $n29 $udp1
$ns attach-agent $n1 $udp1
#$n29 color blue
$n1 color blue
set null5 [new Agent/Null]
$ns attach-agent $n2 $null5
$ns connect $udp1 $null5
$udp1 set packetSize_ 1024


#set udp2 [new Agent/UDP]
#$ns attach-agent $n23 $udp2
#$ns attach-agent $n2 $udp2
#$n23 color green
#$n2 color green
#set null4 [new Agent/Null]
#$ns attach-agent $n25 $null4
#$ns connect $udp2 $null4
#$udp2 set packetSize_ 1024


#Setup a CBR Application over UDP connection
set cbr0 [new Application/Traffic/CBR]
$cbr0 attach-agent $udp0
$cbr0 set packetSize_ 120
$cbr0 set rate_ 0.1mb
$cbr0 set random_ null
$ns at 0.0 "$cbr0 start"
$ns at 100.0 "$cbr0 stop"


#set cbr1 [new Application/Traffic/CBR]
#$cbr1 attach-agent $udp2
#$cbr1 set packetSize_ 120
#$cbr1 set rate_ 0.1mb
#$cbr1 set random_ null
#$ns at 0.0 "$cbr1 start"
#$ns at 100.0 "$cbr1 stop"


set cbr2 [new Application/Traffic/CBR]
$cbr2 attach-agent $udp1
$cbr2 set packetSize_ 120
$cbr2 set rate_ 0.1mb
$cbr2 set random_ null
$ns at 0.0 "$cbr2 start"
$ns at 100.0 "$cbr2 stop"


proc finish {} {
    global ns tracingfile namfile
    $ns flush-trace
    close $tracingfile
    close $namfile
    exec nam tracingfile.nam &
    exit 0
}

#for {set i 0} {$i < $val(nn) } { incr i } {
#    $ns at $val(stop) "\$n$i reset"
#}

$ns at val(stop) "$n0 reset"
$ns at val(stop) "$n1 reset"
$ns at val(stop) "$n2 reset"

$ns at $val(stop) "$ns nam-end-wireless $val(stop)"
$ns at $val(stop) "finish"
$ns at $val(stop) "puts \"done\" ; $ns halt"
$ns run