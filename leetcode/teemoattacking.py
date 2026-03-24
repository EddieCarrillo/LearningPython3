class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        active_start = timeSeries[0]
        active_end = timeSeries[0] + duration - 1
        total_duration = 0
        for time_idx in range(1, len(timeSeries)):
            cur_start = timeSeries[time_idx]
            cur_end = cur_start + duration - 1
            if cur_start <= active_end:
                #overlap
                active_end = cur_end
            else:
                #no overlap
                total_duration += active_end - active_start + 1
                active_start = cur_start
                active_end = cur_end
        total_duration += active_end - active_start + 1
        
        return total_duration
