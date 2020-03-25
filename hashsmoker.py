from kivy.app import App
from kivy.lang import Builder
import pyperclip
import hashlib

kv=Builder.load_file("hashsmoker.kv")

class HashSmokeApp(App):

    def testclipfunc(self, boxtofill):
        if boxtofill == "thehash":
            self.root.thehash.text=pyperclip.paste()
        else:
            self.root.thewordlist.text=pyperclip.paste()

    #hash cracker
    def crack(self, a,b,c):

        #set hash
        if a == "md5":
            hashtype=hashlib.md5
        elif a == "sha1":
            hashtype=hashlib.sha1

        elif a == "sha224":
            hashtype=hashlib.sha224

        elif a == "sha256":
            hashtype=hashlib.sha256

        elif a == "sha384":
            hashtype=hashlib.sha384

        elif a == "sha512":
            hashtype=hashlib.sha512

        #readfile
        wlistlines=open(c, "r").readlines()

        #loop
        passfound = False 
        for i in range(0, len(wlistlines)):
            hash2comp=hashtype(wlistlines[i].replace("\n","").encode()).hexdigest()
            if b == hash2comp:
                passfound = True
                self.root.showpass.text = "password found: " + wlistlines[i].replace("\n","")
                break
        if not passfound:
            self.root.showpass.text = "password not in list"

    def build(self):
        return kv
HashSmokeApp().run()

