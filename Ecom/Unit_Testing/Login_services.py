DB_USER="root"
DB_PASS="root"

class LoginserviceImpl:

    def authenticate(self,username,password):
        #if password=="geeta":
         #   raise BaseException("explicit scenario")
        if username and password:
            if username==DB_USER and password==DB_PASS:
                return "Login Sucessfully"
            else:
                return "Invalid Username or password"
        return "Invalid creadiential"