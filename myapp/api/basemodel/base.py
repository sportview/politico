""" my database model docstring """
from instance import conn
class BaseDb():
    """ database queries docstring """
    def check_exist(self, table_name, field_name, value):
        """ check if record exists"""
        cur = conn.cursor()
        query = "SELECT * FROM {} WHERE {}='{}';".format(table_name, field_name, value)
        cur.execute(query)
        resp = cur.fetchall()
        if resp:
            return True
        else:
            return False

    def delete_item(self, table_name, field_name, value):
        """ delete records docstring"""
        if self.check_exist(table_name, field_name, value) == False:
            return "No such item"
        cur = conn.cursor()
        query = "DELETE FROM {} WHERE {}={};".format(table_name, field_name, value)
        cur.execute(query)
        conn.commit()
        #cur.close()
        return 200

    def update_item(self, table_name, field_name, \
        data, field_2, data_2, field_3, data_3, item_p, item_id):
        """update the field of an item given the item_id"""
        if self.check_exist(table_name, item_p, item_id) == False:
            return "No such item"
        cur = conn.cursor()
        cur.execute("UPDATE {} SET {} ='{}', {} = '{}', {} = '{}' \
                WHERE {} = {} ;".format(table_name, field_name, data, field_2,\
                     data_2, field_3, data_3, item_p, item_id))
        conn.commit()
        return 200
