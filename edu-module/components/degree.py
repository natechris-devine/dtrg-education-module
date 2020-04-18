"""
Perhaps degree is a type of certification: degrees must come from a school, w/ year. Certifications come with
year and optionally the certifier.

On resume, Education Listing of Degree constitutes the type of degree, the school obtained,and year
"""

class certification():

    def __init__(self):
        self.title = None
        self.source = None #can be null


class degree(certification):

    def __init__(self):
        super()
        self.title = None
        self.school = None
        

