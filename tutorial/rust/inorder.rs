use std::rc::Rc;
use std::cell::RefCell;

struct Node {
    val: i32,
    left: Option<Rc<RefCell<Node>>>,
    right: Option<Rc<RefCell<Node>>>,
}

fn inorder(node: &Option<Rc<RefCell<Node>>>) {
    if let Some(n) = node {
        inorder(&n.borrow().left);
        println!("{}", n.borrow().val);
        inorder(&n.borrow().right);
    }
}

fn main() {
    let leaf1 = Rc::new(RefCell::new(Node {
        val: 3,
        left: None,
        right: None,
    }));

    let leaf2 = Rc::new(RefCell::new(Node {
        val: 2,
        left: None,
        right: None,
    }));

    let root = Rc::new(RefCell::new(Node {
        val: 1,
        left: Some(Rc::clone(&leaf1)), 
        right: Some(Rc::clone(&leaf2)),
    }));

    inorder(&Some(Rc::clone(&root)));
}