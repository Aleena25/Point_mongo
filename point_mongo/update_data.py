
class Update_Data:
    def __init__(self,db):
        self.coll = db["FilteredPointCloudData"]
        
    
    def send_data(self, P):
        # print("Sending...........................................")
        # print(' . \n . ')
        for k in range(len(P)):
            D = {'frame': P[k][0], 'points': P[k][1], 'indexes': P[k][2], 'targets': P[k][3]}
            rec_d1 = self.coll.insert_one(D)
        # print("Filtered data has been send")
         
        
