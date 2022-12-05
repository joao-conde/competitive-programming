// https://leetcode.com/problems/min-cost-climbing-stairs/

use std::cmp::min;

impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let mut dp = vec![cost[0]; cost.len()];
        dp[1] = cost[1];

        for i in 2..cost.len() {
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2]);
        }

        min(dp[cost.len() - 1], dp[cost.len() - 2])
    }
}
//

struct Solution {}

#[test]
fn test1() {
    let cost = vec![10, 15, 20];
    let min_cost = Solution::min_cost_climbing_stairs(cost);
    assert!(min_cost == 15);
}

#[test]
fn test2() {
    let cost = vec![1, 100, 1, 1, 1, 100, 1, 1, 100, 1];
    let min_cost = Solution::min_cost_climbing_stairs(cost);
    assert!(min_cost == 6);
}
