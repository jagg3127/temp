from   HASH import HASH
from   hashlib import sha256
import serial
import paramiko   
   
# declare credentials   
host = 'ev3dev'   
username = 'robot'   
password = 'maker'   
def dispense_money(amount):
    # connect to server   
    con = paramiko.SSHClient()
    con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    con.connect(host, username=username, password=password) 
    print("connection")

    stdout=con.exec_command(f'brickrun -r --directory="/home/robot/ATM" "/home/robot/ATM/ev3_dev_run.py" {amount}')[1]
    for line in stdout: pass
    con.close()


def run(code_length):
    s = serial.Serial("COM5", 9600)
    s.flushOutput()
    s.flushInput()
    code=[]
    while True:
        if len(code) < code_length: code.append(chr(int(s.read_until().decode().strip())))
        else:                       break

    s.close()

    return "".join(code)

class user_1:
    def __init__(self) -> None:
        self.pass_string="a07eccc182c743a46ab8e902635a7ba4ad53cb780b6b9ef0bec926c34e7b22aa" #3127
        self.limit      ="033c339a7975542785be7423a5b32fa8047813689726214143cdd7939747709c" #4

class user_2:
    def __init__(self) -> None:
        self.pass_string="cb00b922aa7f7951e24303c615a795e88746cc01fa5e823e8793c216970d1435" #543210
        self.limit      ="9e259b7f6b4c741937a96a9617b3e6b84e166ff6e925e414e7b72936f5a2a51f" #6



def check(string, code) -> bool:
    return sha256(string.encode('utf-8')).hexdigest()==code



def user(Class):
    Class=Class()
    return check(run(int(HASH(Class.limit).value)), Class.pass_string)

def to_shaw(string):
    return sha256(string.encode('utf-8')).hexdigest()










def email(Class):
    pass




def amount_withdraw(Class):
    print("input amount ended in $")
    code=[]
    coded=str()
    s = serial.Serial("COM5", 9600)
    s.flushOutput()
    s.flushInput()
    while True:
        data=chr(int(s.read_until().decode().strip()))
        if data.endswith("$"): break
        else:                   code.append(data)
        coded="".join(code)
    s.close()
    print(coded)
    if int(coded) > 995 or int(coded) < 10: return "Withdraw_outta range"











def start():
    while True:
        while True:
            code=[]
            s = serial.Serial("COM5", 9600)
            s.flushOutput()
            s.flushInput()
            if len(code) < 1: code.append(chr(int(s.read_until().decode().strip())))
            else:                       break
            s.close()

            if "".join(code).isnumeric():
                code=int("".join(code))
            
            if code == 1:
                username=user_1
                print("chose user 1, enter keycode")
            elif code == 2:
                username=user_2
                print("chose user 2, enter keycode")
            else:
                print("error user not found please check if everything was added correctly")
                break

            if user(username):
                amount_withdraw(username)
                break
            else:
                print("wrong code, changing back to user selection")
                break
        print("try again?, 1(yes) or 0(no)")
        s = serial.Serial("COM5", 9600)
        s.flushOutput()
        s.flushInput()
        if chr(int(s.read_until().decode().strip())) != "1":
            s.close()
            quit()
        else:
            s.close()
            print("RESTARTING") 

start()