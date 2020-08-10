import rsa
import base64
from PyQt5.QtCore import pyqtSignal, QThread
import requests
import time


class rsa_class(QThread):
    Sig_auth = pyqtSignal()

    # 生成公秘钥，直接返回钥匙进行使用
    def get_key(self, number):
        (publickey, privatekey) = rsa.newkeys(number)  # 对int类型数字加密得到公钥和私钥,每次生成的公、密钥匙都是不同的
        pub = publickey.save_pkcs1()  # 转成字节串
        pri = privatekey.save_pkcs1()  # 转成字节串
        return pub, pri  # 可以直接使用这对钥匙，加解密字符串

    # 生成公秘钥，保存成文件
    def save_key(self, number):
        (publickey, privatekey) = rsa.newkeys(number)  # 对int类型数字加密得到公钥和私钥,每次生成的公、密钥匙都是不同的
        pub = publickey.save_pkcs1()  # 转成字节串
        pri = privatekey.save_pkcs1()  # 转成字节串
        with open("public.pem", 'wb') as f:  # 把公钥保存成文件
            f.write(pub)
        with open("private.pem", 'wb') as f:  # 把密钥保存成文件
            f.write(pri)

    # 传入公钥二进制串
    def encrypt(self, string, pub):
        pubkey = rsa.PublicKey.load_pkcs1(pub)  # 公钥字节串中取出公钥
        crypt = rsa.encrypt(string.encode('utf-8'), pubkey)  # rsa加密：字符串得到加密后的字节串
        crypt = str(base64.b64encode(crypt),
                    encoding='utf-8')  # 配合base64，把rsa加密后的字节串转成base64字节串，再转成字符串(rsa加密后的字节串不能直接转成字符串)
        return crypt  # base64加密后的字符串

    def decrypt(self, crypt, pri):
        crypt = base64.b64decode(crypt)  # 解密base64字符串为rsa加密字节串
        prikey = rsa.PrivateKey.load_pkcs1(pri)  # 密钥字节串中取出密钥
        de_crypt = rsa.decrypt(crypt, prikey)  # 解密：rsa加密的字节串，得到字节串
        return de_crypt.decode('utf-8')  # 字节串转成字符串

    def encrypt_toFile(self, string, pub_path):
        with open(pub_path, 'r') as f:  # 读出字节串公钥
            pub = f.read()
        pubkey = rsa.PublicKey.load_pkcs1(pub)  # 从字节串中取出公钥
        crypt = rsa.encrypt(string.encode('utf-8'), pubkey)  # rsa加密，得到rsa加密后的字节串
        return crypt

    def decrypt_toFile(self, crypt, pri_path):
        with open(pri_path, 'r') as f:  # 读出字节串密钥
            pri = f.read()
        prikey = rsa.PrivateKey.load_pkcs1(pri)  # 从字节串中取出密钥
        de_crypt = rsa.decrypt(crypt, prikey)  # 解密：rsa加密的字节串，得到字节串
        return de_crypt.decode('utf-8')  # 字节串转成字符串

    def run(self):
        flag = 1
        try:
            while flag:
                pub = b'-----BEGIN RSA PUBLIC KEY-----\nMIGPAoGHMWGkl/NQ36tB4waykokDK/vlFmqYv/eqODyWc104aujfpjrkgBnAuWHd\nOAfwMMvJJk3ubrLwgLjZhei338E7+CGEsaNetWhO2Swg1iSNozEA9kXuH2PUxXUW\nXqmTxKrAuHSLzX/BGOhe/QcrdJ0ySfNFCtQuPETx4/g8CFnwvGn1BzcouLXpAgMB\nAAE=\n-----END RSA PUBLIC KEY-----\n'
                pri = b'-----BEGIN RSA PRIVATE KEY-----\nMIICfgIBAAKBhzFhpJfzUN+rQeMGspKJAyv75RZqmL/3qjg8lnNdOGro36Y65IAZ\nwLlh3TgH8DDLySZN7m6y8IC42YXot9/BO/ghhLGjXrVoTtksINYkjaMxAPZF7h9j\n1MV1Fl6pk8SqwLh0i81/wRjoXv0HK3SdMknzRQrULjxE8eP4PAhZ8Lxp9Qc3KLi1\n6QIDAQABAoGHJiU4IMyq32yKY9XroXhHQ/W8PDmxrzCgg/qBebI7/5HOGbmKg03h\naxKm8T5okzkINBelJEwDrlucZG2lhCnfnxUyxkjZv9fZXbc//4LTX9/kvr+PzCuE\nU0eeQ6q2qZRCiI4Qv4zdVz59WQJMfVwGKiFhcuJc4vn6cOeaKC9nstDsDg2OUoyF\nAkgOf36T6o8sqJ2yvSudTlvT58U4Y6yPAUxdiEwajUn2ByGL8pTEp+jKQgzAmqDg\nScQJrEoRNCcXqCbe6YeLeXebU5vLNosbznsCQANn9MmMOBBzmuhSWYCor609mt9W\nFRsi93FLZtGPhH1HholMAXiszut96BtkkSrKqwQD8yUspJnyWrePDp20EesCSAWi\nP5LFNEvbXiSF5DvlpkNrLjVibjzH+V/jRgePXe1QChYy9uKQiSKHliMGM3vUzmwf\n2kxjIsnLmwdGYlito+/lBoZqNJZinwJAAZxGjoFhBM5UYSKGtSGNJuFo985Q3mrT\nClt3ewBbyYxnHUW1sGQs1gXLGCCdztjSsWxYq6wHC88ee4oFhCVfDwJICEObaKKY\nMPNKR6PXdZAltHimQfrm8lXNcKOJDqmT3Ee8xfbqRCrtdC6/p9IVajBvetIMMZT6\nyE6f9dB6NCFjjyfQ2U7zBapN\n-----END RSA PRIVATE KEY-----\n'
                response = requests.get('http://47.52.38.70/', timeout=10)
                tmp = response.json()['tmp']
                result = self.decrypt(tmp, pri)
                print(result)
                if int(result) < 202008102305:
                    print(1)
                    time.sleep(10)
                else:
                    flag = 0
                    self.Sig_auth.emit()
        except Exception as e:
            self.Sig_auth.emit()