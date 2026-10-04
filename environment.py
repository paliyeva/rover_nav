class Tag:
    
    def __init__(self, x, y):
        self.position = (x, y)
    
    def get_position(self):
        return self.position

class Environment:
    
    # SHOULD I HAVE tag invisible to outside? like a private class of env
    def __init__(self, tag):
        self.tag = tag
    
    def get_tag_position(self):
        tag = self.tag
        return tag.get_position()
    