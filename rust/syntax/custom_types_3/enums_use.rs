// An attribute to hide the warnins for unused code.
#![allow(dead_code)]

enum Status {
    Rich,
    Poor,
}

enum Work {
    Civilian,
    Soldier,
}

fn main() {
    // Explicity `use` each name so they are available wihtout
    // manual scoping
    use Status::{Poor, Rich};
    // Automotically `use` each name inside `Work`.
    use Work::*;

    // Equivalent to `Status::Poor`
    let status = Poor;
    // Equivalent to `Work::Civilian`
    let work = Civilian;

    match status {
        // Note the lack of scoping because of the explict `use` above.
        Rich => println!("The rich have lots of money!"),
        Poor => println!("The poor have no money..."),
    }
    
    match work {
        // Note again the lack of scoping
        Civilian => println!("Civilians  work!"),
        Soldier  => println!("Soldiers work!"),
    }
}
