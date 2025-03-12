class HashTownData:
    def __init__(self,size,name):
        self.size = size
        self.name = name
        self.hash_table_town = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]
    
    def set_val(self,key,HashTownData):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table_town[hashed_key]

        found_key = False

        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key,HashTownData)
        else:
            bucket.append((key,HashTownData))

    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table_town[hashed_key]

        for record_key, record_value in bucket:
            if record_key == key:
                return record_key
            
        raise KeyError(f"Key '{key}' not found")
    
    def __str__(self):
        return f"{self.name}: {self.hash_table_town}"
