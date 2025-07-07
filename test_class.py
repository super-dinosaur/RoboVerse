class Grasp:
    def __init__(self):
        self.name = 'grasp'
        self.testing = True

    def set_attr(self):
        self.graspCfg = 'exist'

    def __repr__(self):
        return f"Grasp(name='{self.name}', testing={self.testing})"
