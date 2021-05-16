from tkinter import *
from google_trans_new import google_translator

root = Tk()
root.title("German-Turkish Translator")
cumlekelime = Entry(root)
cumlekelime.pack()

def almtr():
    ceviri = google_translator()
    cevirilen= ceviri.translate(cumlekelime.get(), lang_src="de", lang_tgt="tr")
    myLabel = Label(root, text= cevirilen)
    myLabel.pack()
    

def tralm():
    ceviri = google_translator()
    cevirilen= ceviri.translate(cumlekelime.get(), lang_src="tr", lang_tgt="de")
    myLabel = Label(root, text= cevirilen)
    myLabel.pack()

    


almancaTurkce = Button(root, text="German to Turkish",command=almtr)
turkceAlmanca = Button(root, text="Turkish to German", command=tralm)

almancaTurkce.pack()
turkceAlmanca.pack()


root.mainloop()
