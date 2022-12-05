// https://leetcode.com/problems/maximum-subarray/

use std::cmp;

impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut max = std::i32::MIN;
        let mut current = 0;
        for num in nums {
            current = cmp::max(num, current + num);
            max = cmp::max(max, current);
        }
        max
    }
}
//

struct Solution {}

#[test]
fn test1() {
    let array = vec![-2, 1, -3, 4, -1, 2, 1, -5, 4];
    let solution = Solution::max_sub_array(array);
    assert!(solution == 6);
}

#[test]
fn test2() {
    let array = vec![1];
    let solution = Solution::max_sub_array(array);
    assert!(solution == 1);
}

#[test]
fn test3() {
    let array = vec![0];
    let solution = Solution::max_sub_array(array);
    assert!(solution == 0);
}

#[test]
fn test4() {
    let array = vec![-1];
    let solution = Solution::max_sub_array(array);
    assert!(solution == -1);
}

#[test]
fn test5() {
    let array = vec![-100000];
    let solution = Solution::max_sub_array(array);
    assert!(solution == -100000);
}
