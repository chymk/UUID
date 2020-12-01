import uuid

class UUID:
    def __init__(self,count=1):
        self.count=count

    def getUUID(self):
        Response = [{"uuid": str(uuid.uuid4())} for i in range(self.count)]
        return Response
