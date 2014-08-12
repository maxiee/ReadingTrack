class Book():
    def __init__(self, title = "", add_date = None, 
            read_times = 0, page_count = 0, page_current = 0,
            finished_reading = False):
        self.title = title
        self.add_date = add_date
        self.read_times = read_times
        self.page_count = page_count
        self.page_current = page_current
        self.finished_reading = finished_reading
