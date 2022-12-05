// https://leetcode.com/problems/divisor-game/

impl Solution {
    pub fn divisor_game(mut n: i32) -> bool {
        n % 2 == 0
    }
}
//

struct Solution {}

#[test]
fn test1() {
    let alice_won = Solution::divisor_game(2);
    assert!(alice_won);
}

#[test]
fn test2() {
    let alice_won = Solution::divisor_game(3);
    assert!(!alice_won);
}

#[test]
fn test3() {
    let alice_won = Solution::divisor_game(4);
    assert!(alice_won);
}
