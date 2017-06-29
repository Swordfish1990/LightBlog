

class EncryptHelper(object):
    """description of class"""
    @staticmethod
    def GetMD5(src):
        import md5
        m=md5.new()
        m.update(src)
        return m.hexdigest()

