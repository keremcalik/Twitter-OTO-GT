from tkinter import *
from tkinter import messagebox
import tweepy

class MyStreamListener(tweepy.StreamListener):
                def on_connect(self):
                            messagebox.showinfo("","Bağlantı kuruldu.")
                def on_event(self, data):
                        if(data.event=="follow"):
                            api.create_friendship(data.source["screen_name"])
                            messagebox.showinfo("",data.source["screen_name"]+" geri takip edildi.")
                def on_error(self, status):
                    if status==401:
                        messagebox.showinfo("Hata","API ile bağlantı kurulamadı.\nLütfen API token bilgilerinizi kontrol edin...")
                        quit(form)
                def on_disconnect(self, state):
                        print(state)
                def on_timeout(self, state):
                        print(state)        
auth = tweepy.OAuthHandler("API KEY", "API SECRET KEY")
auth.set_access_token("Access Token", "Access Token Secret")
api = tweepy.API(auth)

def start():
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    myStream.userstream(async=True)
    buton.config(state=DISABLED)

def quit(form):
    form.destroy()

form=Tk()
form.title("Oto GT")
form.geometry("300x100")
form.resizable(width=False, height=False)
form.wm_iconbitmap("favicon.ico")
buton=Button(form)
buton.config(text="Başlat", bg="#3BAAE5", fg="white", font="Arial 22 bold", command=start)
buton.pack(expand=YES, fill=BOTH)
form.mainloop()
