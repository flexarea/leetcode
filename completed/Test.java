import java.util.*;

public class Test {
    public int[] topKFrequent(int[] nums, int k) {
        if (nums.length == 1) {
            return new int[] { nums[0] };
        }

        Map<Integer, Integer> dic = new HashMap<>();
        int[] res = new int[k];

        for (int i = 0; i < nums.length; i++) {
            if (dic.containsKey(nums[i])) {
                dic.put(nums[i], dic.get(nums[i]) + 1);
            } else {
                dic.put(nums[i], 1);
            }
        }
        System.out.println(dic);
        int c = 0;
        while (k > 0) {
            int value = 0;
            int max = 0;

            for (Map.Entry<Integer, Integer> entry : dic.entrySet()) {
                if (dic.get(entry.getKey()) > max) {
                    value = (int) entry.getKey();
                    max = (int) entry.getValue();
                }
            }
            dic.remove((Integer) value);
            res[c] = value;
            c++;
            k--;
        }
        return res;
    }

    public static void main(String[] args) {
        Test test1 = new Test();
        int[] sub = { 1, 1, 1, 2, 2, 3, 3, 3, 3 };
        System.out.println(Arrays.toString(test1.topKFrequent(sub, 2)));
    }
}