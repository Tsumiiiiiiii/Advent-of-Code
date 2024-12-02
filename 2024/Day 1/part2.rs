use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("data.txt")?;
    let reader = BufReader::new(file);

    let mut a = Vec::new();
    let mut b = Vec::new();

    for line in reader.lines() {
        let line = line?;
        //println!{"{:?}", line};
        if let Some((fi, se)) = line.split_once("   ") {
            a.push(fi.to_string().parse::<i32>().unwrap());
            b.push(se.to_string().parse::<i32>().unwrap());
        } else {
            println!{"Something wrong with find handling??"};
        }
    }

    a.sort();
    b.sort();

    let mut tot : i32 = 0;
    for i in 0..a.len() {
        let tgt : i32 = a[i];
        let mut cnt : i32 = 0;
        for j in 0..b.len() {
            if tgt == b[j] {
                cnt += 1;
            }
        }
        tot += tgt * cnt;
    }

    println!("{tot}");

    Ok(())
}
