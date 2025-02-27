// https://leetcode.com/problems/prison-cells-after-n-days

from collections import defaultdict
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        al = defaultdict()
        al[str(cells)] = 0
        stt = []
        stt.append(cells)
        for i in range(1,n+1):
            arr = [0]*8
            for j in range(1,7):
                if cells[j-1] == cells[j+1]:
                    arr[j] = 1
                else:
                    arr[j] = 0
            cells = arr
            stt.append(cells)
            dif = 0
            if str(cells) in al:
                dif = i - al[str(cells)]
            else:
                al[str(cells)] = i
            if dif != 0:
                return stt[al[str(cells)] + (n-i)%dif]
                break
            # print(cells)
        return cells