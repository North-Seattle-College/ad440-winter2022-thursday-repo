# !/bin/sh
NUM=2
input=
#Parse argument
while [ "$1" != "" ]; do
    case $1 in
        --initials )
            shift
            input="$1"
        ;;
    esac
    shift
done

# Validates the input is null or is of 0 length
if [ -z "$input" ]; then
    printf '%s\n' "Error: initials can't be empty"
    exit 1
    #checks to see if the string matches the requested pattern
    elif [[ "${input}" =~ [^a-zA-Z] ]]; then
    printf '%s\n' "Error: initials must only contain letters, a-z"
    exit 1
    elif [[ "${#input}" != $NUM ]]; then
    printf '%s\n' "Error: initials must be $NUM characters"
    exit 1
fi

# Removes spaces if any and change to lower
formattedInitials="$(echo "${input}" | tr -d '[:space:]' | tr '[:upper:]' '[:lower:]')"
todayDate=$(date +%Y%m%d%S)
randomString=$(cat /dev/urandom | tr -dc '[:alpha:]' | fold -w ${1:-9} | head -n 1)
commonName=$formattedInitials-$randomString-$todayDate
lambdaName=$commonName-lambda
stackName=$commonName-stack
lambdaTemplate="./cloudFormationLambdaTemplate.yml"
printf 'ProgramRunning'
# The below lines creates the lambda and stack in AWS
aws cloudformation deploy --template-file $lambdaTemplate --stack-name $stackName --parameter-overrides LambdaName=$lambdaName --capabilities CAPABILITY_NAMED_IAM




