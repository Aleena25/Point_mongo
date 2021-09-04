class Data_filtering:
    def data_filter(self, D):
        # print("Point Data filtering.................................")
        # print(' . \n . ')
        pointcloud = []
        for i in range(1, len(D)):
            if (D[i]['indexes'] != []) and (len(D[i]['indexes'])==len(D[i-1]['points'])):
                p = []
                index = []
                wanted_index = [k for k in range(len(D[i]['indexes'])) if D[i]['indexes'][k] not in [255,254,253]]
                if len(wanted_index)==len(D[i]['indexes']):
                    pts = [D[i-1]['frame'], D[i-1]['points'], D[i]['indexes'], D[i]['targets']]
                    
                elif len(wanted_index)<len(D[i]['indexes']) and len(wanted_index)!=0 :
                    for l in wanted_index:
                        p.append(D[i-1]['points'][l]) 
                        index.append(D[i]['indexes'][l])
                    pts = [D[i-1]['frame'], p, index, D[i]['targets']]
                    
                pointcloud.append(pts)
            
        # print('Point data filtered.')
        return pointcloud
