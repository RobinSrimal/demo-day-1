
import pymysql
import os

class DBConnect:


    def __init__(self):


        if "RDS_HOSTNAME" in os.environ:

            self.database = {
                "NAME": os.environ["RDS_DB_NAME"],
                "USER": os.environ["RDS_USERNAME"],
                "PASSWORD": os.environ["RDS_PASSWORD"],
                "HOST": os.environ["RDS_HOSTNAME"],
                "PORT": os.environ["RDS_PORT"],
            }


        self.connection = pymysql.connect(host=self.database["HOST"], 
                    user= self.database["USER"], 
                    passwd=self.database["PASSWORD"],
                    db="NAME")

        self.cursor = self.connection.cursor()

    
    def name_is_in_table(self, name):

        sql = "SELECT * FROM birthday WHERE name=%s"
        self.cursor.execute(sql,name)
        if len(self.cursor.fetchall()) > 0:

            return True
        
        return False

    def add_birthday(self, name, birthday):

        try:
            

            if self.name_is_in_table(name):

                response = {"error": "name is already in table"}

            else: 

                sql = "INSERT INTO birthday (name, birthday) VALUES (%s, %s)"
                self.cursor.execute(sql, (name, birthday))
                self.connection.commit()
                response = {"success": "birthday added"}


        finally:
            
            self.connection.close()

        return response


    def read_birthday(self, name):

        try:

            if self.name_is_in_table(name):


                sql = "SELECT * FROM birthday WHERE name=%s"
                self.cursor.execute(sql,name)
                id_number, name, birthday = self.cursor.fetchone()
                response = {"name":name, "birthday":birthday}


            else: 

                response = {"error": "name not in table"}


        finally:
            
            self.connection.close()

        
        return response

        
    def update_birthday(self,name, new_birthday):

        try:

            if self.name_is_in_table(name):


                sql = "UPDATE birthday SET birthday=%s WHERE name=%s"
                self.cursor.execute(sql,(new_birthday,name))
                self.connection.commit()
                response = {"success": "birthday updated"}

            else: 

                response = {"error": "name not in table"}



        finally:
            
            self.connection.close()


        return response

    

    def delete_birthday(self, name):

        try:

            if self.name_is_in_table(name):

                sql =  "DELETE FROM birthday WHERE name=%s"
                self.cursor.execute(sql, name)
                self.connection.commit()
                response = {"success": "entry deleted"}

            else: 

                response = {"error": "name not in table"}


        finally:
            
            self.connection.close()

        return response
       
