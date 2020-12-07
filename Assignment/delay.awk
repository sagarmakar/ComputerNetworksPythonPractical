BEGIN {
}
{
	# finding sending-time from respective trace file
	if($1 == "s") {
		sent_time = $3;
	}  #if ends

	else if($1 == "r") {
		receive_time= $3;
        end_to_end_delay = receive_time - sent_time;
        print receive_time " " end_to_end_delay;
	} #elseif ends
}
END {
}