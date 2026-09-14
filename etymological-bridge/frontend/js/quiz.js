// ==========================================================================
// Learn English via Thai Mnemonic Quiz System
// ==========================================================================

let quizQuestions = [];
let currentQuestionIndex = 0;
let userScore = 0;
let isAnswered = false;

async function initQuizSystem() {
  try {
    const res = await fetch("/api/quiz?count=5");
    if (res.ok) {
      quizQuestions = await res.json();
    } else {
      throw new Error("API failed");
    }
  } catch (err) {
    // Fallback offline quiz questions
    quizQuestions = [
      {
        thai_word: "ทันต",
        pali_sanskrit: "danta",
        pie_root: "*h₁dónts",
        question: "คำว่า 'ทันต' (ทันตแพทย์) ในภาษาไทย มีรากศัพท์ร่วม (Cognate) ผ่านตระกูล PIE เดียวกับคำศัพท์ภาษาอังกฤษใด?",
        options: ["dental", "hospital", "patient", "scalpel"],
        correct_answer: "dental",
        explanation: "ทันต (danta) และ dental/dentist/tooth รวมถึงดอกไม้ dandelion (dent de lion = ฟันสิงห์) ล้วนสืบสายมาจากราก PIE *h₁dónts (ฟัน)!",
        difficulty: "General (A2)"
      },
      {
        thai_word: "ศูนย์",
        pali_sanskrit: "śūnya",
        pie_root: "*ḱewH-",
        question: "คำว่า 'ศูนย์' (śūnya ความว่างเปล่า) เป็นรากที่เดินทางผ่านภาษาอาหรับ (sifr) สู่ภาษาอังกฤษเป็นคำว่าอะไร?",
        options: ["zero", "circle", "round", "null"],
        correct_answer: "zero",
        explanation: "คำว่า zero ในภาษาอังกฤษยืมผ่านคำว่า sifr ของอาหรับ ซึ่งแปลมาจากคำว่า ศูนย์ (śūnya) ของอินเดียโบราณโดยตรง!",
        difficulty: "General (A1)"
      },
      {
        thai_word: "วิทยา",
        pali_sanskrit: "vidyā",
        pie_root: "*weyd-",
        question: "คำว่า 'วิทยา' (ความรู้) มาจากราก PIE *weyd- (มองเห็น) ซึ่งตรงกับคำภาษาอังกฤษในชีวิตประจำวันคำใด?",
        options: ["video", "study", "book", "lecture"],
        correct_answer: "video",
        explanation: "คำว่า video (ฉันมองเห็น ในภาษาละติน) และ วิทยา/วิทย์ มาจากราก *weyd- เดียวกัน: เพราะการมองเห็นนำไปสู่ความรู้แจ้ง!",
        difficulty: "General (A1)"
      },
      {
        thai_word: "สุนัข",
        pali_sanskrit: "śunaka",
        pie_root: "*ḱwṓn",
        question: "คำว่า 'สุนัข' มีรากศัพท์ร่วมกับคำเรียกฟันเขี้ยวสัตว์และตระกูลสุนัขในภาษาอังกฤษคำใด?",
        options: ["canine", "feline", "bovine", "equine"],
        correct_answer: "canine",
        explanation: "canine (ตระกูลสุนัข/ฟันเขี้ยว) และ hound รวมถึงสำนักปรัชญา cynic ล้วนมาจากราก *ḱwṓn เดียวกับ สุนัข!",
        difficulty: "Intermediate (B2)"
      },
      {
        thai_word: "มนุษย์",
        pali_sanskrit: "manuṣya",
        pie_root: "*mon-",
        question: "คำว่า 'มนุษย์' มาจากรากที่มองว่ามนุษย์คือสิ่งมีชีวิตที่มีความคิด (มโน) ซึ่งตรงกับคำภาษาอังกฤษคำใด?",
        options: ["man", "person", "mortal", "creature"],
        correct_answer: "man",
        explanation: "มนุษย์ (manuṣya) ↔ man / mankind สันนิษฐานว่ามาจากรากที่แปลว่า 'สิ่งมีชีวิตผู้มีความคิด'!",
        difficulty: "General (A1)"
      }
    ];
  }

  currentQuestionIndex = 0;
  userScore = 0;
  renderCurrentQuestion();

  document.getElementById("quizNextBtn").onclick = handleNextQuestion;
  document.getElementById("restartQuizBtn").onclick = () => {
    initQuizSystem();
  };
}

function renderCurrentQuestion() {
  isAnswered = false;
  const q = quizQuestions[currentQuestionIndex];
  if (!q) return;

  document.getElementById("quizWrapper").style.display = "block";
  document.getElementById("quizCompleteCard").style.display = "none";
  document.getElementById("quizFeedbackBox").style.display = "none";

  document.getElementById("quizProgressLabel").innerText = `คำถามข้อที่ ${currentQuestionIndex + 1} / ${quizQuestions.length}`;
  document.getElementById("quizScoreText").innerText = userScore;
  document.getElementById("quizQuestionText").innerText = q.question;
  document.getElementById("quizSubHint").innerText = `รากศัพท์โบราณ: ${q.pie_root} • คำบาลี/สันสกฤต: ${q.pali_sanskrit}`;

  const grid = document.getElementById("quizOptionsGrid");
  grid.innerHTML = "";

  q.options.forEach(opt => {
    const btn = document.createElement("button");
    btn.className = "quiz-opt-btn";
    btn.innerText = opt;
    btn.onclick = () => handleAnswerSelect(opt, q, btn);
    grid.appendChild(btn);
  });
}

function handleAnswerSelect(selectedOption, questionObj, buttonEl) {
  if (isAnswered) return;
  isAnswered = true;

  const isCorrect = (selectedOption === questionObj.correct_answer);
  if (isCorrect) {
    userScore++;
    document.getElementById("quizScoreText").innerText = userScore;
    buttonEl.classList.add("correct");
    document.getElementById("feedbackStatus").innerText = "ยอดเยี่ยม! ถูกต้องตรงเผง 🎉";
    document.getElementById("feedbackStatus").style.color = "#34d399";
  } else {
    buttonEl.classList.add("wrong");
    document.getElementById("feedbackStatus").innerText = `ยังไม่ถูกต้อง คำตอบที่แท้จริงคือ "${questionObj.correct_answer}" 💡`;
    document.getElementById("feedbackStatus").style.color = "#f43f5e";

    // Highlight correct button
    const allBtns = document.querySelectorAll(".quiz-opt-btn");
    allBtns.forEach(b => {
      if (b.innerText === questionObj.correct_answer) {
        b.classList.add("correct");
      }
    });
  }

  document.getElementById("feedbackExplanation").innerText = questionObj.explanation;
  document.getElementById("quizFeedbackBox").style.display = "block";

  if (currentQuestionIndex === quizQuestions.length - 1) {
    document.getElementById("quizNextBtn").innerText = "ดูผลคะแนนรวม 🏆";
  } else {
    document.getElementById("quizNextBtn").innerText = "คำถามถัดไป ➔";
  }
}

function handleNextQuestion() {
  currentQuestionIndex++;
  if (currentQuestionIndex < quizQuestions.length) {
    renderCurrentQuestion();
  } else {
    showQuizCompletion();
  }
}

function showQuizCompletion() {
  document.getElementById("quizWrapper").style.display = "none";
  document.getElementById("quizCompleteCard").style.display = "block";
  document.getElementById("finalScore").innerText = userScore;

  const praise = document.getElementById("completePraise");
  if (userScore === quizQuestions.length) {
    praise.innerText = "สมบูรณ์แบบระดับปรมาจารย์ภาษาศาสตร์! คุณเข้าใจความเชื่อมโยงของภาษาไทยและอังกฤษอย่างถ่องแท้";
  } else if (userScore >= 3) {
    praise.innerText = "เก่งมาก! คุณมองเห็นมิติใหม่ของพจนานุกรมไทยที่เชื่อมโยงกับคำศัพท์ภาษาอังกฤษสากล";
  } else {
    praise.innerText = "ดีเยี่ยมที่ได้เรียนรู้! คำศัพท์หลายคำน่าประหลาดใจมากเมื่อรู้รากศัพท์ที่แท้จริง";
  }
}
