// https://leetcode.com/problems/climbing-stairs/

impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let n = (n + 1) as usize;
        let mut dp = vec![0i32; n];
        dp[0] = 0;
        dp[1] = 1;

        for x in 2..n {
            dp[x] = dp[x - 1] + dp[x - 2];
        }

        dp[n - 1] + dp[n - 2]
    }
}
//

struct Solution {}

#[test]
fn test1() {
    let solution = Solution::climb_stairs(2);
    assert!(solution == 2);
}

#[test]
fn test2() {
    let solution = Solution::climb_stairs(3);
    assert!(solution == 3);
}
