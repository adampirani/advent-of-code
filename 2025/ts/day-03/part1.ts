import * as fs from "fs";

const getMaxWithIndex = (array: number[]) => {
  let max = array[0];
  let index = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] === 9) {
      return { max: 9, index: i };
    }

    if (array[i] > max) {
      max = array[i];
      index = i;
    }
  }
  return { max, index };
};

const calcJoltage = (bank: string) => {
  const bankToArray = bank.split("").map(Number);

  const firstMaxIndex = getMaxWithIndex(bankToArray.slice(0, -1));
  const secondMaxIndex = getMaxWithIndex(
    bankToArray.slice(firstMaxIndex.index + 1)
  );

  return firstMaxIndex.max * 10 + secondMaxIndex.max;
};

console.log(calcJoltage("987654321111111"));
console.log(calcJoltage("811111111111119"));
console.log(calcJoltage("234234234234278"));
console.log(calcJoltage("818181911112111"));

const main = () => {
  const args = process.argv.slice();
  const filename = args.at(-1);
  const input = fs.readFileSync(filename!, "utf8");
  let total = 0;
  const lines = input.split("\n");

  for (const line of lines) {
    total += calcJoltage(line);
  }
  return total;
};

console.log(main());

// console.log(isInvalidId(11));
// console.log(isInvalidId(12));
// console.log(isInvalidId(1188511885));
