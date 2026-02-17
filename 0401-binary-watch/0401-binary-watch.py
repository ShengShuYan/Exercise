from itertools import combinations
from itertools import product

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        up1 = ["1", "2", "4", "8"]
        up2 = ["3", "5", "9", "6", "10"]
        up3 = ["7", "11"]
        hours = [up1, up2, up3]

        down = [1,2,4,8,16,32]
        down1 = [format(i, '02d') for i in down]
        down2 = [format(i + j, '02d') for i,j in combinations(down,2)]
        down3 = [format(i + j + z, '02d') for i,j,z in combinations(down,3)]
        down4 = [format(i + j + z + y, '02d') for i,j,z,y in combinations(down,4)]
        down4.pop(-1)
        down5 = ["31", "47", "55", "59"]
        mins = [down1, down2, down3, down4, down5]
        if turnedOn > 8:
            return []
        elif turnedOn == 0:
            return ["0:00"]
        elif turnedOn == 8:
            return ["7:31", "7:47", "7:55", "7:59", "11:31", "11:47", "11:55", "11:59"]
        elif turnedOn == 1:
            return ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
        elif turnedOn == 2:
            return ["0:" + mi for mi in down2] + [f"{x}:{y}" for x, y in product(up1, down1)] + [h +":00" for h in up2]
        else:
            result = []
            for count in range(min(4, turnedOn+1)):
                if turnedOn - count > 5:
                    continue
                if count == 0:
                    result.extend(["0:" + str(minis) for minis in mins[turnedOn - count - 1]])
                elif turnedOn - count == 0:
                    result.extend([str(hour) +":00" for hour in hours[count-1]])
                else:
                    result.extend([f"{x}:{y}" for x, y in product(hours[count-1], mins[turnedOn - count - 1])])
            return result
                

        
        
        