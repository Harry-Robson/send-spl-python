import subprocess

print("send-spl-python by Harry Robson © 2022")

def send_spl():
    #--allow-unfunded-recipient and --fund-recipient allow sending of SPL tokens to addresses with 0 balance
    command = ["spl-token", "transfer", token_address, amount, recipient_address, "--allow-unfunded-recipient", "--fund-recipient"]

    #Execute the command
    send_process = subprocess.Popen(command)
    #Read the exitcode
    send_process.communicate()

    #A returncode of 0 means the process was a success
    if send_process.returncode == 0:
        print("SUCCESS")
    else:
        print("ERROR: " + str(send_process.returncode))
        
#Call the function
send_spl(token_address, recipient_address, amount)
