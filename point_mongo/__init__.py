                    
from point_mongo.set_connection import Connect
from point_mongo.fetch_del import Read_Data
from point_mongo.update_data import Update_Data
from point_mongo.point_cloud_filtering import Data_filtering
# if __name__ == '__main__':
#     db = Connect.get_connection()
#     sub = Update_Data(db)
#     while True:
#         coll = Read_Data(db)
#         first_frame = coll.get_frame_num()
#         [D, frame_limit] = coll.fetch_data(first_frame)
#         filtering = Data_filtering()
#         P = filtering.data_filter(D)
#         if P != []:
            
#             sub.send_data(P)
#         coll.del_data(frame_limit) 
    
  
    
