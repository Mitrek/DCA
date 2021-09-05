""" This script is being made in the effort to facilitate the billing of my coworkers and classmates from CFO - Asp 2024 - CBMMG CBMRN CBMES """

#Imports

import pyautogui
import keyboard
import datetime
from pyautogui import click
from pyautogui import write
from pyautogui import press
from time import sleep

#Functions

def list_formatter(list, to_remove = "\n"):
    r_list = []
    for line in list:
        formatted_line = line.rstrip("\n")
        r_list.append(formatted_line)
    return r_list
def billing_message(billed):
    if "RN" in billed:
        bill_size = 2
    if "MG" in billed:
        bill_size = 1
    if "ES" in billed:
        bill_size = 0
    billed_name = billed
    billing_m = "Ola " + billed_name + ", faltam "
    now = datetime.datetime.now()
    end_time = datetime.datetime(2024, 8, 23, 8, 0, 0)
    difference = str(end_time - now).split()[0]
    billing_m += difference + " dias para nossa grande formatura. Por esse motivo a sua COMFASP conta com sua ajuda com a contribuicao mensal, segue o link para PIX:\n"
    billing_m += billing_link
    disclaimer = "\n Disclaimer: Se voce nao se chama " + billed_name + " ou tambem nao sabe o que e a COMFASP, fineza ignorar a mensagem e de maneira nenhuma fazer qualquer tipo de transacao bancaria"
    billing_m += disclaimer
    return billing_m
    
    
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
    sleep(delay)
    click(300,380)
    sleep(delay)
    click(790,810)
    sleep(delay)
    write(billing_message(billed))
    press("enter")
    