/**
 * @file
 * This is a naive implementation of a selection sort in JS.
 * Always favor using native Array.prototype.sort, it'll be faster.
 */

/**
 * @typedef { -1 | 0 | 1 } Ord
 */

/**
 * Compare two numbers by precedence order
 * @param { number } numberA
 * @param { number } numberB
 * @returns { Ord }
 */
function numberOrd (numberA, numberB) {
  if (numberA > numberB) {
    return 1
  } else {
    return -1
  }
}

/**
 *
 * @param {T[]} array
 * @param {(a: T, b: T) => Ord} compare
 * @param { T[] } [acc=[]]
 * @template T
 */
function sort (array, compare = numberOrd, acc = []) {
  array = [].concat(array)
  if (array.length === 0) {
    return acc
  } else {
    let minimalIndex = 0
    for (let i = 1; i < array.length; i++) {
      if (compare(array[minimalIndex], array[i]) > 0) {
        minimalIndex = i
      }
    }
    acc = acc.concat([array[minimalIndex]])
    array.splice(minimalIndex, 1)
    return sort(array, compare, acc)
  }
}
