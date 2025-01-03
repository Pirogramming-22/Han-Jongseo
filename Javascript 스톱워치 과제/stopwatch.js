// DOM 요소들
const timeSection = document.getElementById("time_section");
const startButton = document.getElementById("start_button");
const stopButton = document.getElementById("stop_button");
const resetButton = document.getElementById("reset_button");
const checkBox = document.getElementById("checkbox_all");
const deleteButton = document.getElementById("delete_button");
const main = document.getElementById("main");

let stopwatch;
let milliSeconds = 0; // 0.01초 단위
let isRunning = false; // 타이머 실행 플래그

// 시간 표시 함수 (00:00 형식으로 표시)
function showTime() {
  const seconds = Math.floor(milliSeconds / 100); // 100ms = 1초
  const hundredSec = (milliSeconds % 100).toString().padStart(2, "0"); // 0.01초 부분
  const second = seconds.toString().padStart(2, "0"); // 초를 두 자릿수로 설정
  
  timeSection.textContent = `${second}:${hundredSec}`; // 시간 표시
}

// 스톱워치 시작 함수
function startStopwatch() {
  if (isRunning) return; // 실행 중 START 버튼 무시
  
  isRunning = true;
  
  stopwatch = setInterval(() => {
    milliSeconds++; // 0.01초 단위로 증가
    showTime();
  }, 10); // 0.01초마다 표시
}

startButton.addEventListener("click", startStopwatch);

let records = [];

// 스톱워치 정지 함수
function stopStopwatch() {
  if (!isRunning) return; // 실행 중이지 않을 때 STOP 버튼 무시
  
  isRunning = false;
  
  clearInterval(stopwatch); // 스톱워치 정지

  const currentTime = timeSection.textContent;
  records.push(currentTime); // 현재 시간 기록
  displayRecords(); // 기록을 화면에 표시
}

stopButton.addEventListener("click", stopStopwatch);

// 구간 기록 표시 함수
function displayRecords() {
  const lastRecord = records[records.length - 1]; // 마지막으로 추가된 기록 가져오기

  const recordDiv = document.createElement("div");
  recordDiv.id = "record_section";

  const recordCheckbox = document.createElement("input");
  recordCheckbox.id = "checkbox";
  recordCheckbox.type = "checkbox";

  const recordTime = document.createElement("h2");
  recordTime.textContent = lastRecord;

  const deleteButton = document.createElement("button");
  deleteButton.id = "delete_button";
  deleteButton.innerHTML = `<img src="./delete-bin-line.svg" alt="삭제">`;

  recordDiv.appendChild(recordCheckbox);
  recordDiv.appendChild(recordTime);
  recordDiv.appendChild(deleteButton);

  main.appendChild(recordDiv);
}

// 스톱워치 초기화 함수
function resetStopwatch() {
  isRunning = false;

  clearInterval(stopwatch); // 스톱워치 정지

  milliSeconds = 0;
  records = [];
  showTime();
}

resetButton.addEventListener("click", resetStopwatch);

// 기록 삭제 함수
function deleteRecord() {
  const recordSections = document.querySelectorAll("#record_section"); // 모든 record_section 가져오기

  recordSections.forEach((recordDiv) => {
    const recordCheckbox = recordDiv.querySelector("input[type='checkbox']");
    if (recordCheckbox.checked) { // 체크박스가 선택되어 있으면
      recordDiv.remove(); // 해당 기록 삭제
    }
  });
}

deleteButton.addEventListener("click", deleteRecord);

// 전체 기록 선택 함수
function selectAll() {
  const recordSections = document.querySelectorAll("#record_section"); // 모든 record_section 가져오기
  const checkBox = document.getElementById("checkbox_all");

  recordSections.forEach((recordDiv) => {
    const recordCheckbox = recordDiv.querySelector("input[type='checkbox']");
    recordCheckbox.checked = checkBox.checked; // checkBox 상태를 모든 체크박스에 적용
  });
}

checkBox.addEventListener("click", selectAll);