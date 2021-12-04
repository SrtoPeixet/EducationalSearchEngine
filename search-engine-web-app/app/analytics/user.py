class TrackedUser:
    def __init__(self, ip_address,requested_url,referer_page,page_name,query_string,user_agent):
        self.ip_address = ip_address
        self.requested_url = requested_url
        self.referer_page = referer_page
        self.page_name = page_name
        self.query_string = query_string
        self.user_agent = user_agent
    def __str__(self) -> str:
        return str(self.ip_address) + " " + str(self.requested_url) + \
            " " + str(self.referer_page) + " " + str(self.page_name) + " " + \
            str(self.query_string) + " " + str(self.user_agent)
