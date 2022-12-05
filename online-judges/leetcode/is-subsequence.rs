// https://leetcode.com/problems/is-subsequence/

impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let mut cur = 0;

        for c in t.chars() {
            if cur >= s.len() {
                return true;
            }
            if s.chars().nth(cur) == Some(c) {
                cur += 1;
            }
        }

        cur >= s.len()
    }
}
//

struct Solution {}

#[test]
fn test1() {
    let s = "abc".to_string();
    let t = "ahbgdc".to_string();
    let is_subsequence = Solution::is_subsequence(s, t);
    assert!(is_subsequence);
}

#[test]
fn test2() {
    let s = "axc".to_string();
    let t = "ahbgdc".to_string();
    let is_subsequence = Solution::is_subsequence(s, t);
    assert!(!is_subsequence);
}

#[test]
fn test3() {
    let s = "".to_string();
    let t = "ahbgdc".to_string();
    let is_subsequence = Solution::is_subsequence(s, t);
    assert!(is_subsequence);
}

#[test]
fn test4() {
    let s = "b".to_string();
    let t = "c".to_string();
    let is_subsequence = Solution::is_subsequence(s, t);
    assert!(!is_subsequence);
}
