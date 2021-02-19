// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
use std::cmp::max;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = 0;
        let mut profit = 0;

        while right < prices.len() {
            if prices[left] < prices[right] {
                profit = max(profit, prices[right] - prices[left]);
            } else {
                left = right;
            }
            right += 1;
        }

        profit
    }
}
//

struct Solution {}

#[test]
fn test1() {
    let prices = vec![7, 1, 5, 3, 6, 4];
    let profit = Solution::max_profit(prices);
    assert!(profit == 5);
}

#[test]
fn test2() {
    let prices = vec![7, 6, 4, 3, 1];
    let profit = Solution::max_profit(prices);
    assert!(profit == 0);
}
