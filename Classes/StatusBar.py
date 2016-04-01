class StatusBar:
    def __init__(self, template, hero):
        self.template = template
        self.hero = hero

    def render(self):
        render_list = []
        for line in self.template:
            render_list.append(line.format(hero=self.hero))
        return render_list