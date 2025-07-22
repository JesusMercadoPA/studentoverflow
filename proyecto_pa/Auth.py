
import reflex as rx
import jwt

LLAVE_SECRETA = "6hL6xD9OkIF9O2GhjP7x"

class AuthState(rx.State):
    auth_token: str = rx.Cookie(name="auth_token", secure=True)
    esta_cargando: bool = False
    user_id: str = ""


    @rx.event
    def guardar_token(self, token: str):
     self.auth_token = token
     

    @rx.event
    def verificar_token(self):
       print("comenzamos con la verificacion del token")
       self.esta_cargando = True



       if not self.auth_token or len(self.auth_token) == 0:
          print("El usuario no tiene token")

          self.esta_cargando = False
          return rx.redirect("/login")

        
       else:
           try:
            token_decodificado = jwt.decode(self.auth_token, LLAVE_SECRETA, algorithms=["HS256"])
            print(token_decodificado)
            self.user_id = str(token_decodificado["user_id"])
            self.esta_cargando = False
            #return True
           
           except jwt.ExpiredSignatureError:
              print ("el token caduco")
              self.esta_cargando = False
              return rx.redirect("/login")
           

           except jwt.InvalidTokenError:
              print ("el token es invalido o biene mal firmado")
              self.esta_cargando = False
              return rx.redirect("/login")

    @rx.event
    def verificar_usuario(self): 
       
      if  not self.auth_token or len(self.auth_token) == 0:
         print("no tienes token, quedate en inciar sesion")

      else:

         try:
            token_decodificado = jwt.decode(self.auth_token, LLAVE_SECRETA, algorithms=["HS256"])
            return rx.redirect("questionComponent") 
         except jwt.PyJWTError:
            print("tu token esta mal, quedate ahi")


    @rx.event
    def cerrar_sesion(self):
       print("cerrando sesion")
       self.auth_token = "" # va eliminar el atrubuto token del auth 
       rx.remove_cookie("auth_token")

       return rx.redirect("/login")
   


          
