extern crate time;

fn main() {
    let d = time::now();
    println!("Today is {}/{}/{}", d.tm_mday, d.tm_mon, d.tm_year + 1900);

    let hour: i32 = d.tm_hour;
    let min: i32 = d.tm_min;
    let sec: i32 = d.tm_sec;

    println!("now it is {}h{}min{}s", hour, min, sec);

    /*
    Não podemos atribuir duas vezes!
    d = time::now();
    println!("Now it is {}", d.tm_hour);
    */
}
