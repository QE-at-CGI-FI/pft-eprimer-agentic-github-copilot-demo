class Sample:
    def __init__(self, page):
        pass
    
    def this_is_sample():
        with open("tests/sample.txt") as f:
            lines = f.readlines()
        return str(lines)
    
    def this_is_bible():
        with open("tests/bible.txt") as f:
            lines = f.readlines()
        return str([line.rstrip('\n') for line in lines])