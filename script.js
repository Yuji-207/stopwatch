let stopTime = 0;
let count = false;
let intervalId;
let diff;
let scores = [];
let number = 0;
let sumScore = 0;
let sound_path = 'seatbelt_sign.wav';

function timeChange(ms) {
  hour = Math.floor(ms / 3600000)
  minute = Math.floor(ms % 3600000 / 60000)
  second = Math.floor(ms % 360000 % 60000 / 1000)
  hour = String(hour).padStart(2, '0');
  minute = String(minute).padStart(2, '0');
  second = String(second).padStart(2, '0');
  return hour + ':' + minute + ':' + second;
}

function playSound(path) {
  let audioElem = new Audio();
  audioElem.src = path;
  audioElem.play();
}

document.getElementById('start').onclick = () => {
  if (!count) {

    playSound(sound_path);

    let startTime = Date.now() - stopTime;
    count = true;

    intervalId = setInterval(() => {
      diff = Date.now() - startTime;
      document.getElementById('display').innerHTML = timeChange(diff);
    });
  }
};

document.getElementById('stop').onclick = () => {
  if (count) {
    playSound(sound_path);
    count = false;
    stopTime = diff;
    clearInterval(intervalId);


  }
};

document.getElementById('reset').onclick = () => {
  playSound(sound_path);
  count = false;
  stopTime = 0;
  scores = [];
  number = [];
  clearInterval(intervalId);
  document.getElementById('display').innerHTML = '00:00:00';
  document.getElementById('scores').innerHTML = '';
};

document.getElementById('correct').onclick = () => {  
  if (count) {
    playSound(sound_path);
    if (scores.length == 0) {
      document.getElementById('scores').insertAdjacentHTML('beforeend', `<tr id="tr-${number+1}"><td class="text-start" id="td-${number+1}"><i class="fas fa-check true "></i></td></tr>`);
    } else {
      document.getElementById(`td-${number+1}`).insertAdjacentHTML('beforeend', '<i class="fas fa-check true"></i>');
    }
    
    scores.push(true);

  }
};

document.getElementById('wrong').onclick = () => {
  if (count) {
    playSound(sound_path);
    if (scores.length == 0) {
      document.getElementById('scores').insertAdjacentHTML('beforeend', `<tr id="tr-${number+1}"><td class="text-start" id="td-${number+1}"><i class="fas fa-times false"></i></td></tr>`);
    } else {
      document.getElementById(`td-${number+1}`).insertAdjacentHTML('beforeend', '<i class="fas fa-times false"></i>');
    }

    scores.push(false);
  
  }
};

document.getElementById('next').onclick = () => {
  if (scores.length > 0) {
    playSound(sound_path);
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

    let trueNum = document.getElementsByClassName('true').length;
    let falseNum = document.getElementsByClassName('false').length;

    let displaySumScore = trueNum / (trueNum + falseNum) * 100;
    if (displaySumScore < 100) {
      displaySumScore = displaySumScore.toPrecision(2);
    }
    
    stringDisplaySumScore = String(displaySumScore) + ' %';
    stringMinute = String(minute) + ' m/q';

    document.getElementById(`tr-${number}`).insertAdjacentHTML('beforeend', `<td>${stringDisplaySumScore}</td><td>${stringMinute}</td>`);

  }
};
