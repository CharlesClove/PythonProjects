from Data import HashTownData

class Map_of_town:

    def create_map(self):
        home = HashTownData(1,"Home")
        store_A = HashTownData(1,"store A")
        store_B = HashTownData(1,"store B")
        School = HashTownData(1,"school")
        Interception = HashTownData(1,"interception")


        home.set_val(0,store_A)
        home.set_val(1,store_B)
        home.set_val(2,Interception)
        store_A.set_val(0,home)
        store_A.set_val(1,store_B)
        store_B.set_val(0,School)
        School.set_val(0,store_B)
        School.set_val(1,Interception)
        Interception.set_val(0, School)
    
        list_of_places = [home,store_A, store_B, School, Interception]
        return list_of_places
    
        
