const gameForm = document.getElementById('game-form');
const guessInput = document.getElementById('guess');
const message = document.getElementById('message');
const hints = document.getElementById('hints');

let answer = Math.floor(Math.random() * 20) + 1;
let factors = [];

for (let i = 1; i < answer; i++) {
  if (answer % i === 0) {
    factors.push(i);
  }
}

if (answer === 5) {
  hints.innerHTML = `Hints:<br>I am associated with Boron`;
} else if (answer === 7) {
  hints.innerHTML = `Hints:<br>I am the jersey number of famous former Indian cricket team captain`;
} else if (answer === 13) {
  hints.innerHTML = `Hints:<br>Many people consider the number to be an unlucky number, and some buildings even skip the floor number because of this superstition.`;
} else if (answer === 17) {
  hints.innerHTML = `Hints:<br>The number is written as XVII.`;
} else if (answer === 19) {
  hints.innerHTML = `Hints:<br>The sum of the digits of the number is 10`;
} 
else if (answer === 11) {
  hints.innerHTML = `Hints:<br>The sum of the digits of the number is 2`;
}else {
  hints.innerHTML = `Hints:<br>
                      ${
                        answer > 9
                          ? 'Number of digits in the number is 2.<br>'
                          : 'The number is a single digit number.<br>'
                      }
                      ${
                        answer === 3
                          ? 'I am the beginning of pi.<br>'
                          : 'The factors of the number are:<br>' + factors.join(', ') + '<br>'
                      }`;
}

gameForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const guess = parseInt(guessInput.value);
  if (guess === answer) {
    message.textContent = 'You have guessed it correctly!!!';
  } else {
    message.textContent = 'Wrong, try again.';
  }
});

