use std::io;

fn main() {
    // basic Hello world
    println!("Hello World!");

    // Hello world using a single variable
    let greeting = "Hello World!";
    println!("{}", greeting);

    let first_greeting = "Hello";
    let second_greeting = "World";
    println!("{} {}", first_greeting, second_greeting);

    let good_morning = "Bom dia,";
    let mut name = String::new();

    io::stdin().read_line(&mut name);
    println!("{} {}", good_morning, name);
}
