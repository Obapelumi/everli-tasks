function reverseBinary (n) {
  // convert the number to a binary string and reverse the string
  const reverseBinary = n.toString(2).split('').reverse().join('')

  // convert binary string to a number using BigInt to accomodate huge binary numbers
  return BigInt(`0b${reverseBinary}`)
}

// test in a node environment - node reverse_binary.js
console.log(reverseBinary(59483))