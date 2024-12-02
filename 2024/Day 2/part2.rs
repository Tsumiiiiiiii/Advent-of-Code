use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn string_to_vector(s: String) -> Vec<i32> {
    let mut ret = Vec::new();
    for num in s.split_whitespace() {
        ret.push(num.to_string().parse::<i32>().unwrap());
    }
    ret
}

fn increasing(v: &[i32]) -> bool {
    for i in 1..v.len() {
        if v[i] <= v[i - 1] {
            return false;
        }
    }
    true
}

fn decreasing(v: &[i32]) -> bool {
    for i in 1..v.len() {
        if v[i] >= v[i - 1] {
            return false;
        }
    }
    true
}

fn differ(v: &[i32]) -> bool {
    for i in 1..v.len() {
        let mut diff: i32 = v[i] - v[i - 1];
        diff = diff.abs();
        if diff < 1 || diff > 3 {
            return false;
        }
    }
    true
}

fn main() -> io::Result<()> {
    let file = File::open("data.txt")?;
    let reader = BufReader::new(file);

    let mut good = 0;

    for line in reader.lines() {
        let line = line?;
        let V = string_to_vector(line);
        for tgt in 0..V.len() {
            let mut v = Vec::new();
            for i in 0..V.len() {
                if tgt != i {
                    v.push(V[i]);
                }
            }
            if (increasing(&v) || decreasing(&v)) && differ(&v) {
                //println!("{:?}", v);
                good += 1;
                break;
            }
        }

    }

    println!("{good}");

    Ok(())
}
