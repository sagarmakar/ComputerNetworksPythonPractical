set val(chan)   Channel/WirelessChannel    ;# channel type
set val(prop)   Propagation/TwoRayGround   ;# radio-propagation model
set val(netif)  Phy/WirelessPhy            ;# network interface type
set val(mac)    Mac/802_11                 ;# MAC type
set val(ifq)    Queue/DropTail/PriQueue    ;# interface queue type
set val(ll)     LL                         ;# link layer type
set val(ant)    Antenna/OmniAntenna        ;# antenna model
set val(ifqlen) 1000                       ;# max packet in ifq
set val(nn)     21                         ;# number of mobilenodes
set val(rp)     DSR                        ;# routing protocol
set val(x)      500                        ;# X dimension of topography
set val(y)      500                        ;# Y dimension of topography
set val(stop)   100.0                       ;# time of simulation end
set val(new0)   60
set val(new1)   60
set val(new2)   60

set ns [new Simulator]


set topo       [new Topography]
$topo load_flatgrid $val(x) $val(y)
create-god $val(nn)


set tracingfile [open tracingfile.tr w]
$ns trace-all $tracingfile
$ns use-newtrace

create-god $val(nn)


set namfile [open tracingfile.nam w]
$ns namtrace-all $namfile
$ns namtrace-all-wireless $namfile $val(x) $val(y)
set chan [new $val(chan)];


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


for {set i 0} {$i < $val(nn) } { incr i } {
	set n$i [$ns node]	
}

$n0 set X_ 95.0
$n0 set Y_ 50.0
$n0 set Z_ 0.0

$n1 set X_ 60.0
$n1 set Y_ 50.0
$n1 set Z_ 0.0

$n2 set X_ 25.0
$n2 set Y_ 190.0
$n2 set Z_ 0.0



$n3 set X_ 135.0
$n3 set Y_ 155.0
$n3 set Z_ 0.0



$n4 set X_ 105.0
$n4 set Y_ 180.0
$n4 set Z_ 0.0


$n5 set X_ 110.0
$n5 set Y_ 200.0
$n5 set Z_ 0.0


$n6 set X_ 55.0
$n6 set Y_ 75.0
$n6 set Z_ 0.0


$n7 set X_ 1.0
$n7 set Y_ 20.0
$n7 set Z_ 0.0

$n8 set X_ 175.0
$n8 set Y_ 90.0
$n8 set Z_ 0.0

$n9 set X_ 115.0
$n9 set Y_ 115.0
$n9 set Z_ 0.0

$n10 set X_ 75.0
$n10 set Y_ 175.0
$n10 set Z_ 0.0

$n11 set X_ 150.0
$n11 set Y_ 135.0
$n11 set Z_ 0.0

$n12 set X_ 45.0
$n12 set Y_ 90.0
$n12 set Z_ 0.0

$n13 set X_ 10.0
$n13 set Y_ 45.0
$n13 set Z_ 0.0

$n14 set X_ 90.0
$n14 set Y_ 1.0
$n14 set Z_ 0.0

$n15 set X_ 110.0
$n15 set Y_ 100.0
$n15 set Z_ 0.0

$n16 set X_ 160.0
$n16 set Y_ 120.0
$n16 set Z_ 0.0

$n17 set X_ 180.0
$n17 set Y_ 20.0
$n17 set Z_ 0.0

$n18 set X_ 120.0
$n18 set Y_ 10.0
$n18 set Z_ 0.0

$n19 set X_ 190.0
$n19 set Y_ 1.0
$n19 set Z_ 0.0

$n20 set X_ 150.0
$n20 set Y_ 135.0
$n20 set Z_ 0.0


for {set i 0} {$i < $val(nn) } { incr i }  {
	$ns at 0.0 "\$n$i setdest $val(new0) $val(new1) $val(new2)"
	incr val(new0) 12
	incr val(new1) 12
	incr val(new2) 0
}
  
set udp0 [new Agent/UDP]
$ns attach-agent $n18 $udp0
$ns attach-agent $n0 $udp0
$n18 color red
$n0 color red
set null3 [new Agent/Null]
$ns attach-agent $n8 $null3
$ns connect $udp0 $null3
$udp0 set packetSize_ 180


set udp1 [new Agent/UDP]
$ns attach-agent $n19 $udp1
$ns attach-agent $n1 $udp1
$n19 color blue
$n1 color blue
set null5 [new Agent/Null]
$ns attach-agent $n2 $null5
$ns connect $udp1 $null5
$udp1 set packetSize_ 180


set udp2 [new Agent/UDP]
$ns attach-agent $n13 $udp2
$ns attach-agent $n2 $udp2
$n13 color green
$n2 color green
set null4 [new Agent/Null]
$ns attach-agent $n15 $null4
$ns connect $udp2 $null4
$udp2 set packetSize_ 180


set cbr0 [new Application/Traffic/CBR]
$cbr0 attach-agent $udp0
$cbr0 set packetSize_ 120
$cbr0 set rate_ 0.1mb
$cbr0 set random_ null
$ns at 0.0 "$cbr0 start"
$ns at 100.0 "$cbr0 stop"


set cbr1 [new Application/Traffic/CBR]
$cbr1 attach-agent $udp2
$cbr1 set packetSize_ 120
$cbr1 set rate_ 0.1mb
$cbr1 set random_ null
$ns at 0.0 "$cbr1 start"
$ns at 100.0 "$cbr1 stop"


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

for {set i 0} {$i < $val(nn) } { incr i } {
    $ns at $val(stop) "\$n$i reset"
}

$ns at $val(stop) "$ns nam-end-wireless $val(stop)"
$ns at $val(stop) "finish"
$ns at $val(stop) "puts \"done\" ; $ns halt"
$ns run