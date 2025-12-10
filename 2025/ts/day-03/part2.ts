import * as fs from "fs";

const getMaxWithIndex = (
  array: number[],
  startIndex: number,
  endIndex: number
) => {
  // console.log("get max with index", array);
  let max = -Infinity;
  let index = 0;
  for (let i = startIndex; i < endIndex; i++) {
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

  const joltSize = 12;

  const maxIndices: { max: number; index: number }[] = [];

  for (let i = joltSize - 1; i >= 0; i--) {
    // console.log(maxIndices.at(-1)?.index);
    const topElement = maxIndices.at(-1);
    const startIndex = topElement ? topElement.index + 1 : 0;
    const endIndex = bankToArray.length - i;

    // console.log({ startIndex, endIndex });
    const maxIndex = getMaxWithIndex(bankToArray, startIndex, endIndex);

    // console.log({ maxIndex });
    maxIndices.push(maxIndex);
  }

  let joltage = maxIndices[0].max;
  for (let i = 1; i < maxIndices.length; i++) {
    joltage = joltage * 10 + maxIndices[i].max;
  }
  return joltage;
};

// console.log(calcJoltage("987654321111111"));
// console.log(calcJoltage("811111111111119"));
// console.log(calcJoltage("234234234234278"));
// console.log(calcJoltage("818181911112111"));

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
