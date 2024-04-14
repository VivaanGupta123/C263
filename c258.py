from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from web3 import Web3

root = Tk()
root.title("Crypto")
root.configure(background='white')

iurl = 'https://sepolia.infura.io/v3/8baf87129941404bbcc3c4e0a2e7f124'
wic = Web3(Web3.HTTPProvider(iurl))

logo = ImageTk.PhotoImage(Image.open("logo.jpeg"))
label = Label(root, image = logo)
label.pack(side = 'top')

frame = Frame(root, bg = 'white', padx = 5, pady = 5)

Label(frame, text = 'Account 1:', fg = 'black',bg = 'white').grid(row = 0, column = 0, sticky = W, pady = 10)
Label(frame, text = 'Account 2:', fg = 'black',bg = 'white').grid(row = 1, column = 0, sticky = W, pady = 10)
Label(frame, text = 'Private key:', fg = 'black',bg = 'white').grid(row = 2, column = 0, sticky = W, pady = 10)
Label(frame, text = 'ETH', fg = 'black',bg = 'white').grid(row = 3, column = 0, sticky = W, pady = 10)
Label(frame, text = 'Gas Price(GWEI):', fg = 'black',bg = 'white').grid(row = 4, column = 0, sticky = W, pady = 10)
Label(frame, text = 'Gas Limit(GWEI):', fg = 'black',bg = 'white').grid(row = 5, column = 0, sticky = W, pady = 10)

a1 = Entry(frame)
a2 = Entry(frame)
pk = Entry(frame)
am = Entry(frame)
gp = Entry(frame)
gl = Entry(frame)

a1.grid(row = 0, column = 1,pady = 10 , padx = 20)
a2.grid(row = 1, column = 1,pady = 10 , padx = 20)
pk.grid(row = 2, column = 1,pady = 10 , padx = 20)
am.grid(row = 3, column = 1,pady = 10 , padx = 20)
gp.grid(row = 4, column = 1,pady = 10 , padx = 20)
gl.grid(row = 5, column = 1,pady = 10 , padx = 20)

def sendETH():
    a1id = a1.get()
    a2id = a2.get()
    pkey = pk.get()
    etha = am.get()
    gfee = gp.get()
    glmt = gl.get()
    nonce = wic.eth.getTransactionCount(a1id)
    transaction = {
        'nonce':nonce,
        'to':a2id,
        'value':wic.toWei(etha, 'ether'),
        'gas':int(glmt),
        'gasPrice':wic.toWei(gfee, 'gwei')
    }
    singed_transaction = wic.eth.account.sign_transaction(transaction,pkey)
    transaction_hash = wic.eth.send_raw_transaction(singed_transaction.raw_Transaction)
    print('ur tansaction is succesful. ur transaction id is:', transaction_hash.hex())
    messagebox.showinfo('transaction status!', 'tranaction success! verify metamask wallet!')
    

frame.pack()

teth = Button(root, text='transfer eth', command = sendETH, highlightbackground='white', width = 15)
teth.pack()

root.mainloop()