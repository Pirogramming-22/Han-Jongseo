let attempts = 9; // 시도 가능 횟수

function generateRandomNumbers() {
    const numbers = [];
    while (numbers.length < 3) {
        const number = Math.floor(Math.random() * 10);
        if (!numbers.includes(number)) {
            numbers.push(number);
        }
    }
    return numbers;
}

let answer = generateRandomNumbers(); // 중복되지 않는 3개의 랜덤한 숫자 설정
let isGameOver = false; // 정답이거나 시도 가능 횟수가 0이 되면 true로 설정

function clearInputFields() { // 입력창 초기화 및 포커스 설정
    for (let i = 1; i <= 3; i++) {
        document.getElementById(`number${i}`).value = '';
    }
    document.getElementById('number1').focus();
}

function updateAttempts() { // 남은 시도 가능 횟수 업데이트
    document.getElementById('attempts').textContent = attempts;
}

function formatResult(numbers, strikes, balls) {
    const resultDiv = document.createElement('div');
    resultDiv.className = 'check-result';
    
    const leftDiv = document.createElement('div'); // 입력한 숫자들 표시
    leftDiv.className = 'left';
    leftDiv.textContent = numbers.join(' ') + '    :    ';
    
    const rightDiv = document.createElement('div'); // 결과 표시
    rightDiv.className = 'right';

    if (strikes === 0 && balls === 0) { // 아웃일 때
        const outSpan = document.createElement('span');
        outSpan.className = 'num-result out';
        outSpan.textContent = 'O';
        rightDiv.appendChild(outSpan);
    } else {
        if (strikes > 0) { // 스트라이크가 있을 때
            const strikeSpan = document.createElement('span');
            strikeSpan.className = 'num-result strike';
            strikeSpan.textContent = 'S';
            rightDiv.appendChild(document.createTextNode(strikes));
            rightDiv.appendChild(strikeSpan);
        }
        if (balls > 0) { // 볼이 있을 때
            const ballSpan = document.createElement('span');
            ballSpan.className = 'num-result ball';
            ballSpan.textContent = 'B';
            rightDiv.appendChild(document.createTextNode(balls));
            rightDiv.appendChild(ballSpan);
        }
    }
    
    resultDiv.appendChild(leftDiv);
    resultDiv.appendChild(rightDiv);

    return resultDiv;
}

function check_numbers() {
    const inputs = [
        document.getElementById('number1').value,
        document.getElementById('number2').value,
        document.getElementById('number3').value
    ];

    const numbers = inputs.map(Number);
    attempts--;

    updateAttempts();

    let strikes = 0;
    let balls = 0;

    for (let i = 0; i < 3; i++) {
        if (numbers[i] === answer[i]) {
            strikes++;
        } else if (answer.includes(numbers[i])) {
            balls++;
        }
    }

    const resultDiv = document.getElementById('results'); // 결과 화면에 표시
    resultDiv.appendChild(formatResult(numbers, strikes, balls));

    if (strikes === 3 || attempts === 0) {
        isGameOver = true;
        const resultImg = document.getElementById('game-result-img');
        resultImg.src = strikes === 3 ? 'success.png' : 'fail.png';
        document.querySelector('.submit-button').disabled = true;
    }
    
    clearInputFields();
}

for (let i = 1; i <= 2; i++) { // 입력 필드 자동 포커스 이동 설정
    document.getElementById(`number${i}`).addEventListener('input', function() {
        if (this.value) {
            document.getElementById(`number${i + 1}`).focus();
        }
    });
}

updateAttempts();
document.getElementById('game-result-img').src = '';
document.getElementById('results').innerHTML = '';