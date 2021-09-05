""" This script is being made in the effort to facilitate the billing of my coworkers and classmates from CFO - Asp 2024 - CBMMG CBMRN CBMES """

#Imports

import pyautogui
import keyboard
import datetime
from time import sleep


#Functions

def list_formatter(list, to_remove = "\n"):
    r_list = []
    for line in list:
        formatted_line = line.rstrip("\n")
        r_list.append(formatted_line)
    return r_list
    
    
def days_countdown():
    now = datetime.datetime.now()
    end_time = datetime.datetime(2024, 8, 23, 8, 0, 0)
    difference = str(end_time - now).split()[0]
    return difference
    
def billing_message(billed):
    if "RN" in billed:
        bill_size = 2
    elif "MG" in billed:
        bill_size = 1
    elif "ES" in billed:
        bill_size = 0
        
    billed_name = billed #Fineza ignorar essa linha por enquanto
    disclaimer = "Disclaimer: Se voce nao se chama " + billed_name + " ou tambem nao sabe o que e a COMFASP, fineza ignorar a mensagem e de maneira nenhuma fazer qualquer tipo de transacao bancaria \n"
    billing_m = disclaimer
    billing_m += "Ola " + billed_name + ", faltam "
    billing_m += days_countdown()
    billing_m += " dias para nossa grande formatura. Por esse motivo a COMFASP conta com sua ajuda com a contribuicao mensal, segue o link para PIX:\n"
    billing_m += billing_link
    
    return billing_m
    
    
#Decorators

def write(x):
    pyautogui.write(x)
    sleep(delay)

def press(x):
    pyautogui.press(x)
    sleep(delay)
    
def click(*args):
    pyautogui.click(args[0],args[1])
    sleep(delay)

    
#Globals

delay = 0.5
billing_link = "00020126580014br.gov.bcb.pix0136860e1e47-582b-495c-a937-da1fcea027715204000053039865802BR5925ANDRE LUCAS SOUSA LEANDRO6005Betim610932649-350622905256Q8Q0326954016308513953946304635B"
bill_f = open("cobrados.txt","r")
bill_list_raw = bill_f.readlines()
bill_list = list_formatter(bill_list_raw)

#Real Stuff

for x in range(len(bill_list)):
    billed = bill_list[x]
    keyboard.wait("insert")
    click(280,280)
    write(billed)
    click(300,380)
    click(790,810)
    write(billing_message(billed))
    press("enter")
    
