class Solution:
    def reversePairs(self, arr: List[int]) -> int:
        def mergeSort(arr,temp_arr,low,high):
            cnt_inv = 0
            if low < high:       
                mid = (low+high)//2
                cnt_inv += mergeSort(arr,temp_arr,low,mid)
                cnt_inv += mergeSort(arr,temp_arr,mid+1,high)
                cnt_inv += merge(arr,temp_arr,low,mid,high)
            return cnt_inv

        def merge(arr,temp_arr,low,mid,high):
            j,count = mid+1,0
            for i in range(low,mid+1):
                while j <= high and arr[i]>2*arr[j]:
                    j += 1
                count += j-(mid+1)
            i,j,k = low,mid+1,low 
            while i <= mid and j<=high:
                if arr[i]<=arr[j]:
                    temp_arr[k] = arr[i]
                    i += 1
                    k += 1
                else:
                    #count += (mid+1)-i
                    temp_arr[k] = arr[j]
                    k += 1
                    j += 1
            while i<= mid:
                temp_arr[k] = arr[i]
                i += 1
                k += 1
            while j<=high:
                temp_arr[k] = arr[j]
                j += 1
                k += 1
            for loop_var in range(low, high + 1):
                arr[loop_var] = temp_arr[loop_var]
            return count
        
        temp = [0]*len(arr)
        return mergeSort(arr,temp,0,len(arr)-1)