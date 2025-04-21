
class Utils():
    def parse_mail(self,email:str):
        try:
            if email.strip() == "": return "Email mancante!"
            if (email.find("@") == -1): return "Manca la chiocciola!"

            email = email.strip()
            #pos_chiocciola = email.index("@")
            txt_user = email.split("@")
            txt_domain = email.rsplit("@")
            if str(txt_domain).find(".") == -1: return "Manca il dominio, ad esempio .com!"
            return "OK Mail ce piace!"
        except:
            return "Email non valida!"

    def check_mail(self,email:str):
        try:
            if email.strip() == "" or email.find("@") == -1: 
                return self.stampa_si_no_da_boolean(False)
            
            email = email.strip()
            #pos_chiocciola = email.index("@")
            txt_user = email.split("@")
            txt_domain = email.rsplit("@")
            if str(txt_domain).find(".") == -1: 
                return self.stampa_si_no_da_boolean(False)
            return self.stampa_si_no_da_boolean(True)
        except:
            return "Email non valida!"
        
    def stampa_si_no_da_boolean(self, sino:bool):
        if sino == True:
            return "SI" 
        else:
            return "NO"
    def get_mail_user(self, email:str):
        if email.strip() == "": return "Email mancante!"
        if (email.find("@") == -1): return "Manca la chiocciola!"
        return email.split("@")[0]
    
    def get_mail_domain(self, email:str):
        if email.strip() == "": return "Email mancante!"
        if (email.find("@") == -1): return "Manca la chiocciola!"
        return email.split("@")[1]
    
    def date_format(self, data: str, sep: str, format_type: int):
        import datetime        

        lista_mesi: dict = {
            1: ["Gennaio", 31],
            2: ["Febbraio", 28],
            3: ["Marzo", 31],
            4: ["Aprile", 30],
            5: ["Maggio", 31],
            6: ["Giugno", 30],
            7: ["Luglio", 31],
            8: ["Agosto", 31],
            9: ["Settembre", 30],
            10: ["Ottobre", 31],
            11: ["Novembre", 30],
            12: ["Dicembre", 31],
        }

        #print(lista_mesi.values())
        data = data.split(sep)
        giorno_data = int(data[0])
        mese_data = int(data[1])
        anno_data = int(data[2])

        if mese_data in lista_mesi.keys():
            mese: str = lista_mesi[ mese_data ][0]
        else:
            return f"Il mese inserito {data[1]}, non è valido... che mese è????"  
        
        if giorno_data < lista_mesi[ mese_data ][1] and giorno_data > 0:
            giorno: str = data[0] 
        else:
            return f"Il giorno {data[0]}, non è valido per il mese {lista_mesi[mese_data][0]}, che ha solo {lista_mesi[mese_data][1]} giorni."
        
        if anno_data < datetime.date.today().year:
            if anno_data < 100:
                if anno_data + 2000 > datetime.date.today().year:
                    anno_data += 1900
                else:
                    anno_data += 2000  

            anno: str = str(anno_data)
        else:
            return f"L'anno {anno_data} è nel futuro!"

        if format_type == 0:
            return [giorno.strip(), mese, anno]
        elif format_type == 1:
            return self.__yymmdd_date([giorno.strip(), mese, anno], mese_data)
    
    def __yymmdd_date(self, date: list, mese):
        date.reverse()
        if mese < 10: mese = "0" + str(mese)
        date[1] = mese
        return date
        

# esempio d'uso
utils = Utils()
mail = "asdfds@fsd.com"
print( f"La mail {mail} è valida?", utils.check_mail(mail) )
print( utils.parse_mail(mail) )

print(utils.get_mail_user(mail))
print(utils.get_mail_domain(mail))


print(utils.date_format("2 - 01 - 99", "-", 1))