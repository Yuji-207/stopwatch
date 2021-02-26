let stopTime = 0;
let count = false;
let intervalId;
let diff;

document.getElementById('start').onclick = () => {
  if (count == false) {

    let startTime = Date.now() - stopTime;
    count = true;

    intervalId = setInterval(() => {
      diff = Date.now() - startTime;
      document.querySelector('#display').innerHTML = Math.ceil(diff / 1000);
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
  clearInterval(intervalId);
  document.querySelector('#display').innerHTML = 0;
};
