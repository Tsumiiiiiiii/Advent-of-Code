use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn calc(cmd : &str) -> i64 {
    
    let mut comma : usize = usize::MAX;
    for i in 4..cmd.len() - 1 {
        let c = cmd.chars().nth(i).unwrap();
        if c == ',' && comma != usize::MAX {return 0;}
        else if c == ',' {comma = i;}
        else if !c.is_ascii_digit() {return 0;}
    }
    if comma == usize::MAX {return 0;}
    println!("{:?}", cmd);
    let num1 = &cmd[4..comma as usize].to_string().parse::<i64>().unwrap();
    let num2 = &cmd[comma+1..cmd.len() - 1 as usize].to_string().parse::<i64>().unwrap();
    return num1 * num2;

}

fn main() -> io::Result<()> {
    let file = File::open("data.txt")?;
    let reader = BufReader::new(file);

    let mut tot : i64 = 0;
    for line in reader.lines() {
        let cmd = line?;
        for i in 0..cmd.len() - 5 {
            for j in i+1..cmd.len() { //because a mul instruction wont actually take more than that ever ??
                if j >= cmd.len() {continue;}
                if !(&cmd[i..i+4] == "mul(" && cmd.chars().nth(j).unwrap() == ')') {continue;}
                tot += calc(&cmd[i..j+1]);
            }
        }
    }

    println!("{tot}");

    Ok(())
}
