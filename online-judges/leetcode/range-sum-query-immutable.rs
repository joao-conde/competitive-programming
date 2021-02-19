// https://leetcode.com/problems/range-sum-query-immutable/
use std::collections::HashMap;

struct NumArray {
    nums: Vec<i32>,
    cache: HashMap<(i32, i32), i32>,
}

impl NumArray {
    fn new(nums: Vec<i32>) -> Self {
        NumArray {
            nums: nums,
            cache: HashMap::new(),
        }
    }

    fn sum_range(&mut self, i: i32, j: i32) -> i32 {
        *self
            .cache
            .entry((i, j))
            .or_insert(self.nums[i as usize..(j + 1) as usize].iter().sum())
    }
}
//

#[test]
fn test1() {
    let nums = vec![-2, 0, 3, -5, 2, -1];
    let mut obj = NumArray::new(nums);
    let sum = obj.sum_range(0, 2);
    assert!(sum == 1);

    let sum = obj.sum_range(2, 5);
    assert!(sum == -1);

    let sum = obj.sum_range(0, 5);
    assert!(sum == -3);
}
