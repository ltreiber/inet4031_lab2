 #!/bin/bash
              
              a=2
              b=2
              c=$((a + b))
              listOfUsers=(User1 User2 User3)
              echo "Bash says: Hello, World!"
              echo "$a + $b = $c"
	      for i in "${listOfUsers[@]}";
		do
		 echo "$i"
		done
