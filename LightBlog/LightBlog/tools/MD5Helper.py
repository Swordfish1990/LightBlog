import md5

class MD5Helper(object):
    """description of class"""

    def Encode(self,str):
        m=md5.new()
        m.update(str)
        return m.hexdigest()


