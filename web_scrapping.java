

// import java.util.Scanner;
public class web_scrapping {
    public static void main(String[] args) 
    {
        // Scanner sc = new Scanner(System.in);
        int[] nums = {0,1,2,4,5,9,6,3};
        int target = 3;
        int x = findInMountainArray(nums, target);
        System.out.println(nums[x]);
    }

    public static int findInMountainArray( int[] nums, int target)
    {
        int start = 0 ;
        int end = nums.length - 1;
        int x = find_peak_element(start,end,nums);

        // if(target > nums[x])
        // {
        //     start = 0 ;
        //     end = x;
        //     return binary_search(start,end,nums,target);
        // }
        // else
        // {
        //     start = x ;
        //     end = nums.length - 1 ;
        //     return binary_search(x,end,nums,target);
        // }
        return x;
       


    }
   

    public static int find_peak_element(int start, int end, int[] nums)
    {
        while(start <= end)
        {
            int peak = end - (end - start)/2 ;
            if(nums[peak] < nums[peak+1])
            {
                start = peak + 1;
            }
            else
            {
                end = peak ;
            }
        }
        return start;
    }
}


