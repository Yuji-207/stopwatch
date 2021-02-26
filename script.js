let stopTime = 0;
let count = false;
let intervalId;
let diff;
let scores = [];
let number = 0;
let sumScore = 0;

document.getElementById('start').onclick = () => {
  if (count == false) {

    let startTime = Date.now() - stopTime;
    count = true;

    intervalId = setInterval(() => {
      diff = Date.now() - startTime;
      document.getElementById('display').innerHTML = Math.ceil(diff / 1000);
    });

  }
};

document.getElementById('stop').onclick = () => {
  if (count == true) {
    count = false;
    stopTime = diff;
    clearInterval(intervalId);
  }
};

document.getElementById('reset').onclick = () => {
  count = false;
  stopTime = 0;
  scores = [];
  number = [];
  clearInterval(intervalId);
  document.getElementById('display').innerHTML = 0;
  document.getElementById('scores').innerHTML = '';
};

document.getElementById('correct').onclick = () => {
  if (count == true) {

    scores.push(true);
    document.getElementById('scores').insertAdjacentHTML('beforeend', '○');

  }
};

document.getElementById('incorrect').onclick = () => {
  if (count == true) {

    scores.push(false);
    document.getElementById('scores').insertAdjacentHTML('beforeend', '×');
  
  }
};

document.getElementById('next').onclick = () => {
  if (count == true) {

    let sum = scores.reduce(function(a, b){
      return a + b;
    });

    sumScore += sum;

    let score = sum / scores.length * 100;
    if (score < 100) {
      score = score.toPrecision(2);
    }

    scores = [];
    number++;

    let minute = diff / number / 60000;
    minute = minute.toPrecision(2);


    let displaySumScore = sumScore / number * 100;
    if (displaySumScore < 100) {
      displaySumScore = displaySumScore.toPrecision(2);
    }
    
    document.getElementById('scores').insertAdjacentHTML('beforeend', ' ' + String(score) + '%');
    document.getElementById('scores').insertAdjacentHTML('beforeend', ' ' + String(displaySumScore) + ' %');
    document.getElementById('scores').insertAdjacentHTML('beforeend', ' ' + String(minute) + ' m/q');
    document.getElementById('scores').insertAdjacentHTML('beforeend', '<br>');

  }
};