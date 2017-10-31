#! /usr/bin/awk -f
#This a nice exemple of how to use awk for bioinformatics
#This code get a table with transcription expression from Kallisto and summarize it to gene level

BEGIN{
  OFS="\t"
}
{
  if(NR==1){
    print $0
  }else{
      cnt1[$9]+=$3;cnt2[$9]+=$4;cnt3[$9]+=$5;cnt4[$9]+=$6;cnt5[$9]+=$7;cnt6[$9]+=$8;gene_name[$9]=$10
  }
}
END{
  for (x in cnt1){
    print x"\t"gene_name[x]"\t"cnt1[x]"\t"cnt2[x]"\t"cnt3[x]"\t"cnt4[x]"\t"cnt5[x]"\t"cnt6[x]
  }
}
