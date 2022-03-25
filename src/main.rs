use std::io::stdin;

struct Game {
   playersDeck: Deck,
   botsDeck: Deck,
   pile: Deck,
}

#[derive(Debug)]
struct Card {
    suit: String,
    points: u8,
    index: String
}

impl Card {
    fn get_raw(&self) -> String {
        String::from(format!("{}{}", self.index, self.suit))
    }
}

#[derive(Debug)]
struct Deck {
   cards: Vec<Card>,
   points: u8,
   standed: bool,
   won: bool,
   busted: bool,
}

impl Deck {
    fn fill(&mut self){
        for number in 1..=13 {
            let card_index = &["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"][number-1].to_string();
            let card_points = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10][number-1];

            for suit in &["♠", "♦", "♣", "♥"] {
                let card = Card {
                    index: card_index.to_string(),
                    points: card_points,
                    suit: suit.to_string(),
                };
                self.cards.push(card);
            }
        }
    }
}

fn clear() {
    print!("\x1B[2J");
    print!("\x1B[0;0H");
}

fn input() -> String {
    let mut inp = String::new();
    stdin().read_line(&mut inp).expect("Failed to read line");
    inp
}

fn main() {
    let mut game = Game {
        playersDeck: Deck {
            cards: Vec::new(),
            points: 0,
            standed: false,
            won: false,
            busted: false,
        },
        botsDeck: Deck {
            cards: Vec::new(),
            points: 0,
            standed: false,
            won: false,
            busted: false,
        },
        pile: Deck {
            cards: Vec::new(),
            points: 0,
            standed: false,
            won: false,
            busted: false,
        },
    };

    let mut player = String::new();
    let mut bot = String::new();

    println!("Welcome to Blackjack!");
    println!("Please enter your name:");
    player = input();
    println!("Please enter the name of the bot:");
    bot = input();

    game.pile.fill();
    clear();
    // println!("{:#?}", game.pile.cards);
}
