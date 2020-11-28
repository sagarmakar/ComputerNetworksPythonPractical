BEGIN {
    st1["Initialize"]=0;
    rc1["Initialize"] = 0;
    st2["Initialize"]=0;
    rc2["Initialize"] = 0;
    st3["Initialize"]=0;
    rc3["Initialize"] = 0;
    st4["Initialize"]=0;
    rc4["Initialize"] = 0;
    
    c1=0;
    c2=0;
    c3=0;
    c4=0;
    
    total1=0;
    total2=0;
    total3=0;
    total4=0;
    
    avg_delay1=0;
    avg_delay2=0;
    avg_delay3=0;
    avg_delay4=0;
}
{
    action = $1;
    time = $2;
    from = $3;
    to = $4;
    type = $5;
    pktsize = $6;
    fid = $8;
    src = $9;
    dst = $10;
    seq_no = $11;
    packet_id = $12;
    
    if (action=="+" && (type=="cbr" || type=="tcp")){
    	if((from==1&&to==0)||(from==5&&to==4)||(from==11&&to==10)||(from==14&&to==13)||(from==1&&to==2)||(from==14&&to==10)){
    		if(fid==1)
        		sent_times1[packet_id]=time;
        	else if(fid==2)
        		sent_times2[packet_id]=time;
        	else if(fid==3)
        		sent_times3[packet_id]=time;
        	else if(fid==4)
        		sent_times4[packet_id]=time;
    }
    }
    if (action=="r"&& (type=="cbr" || type=="tcp")){
    	if ((from==4&&to==7)||(from==3 && to==0)||(from==1 && to==0)||(from==13 && to==12)||(from==11 && to==12)){
    		if(fid==1)
        		rc1[packet_id]=time;
        	else if(fid==2)
        		rc2[packet_id]=time;
        	else if(fid==3)
        		rc3[packet_id]=time;
        	else if(fid==4)
        		rc4[packet_id]=time;
    	}
    }
}
END{
    for (x in rc1){
    	total1+=rc1[x]-st1[x];
    	c1++;
    }
    for (x in rc2){
    	total2+=rc2[x]-st2[x];
    	c2++;
    }
    for (x in rc3){
    	total3+=rc3[x]-st3[x];
    	c3++;
    }
    for (x in rc4){
    	total4+=rc4[x]-st4[x];
    	c4++;
    }
    avg_delay1=total1/c1;
    avg_delay2=total2/c2;
    avg_delay3=total3/c3;
    avg_delay4=total4/c4;
    printf("%f %f \n%f %f \n%f %f\n%f %f\n ",avg_delay1, c1 ,avg_delay2, c2,avg_delay3, c3,avg_delay4, c4);
}
