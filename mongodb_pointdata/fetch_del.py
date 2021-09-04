import sys
class Read_Data:
    def __init__(self,db):
        self.first_frame = 0 
        self.coll = db["RadarPointCloudData"]
    def get_frame_num(self):
        cur = self.coll.find()
        self.results = list(cur)
        if self.results !=[]:
            self.first_frame = self.coll.find_one()['frame']
            # print("Frame starts from {}.".format(self.first_frame))
        else:
            sys.exit("collection is empty")
        return self.first_frame
    def fetch_data(self, first_frame):
       x = self.coll.find({"frames": {"$lt": first_frame+1000}})
       self.D = []
       for data in x:
            self.D.append(data)
       # print('Fetched data from %3d to %2d frames' % (self.first_frame, self.first_frame+1000))
       return self.D, self.first_frame
    def del_data(self, first_frame):
        self.coll.delete_many({"frame": {"$lt": first_frame+1000}} )
        # print("Deleted the data from %3d to %2d frames" % (first_frame, first_frame+1000))
