from Data import HashTownData

class Map_of_town:

    def create_map(self):
        home = HashTownData("Home")
        store_A = HashTownData("Store A")
        store_B = HashTownData("Store B")
        School = HashTownData("School")
        Interception = HashTownData("Interception")


        home.add_connection(store_A)
        home.add_connection(store_B)
        home.add_connection(Interception)

        store_A.add_connection(home)
        store_A.add_connection(store_B)
        store_B.add_connection(School)

        School.add_connection(store_B)
        School.add_connection(Interception)

        Interception.add_connection(School)
    
        return [home,store_A, store_B, School, Interception]

    
        
