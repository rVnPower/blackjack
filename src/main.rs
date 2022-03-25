use std::io::stdin;

struct Game {
   playersDeck: Deck,
   botsDeck: Deck,
   pile: Deck,
}

struct Card {
    index: u8
}

struct Deck {
   cards: Vec<Card>,
   points: u8,
   standed: bool,
   won: bool,
   busted: bool,
}

fn input() -> String {
    let mut inp = String::new();

    stdin().read_line(&mut inp).expect("Failed to read line");
    inp
}

fn main() {
   let i = input();
   println!("{i}");
}
