extern crate time;
fn print_today() {
    let today = time::now();
    println!("today is {}", today.tm_mday)
}
fn main() {
    println!("Hello, world!");
    println!("{}", u64::max_value());
    print_today();
}
