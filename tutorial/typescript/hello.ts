//@ts-check
let a_number = 1000;

if (Math.random() < 0.5) {
    //a_number = "Hello, World!"    // not this wont be allowed
    a_number = 200;
}

console.log(a_number * 20);

/**
 * Adds VAT to a price
 *
 * @param {number} price The price without VAT
 * @param {number} vat The VAT [0-1]
 *
 * @returns {number}
 */
function addVAT(price, vat=0.2) {
    return price * ( 1 + vat);
}

/** @type {number} */
let amount;

amount = '12'; // this is incorrect

/**
 * @typedef {Object} Article
 * @property {number} price
 * @property {number} vat
 * @property {string} string
 * @property {boolean=} sold
 */

/**
 * Now we can use Article as a proper type
 * @param {[Article]} articles
 */
function totalAmount(articles) {
    return articles.reduce((total, article) => {
      return total + addVAT(article);
    }, 0);
  }