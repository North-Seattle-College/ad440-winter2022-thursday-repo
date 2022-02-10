# !/bin/sh
# Ask user for the input
USER_INPUT="Please enter initials of your first and last name (or 'e' to exit)"
NUM=2

while :
  do
    # get and validate user initials
    printf "%s\n" "$USER_INPUT" 
    while read input && [ "$input" != "e" ];
      do
        # Validates the input is null or is of 0 length
        if [ -z "$input" ]; then
          printf '%s\n' "Error: initials can't be empty" 
        # checks to see if the string matches the requested pattern
        #elif [[ "${input}" =~ [^a-zA-Z] ]]; then
          #printf '%s\n' "Error: initials must only contain letters, a-z"
        elif [[ "${#input}" != $NUM ]]; then
          printf '%s\n' "Error: initials must be $NUM characters"
        else
          break
        fi
          printf "%s\n" "$USER_INPUT" 
      done

    if [ "$input" == "e" ]; then
      printf '%s\n' "Done"
      break
    fi

    # Removes spaces ifany and change to lower
    formattedInitials="$(echo "${input}" | tr -d '[:space:]' | tr '[:upper:]' '[:lower:]')"
    uniqueName=$formattedInitials
    stackName=$uniqueName-stack

    printf "%s\n" "Your stack will be named as follows:" \
            "stack: $stackName" \
            "Create lambda function and stack? (y/n)" 

     #Importing the lamda template to create the function
    lambdaTemplate="./CloudFormationLambdaTemplate.json"
    while read userResponse && [ "$userResponse" != "e" ];
      do
        if [ "$userResponse" == "y" ]; then
          printf '%s\n' "aws cloudformation deploy --template-file $lambdaTemplate --stack-name $stackName --capabilities CAPABILITY_NAMED_IAM"
          aws cloudformation deploy --template-file $lambdaTemplate --stack-name $stackName --capabilities CAPABILITY_NAMED_IAM
          break
        elif [ "$userResponse" == "n" ]; then
          break
        else
          printf "%s\n" "Create lambda? (y/n)"
        fi
      done
    printf '%s\n' "Done" 
    break
  done 

#fake commit test to take care of issue#40