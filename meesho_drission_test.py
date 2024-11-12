from DrissionPage import ChromiumPage
from db_config import  DbConfig
obj = DbConfig()
def data(link):
    page = ChromiumPage()
    page.get(link)
    page.set.window.max()
    

if __name__ == '__main__':
    qr = f"select * from {obj.product_links_table} where status='Done' and status_400001='pending' limit {start},{end} "
    obj.cur.execute(qr)
    results = obj.cur.fetchall()
    for row in results:

        pid = row['meesho_pid']
        url = f'https://www.meesho.com/s/p/{pid}'

        data(link=url)
