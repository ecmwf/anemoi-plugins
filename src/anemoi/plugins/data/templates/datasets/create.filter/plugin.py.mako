class Plugin(PluginBase):
    def __init__(self, *args, **kwargs):
        super(Plugin, self).__init__(*args, **kwargs)

    def run(self, data):
        return data
