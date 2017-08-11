 #!/bin/bash

 directory2=$PWD/*
 DATE2=`date +%Y-%m-%d:%H`
 if [ ! -d "$PWD/extracted_av" ]; then
 mkdir $PWD/extracted_av
 fi

 #///////////////// TEXT FILE COMBINER /////////////////

 for F3 in $directory2
    do
    F3a=$(echo "$F3" | awk '{print tolower($0)}')
    if [[ $F3a == *"11-"* ]]; then
    if grep -Fxq "$F3a" import_record.txt
        then
        echo " File ${F3a} was already imported"
	rm -rf ${F3a}
	continue
        fi
    
    new_file="pollstore_${DATE2}.csv"
    echo $F3a >> import_record.txt
    cat $F3a | sed '/agentIndex/d' | sed '/^\s*$/d' >> $new_file
    echo "//// $new_file copied to $PWD/extracted_av ////"
    rm -rf $F3a
       fi
    
    done


for F4 in $directory2
    do
    F4a=$(echo "$F4" | awk '{print tolower($0)}')
    if [[ $F4a == *"pollstore"* ]]; then
    new_file2="pollstore2_${DATE2}.csv"
    echo $F4a >> import_record.txt
    cat $F4a | sed '1s/^/agentIndex,pollIndex,time,value,alert,compression\n/' >> $new_file2
    echo "//// $new_file2 copied to $PWD/extracted_av ////"
    rm -rf $F4a
    fi

    done
