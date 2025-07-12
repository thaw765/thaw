<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8" />
    <title>로그 계산 연습 어플</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        #problem {
            font-size: 1.2em;
            margin-top: 20px;
            text-align: center;
        }
        #answer {
            width: 200px;
            padding: 8px;
            font-size: 1em;
            margin-top: 10px;
        }
        button {
            padding: 10px 20px;
            font-size: 1em;
            margin-top: 10px;
            cursor: pointer;
        }
        #result {
            margin-top: 20px;
            text-align: center;
            font-size: 1.2em;
        }
        #score {
            margin-top: 10px;
            text-align: center;
        }
    </style>
</head>
<body>

<h1>로그 계산 연습 어플</h1>

<div id="problem">문제가 여기 표시됩니다</div>

<input type="text" id="answer" placeholder="답을 입력하세요" />

<br />

<button onclick="submitAnswer()">답 제출</button>
<button onclick="nextProblem()">새 문제 생성</button>

<div id="result"></div>
<div id="score">점수: 0 / 0</div>

<script>
    const problems = [
        {problem: "log₂16 = ?", answer: 4},
        {problem: "log₃81 = ?", answer: 4},
        {problem: "log₁₀1000 = ?", answer: 3},
        {problem: "log₂8 = ?", answer: 3},
        {problem: "log₅25 = ?", answer: 2},
        {problem: "log₄16 = ?", answer: 2},
        {problem: "log₇49 = ?", answer: 2},
        {problem: "log₁₀1 = ?", answer: 0},
        {problem: "log₉81 = ?", answer: 2},
        {problem: "log₂1 = ?", answer: 0}
    ];

    let currentProblemIndex = 0;
    let score = 0;
    let total = 0;

    function showProblem() {
        document.getElementById('result').innerText = '';
        document.getElementById('answer').value = '';
        document.getElementById('answer').focus();
        document.getElementById('problem').innerText = problems[currentProblemIndex].problem;
    }

    function submitAnswer() {
        const userAnswer = parseFloat(document.getElementById('answer').value.trim());
        if (isNaN(userAnswer)) {
            alert('숫자를 입력하세요.');
            return;
        }

        total++;
        const correctAnswer = problems[currentProblemIndex].answer;
        if (Math.abs(userAnswer - correctAnswer) < 0.0001) {
            score++;
            document.getElementById('result').innerText = '정답입니다!';
        } else {
            document.getElementById('result').innerText = `틀렸어요! 정답은 ${correctAnswer}입니다.`;
        }
        document.getElementById('score').innerText = `점수: ${score} / ${total}`;
        nextProblem();
    }

    function nextProblem() {
        currentProblemIndex = Math.floor(Math.random() * problems.length);
        showProblem();
    }

    // 초기 문제 보여주기
    showProblem();
</script>

</body>
</html>
