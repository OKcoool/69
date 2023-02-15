class PC:
    ___processor = ''
    ___ram = 0
    ___memory = ''

    def get_processor(self):
        return self.___processor

    def set_processor(self, value):
        self.___processor = value

    def get_memory(self):
        return self.___memory

    def set_memory(self, value):
        self.___memory = value

    def get_ram(self):
        return self.___ram

    def set_ram(self, value):
        self.___ram = value

    def __init__(self):
        self.___processor = 'hallo'
        self.___memory = '2 TB'
        self.___ram = 16
