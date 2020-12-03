BEGIN {
PacketRcvd=0;
Throughput=0.0;
}
{
if(($1=="r"))
{
PacketRcvd++;
Throughput=((PacketRcvd*1000*8)/(95.0*1000000));
printf("%f %f", PacketRcvd, Throughput);
}
}
END {
}