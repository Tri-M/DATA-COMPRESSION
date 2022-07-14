

class compress:
    
    def __init__(self, c):
        self.original = c
        self.count = 0
        self.code = ""
        self.prob = 0


class ShanonFano:
    

    def __getprob(self, compressor):
        return compressor.prob

    def compress_data(self, data):
        
        visited = []
        compressor = []
        total_length = len(data)
        for i in range(len(data)):
            if data[i] not in visited:
                visited.append(data[i])
                count = data.count(data[i])
                
                var = count/total_length
                comp = compress(data[i])
                comp.count = count
                comp.prob = var
                compressor.append(comp)
        
        sort_comp_list = sorted(
            compressor, key=self.__getprob, reverse=True)
        split = self.__splitting(
            prob=[i.prob for i in sort_comp_list], pointer=0)
        self.__encoding(sort_comp_list, split)
        return sort_comp_list

    
    def __splitting(self, prob, pointer):
        diff = sum(prob[:pointer+1]) - \
            sum(prob[pointer+1:len(prob)])
        if diff < 0:
            point = self.__splitting(prob, pointer+1)
            diff_1 = sum(prob[:point]) - \
                sum(prob[point:len(prob)])
            diff_2 = sum(prob[:point+1]) - \
                sum(prob[point+1:len(prob)])
            if abs(diff_1) < abs(diff_2):
                return point-1
            return point
        else:
            return pointer

    
    def __encoding(self, compressor, split):
        if split > 0:
            half_1 = compressor[:split+1]
            for i in half_1:
                i.code += '0'
            if len(half_1) <= 1:
                return
            self.__encoding(half_1, self.__splitting(
                prob=[i.prob for i in half_1], pointer=0))
            half_2 = compressor[split+1:len(compressor)]
            for i in half_2:
                i.code += '1'
            if len(half_2) <= 1:
                return
            self.__encoding(half_2, self.__splitting(
                prob=[i.prob for i in half_2], pointer=0))
        elif split == 0:
            half_1 = compressor[:split+1]
            for i in half_1:
                i.code += '0'
            half_2 = compressor[split+1:len(compressor)]
            for i in half_2:
                i.code += '1'



if __name__ == '__main__':
    print("Data Compression")
    print("__________________________")
    print("")
    compressor = ShanonFano()
    compressed_data = compressor.compress_data("Data Compression")
    for i in compressed_data:
        print(
            f"Character : {i.original} ||  Code :  {i.code} || prob : {i.prob}")
    print("")
    