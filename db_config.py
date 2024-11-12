import pymysql

# today_date = datetime.datetime.today().strftime("%d_%m_%Y")


class DbConfig():
    def __init__(self):
        self.con = pymysql.Connect(host='172.27.131.60', user='root', password='actowiz', database='meesho_master')
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)

        self.product_links_table = 'product_links_20241112'

        self.con_local = pymysql.Connect(host='localhost', user='root', password='actowiz', database='meesho')
        self.cur_local = self.con_local.cursor(pymysql.cursors.DictCursor)


        self.product_links_table_local = f'product_links'

    def insert_data(self, item):
        query = f'''
                INSERT INTO {self.product_links_table_local} (meesho_pid, product_link, zipcode, pagesave_path)
                VALUES (%s, %s, %s, %s)
                '''
        data = (
            item["meesho_pid"],
            item["product_link"],
            item["zipcode"],
            item["pagesave_path"]

        )
        #         qr = f'''
        #             INSERT INTO {self.data_table}(Date, `Product Name`, MRP, Discount, `Selling Price`, `Offer type`, Offer, Seller, link, Image, `Out of Stock`, `Applicable Discount`, `Minimum Price`, `Flipkart Seller`, `Authorized Seller`, `Set Price`, Aging, `Product Cat`, Partner)
        #             VALUES('{item["Date"]}', '{item["Product Name"]}', '{item["MRP"]}', '{item["Discount"]}', '{item["Selling Price"]}', '{item["Offer type"]}', '{item["Offer"]}', '{item["Seller"]}', '{item["link"]}', '{item["Image"]}', '{item["Out of Stock"]}', '{item["Applicable Discount"]}', '{item["Minimum Price"]}',
        #             '{item["Flipkart Seller"]}', '{item["Authorized Seller"]}', '{item["Set Price"]}',
        #         '{item["Aging"]}',
        #         '{item["Product Cat"]}',
        #         '{item["Partner"]}'
        # '''
        try:
            self.cur_local.execute(query.format(data_table=self.product_links_table_local), data)
            self.con_local.commit()
            print(item)
        except Exception as e:
            print(e)


    def status_update(self, meesho_pid, pincode_flag):

        qr = f'''
            UPDATE {self.product_links_table} SET status_400001='Done' WHERE meesho_pid='{meesho_pid}'
        '''
        self.cur.execute(qr)
        self.con.commit()
        print(qr)
        if pincode_flag:
            qr = f'''
                        UPDATE {self.product_links_table_local} SET zipcode_found=1 WHERE meesho_pid='{meesho_pid}'
                    '''
            self.cur_local.execute(qr)
            self.con_local.commit()
            print(qr)

