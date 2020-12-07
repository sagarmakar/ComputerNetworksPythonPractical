BEGIN {
	PacketRcvdr=0;
	split("", Pcktr);
	Throughputr=0.0;
	split("", thr);
	pr=0;

}
{
	if(($35 == "cbr") && ($1 == "r") && ($19=="RTR") && ($5 == "2")){
		PacketRcvdr++;
		Pcktr[pr]= PacketRcvdr;
		Throughputr=((PacketRcvdr*1000*8)/(95.0*1000000));
		thr[pr]= Throughputr;
		pr++;
}
}

END {
print("TitleText: Throughout vs Packets Received")
for ( i=0; i< length(Pcktr); i++){
	printf("%f %f\n",thr[i], Pcktr[i]) ;
}
}