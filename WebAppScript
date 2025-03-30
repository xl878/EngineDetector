let port;
let reader;
let inputDone;
let inputStream;

const vibrationCtx = document.getElementById('vibrationChart').getContext('2d');
const fftCtx = document.getElementById('fftChart').getContext('2d');

const vibrationChart = new Chart(vibrationCtx, {
  type: 'line',
  data: { labels: [], datasets: [{ label: 'Vibration (Z)', data: [] }] },
  options: { responsive: false, animation: false }
});

const fftChart = new Chart(fftCtx, {
  type: 'line',
  data: { labels: [], datasets: [{ label: 'FFT Magnitude', data: [] }] },
  options: { responsive: false, animation: false }
});

async function connectSerial() {
  port = await navigator.serial.requestPort();
  await port.open({ baudRate: 115200 });
  inputStream = port.readable.getReader();
  readSerial();
}

async function readSerial() {
  let buffer = '';
  while (true) {
    const { value, done } = await inputStream.read();
    if (done) break;
    buffer += new TextDecoder().decode(value);
    let lines = buffer.split('\n');
    buffer = lines.pop();
    lines.forEach(processLine);
  }
}

function processLine(line) {
  if (!line.includes(',')) return;
  const parts = line.trim().split(',');
  if (parts.length < 3) return;
  const time = parseFloat(parts[0]);
  const amp = parseFloat(parts[1]);
  const freq = parseFloat(parts[2]);

  vibrationChart.data.labels.push(time);
  vibrationChart.data.datasets[0].data.push(amp);
  if (vibrationChart.data.labels.length > 100) {
    vibrationChart.data.labels.shift();
    vibrationChart.data.datasets[0].data.shift();
  }
  vibrationChart.update();

  fftChart.data.labels.push(time);
  fftChart.data.datasets[0].data.push(freq);
  if (fftChart.data.labels.length > 100) {
    fftChart.data.labels.shift();
    fftChart.data.datasets[0].data.shift();
  }
  fftChart.update();

  // Example live stats
  document.getElementById('liveStats').innerText = `RMS: ${amp.toFixed(3)}, FFT Peak: ${freq.toFixed(1)}, FFT Centroid: ---`;
}

function sendLabel() {
  const label = document.getElementById('labelInput').value;
  if (port && port.writable) {
    const writer = port.writable.getWriter();
    writer.write(new TextEncoder().encode(label + '\n'));
    writer.releaseLock();
  }
}

document.getElementById('connectBtn').addEventListener('click', connectSerial);
