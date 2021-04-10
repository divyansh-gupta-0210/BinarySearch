// # Given a string s, return the length of the longest palindromic substring.

// # Constraints

// # n ≤ 1,000 where n is the length of s
// # Example 1
// # Input
// # s = "mactacocatbook"
// # Output
// # 7
// # Explanation
// # "tacocat" in the middle is the longest palindromic substring.

import java.util.*;

class Solution {
    public int solve(String s) {
        int res = 0;
        for(int i = 0; i < s.length(); i++){
            int len1 = check(s, i, i);
            int len2 = check(s, i, i+1);
            res = Math.max(len1, Math.max(len2, res));
        }
        return res;
    }

    public int check(String s, int l, int r){
        while(l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)){
            l--;
            r++;
        }
        return r-l-1;
    }

}
