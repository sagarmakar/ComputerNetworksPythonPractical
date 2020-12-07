BEGIN {
	PacketRcvdr=0;
	split("", Pcktr);
	Throughputr=0.0;
	split("", thr);
	pr=0;
	split("", rad);
	radius=0;

}

{
	if(($1 == "r") && ($5 == "2")){
		PacketRcvdr++;
		Pcktr[pr]= PacketRcvdr;
		Throughputr=((PacketRcvdr*1000*8)/(95.0*1000000));
		thr[pr]= Throughputr;
		pr++;
}
	if(($1 == "r") && ($5 == "2")){
		pr=0;
		radius = (($11)^2 + ($13)^2 + ($15)^2)^(1/3);
		rad[pr]=radius;
		pr++;
}

}
END {
print("TitleText: Throughout vs Radius")
for ( i=0; i< length(Pcktr); i++){
	printf("%f %f\n",rad[i], Pcktr[i]) ;
}
}