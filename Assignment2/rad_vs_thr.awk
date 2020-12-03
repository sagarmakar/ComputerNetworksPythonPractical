BEGIN {
PacketRcvd=0;
Throughput=0.0;
}
{
if(($1=="r"))
{
PacketRcvd++;
Throughput=((PacketRcvd*1000*8)/(95.0*1000000));
radius = (($11)^2 + ($13)^2 + ($15)^2)^(1/3)
printf("%f %f", radius , Throughput);
}
}
END {
}