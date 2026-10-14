/**
 * Legends of the Zambezi - 3D Flipbook & Interactive Reader Engine
 */

(function () {
  'use strict';

  // State
  let stories = window.ZAMBEZI_STORIES || [];
  let currentSpread = 0;
  let totalSpreads = 10; // Spread 0 (Cover), 1-8 (Chapters), 9 (Colophon)
  let currentThemeIndex = 0;
  const THEMES = ['theme-parchment', 'theme-sepia', 'theme-night'];
  let currentFontSizeIndex = 1;
  const FONT_SIZES = ['0.95rem', '1.05rem', '1.18rem'];

  // Speech synthesis state
  let isSpeaking = false;
  let synth = window.speechSynthesis;
  let speechUtterance = null;

  // DOM Elements
  const leftPageContent = document.getElementById('left-page-content');
  const rightPageContent = document.getElementById('right-page-content');
  const leftPageNum = document.getElementById('left-page-number');
  const rightPageNum = document.getElementById('right-page-number');
  const leftRunningHead = document.getElementById('left-running-head');
  const rightRunningHead = document.getElementById('right-running-head');
  const currentChapterTitle = document.getElementById('current-chapter-title');
  const spreadIndicator = document.getElementById('spread-indicator');
  const progressPercent = document.getElementById('progress-percent');
  const pageScrubber = document.getElementById('page-scrubber');
  const btnPrev = document.getElementById('btn-prev');
  const btnNext = document.getElementById('btn-next');
  const btnToc = document.getElementById('btn-toc');
  const tocDrawer = document.getElementById('toc-drawer');
  const tocOverlay = document.getElementById('toc-overlay');
  const btnCloseToc = document.getElementById('btn-close-toc');
  const tocList = document.getElementById('toc-list');
  const btnTheme = document.getElementById('btn-theme');
  const btnFontSize = document.getElementById('btn-font-size');
  const btnAudio = document.getElementById('btn-audio');
  const ttsIconPlay = document.getElementById('tts-icon-play');
  const ttsIconStop = document.getElementById('tts-icon-stop');
  const ttsLabel = document.getElementById('tts-label');

  // Quiz Modal DOM
  const quizModal = document.getElementById('quiz-modal');
  const quizOverlay = document.getElementById('quiz-overlay');
  const btnCloseQuiz = document.getElementById('btn-close-quiz');
  const quizChapterTitle = document.getElementById('quiz-chapter-title');
  const quizBody = document.getElementById('quiz-body');

  // Audio: Synthesized Paper Rustle Sound (Web Audio API)
  let audioCtx = null;
  function playPageTurnSound() {
    try {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
      const bufferSize = audioCtx.sampleRate * 0.12;
      const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
      const output = buffer.getChannelData(0);
      for (let i = 0; i < bufferSize; i++) {
        output[i] = (Math.random() * 2 - 1) * Math.exp(-i / (audioCtx.sampleRate * 0.035));
      }
      const whiteNoise = audioCtx.createBufferSource();
      whiteNoise.buffer = buffer;
      const filter = audioCtx.createBiquadFilter();
      filter.type = 'bandpass';
      filter.frequency.setValueAtTime(1400, audioCtx.currentTime);
      filter.Q.setValueAtTime(2.5, audioCtx.currentTime);
      const gain = audioCtx.createGain();
      gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.12);
      whiteNoise.connect(filter);
      filter.connect(gain);
      gain.connect(audioCtx.destination);
      whiteNoise.start();
    } catch (e) {
      // Audio fallback silent
    }
  }

  // Populate Table of Contents
  function buildToc() {
    tocList.innerHTML = '';

    // Cover Entry
    const coverLi = document.createElement('li');
    coverLi.className = `toc-item ${currentSpread === 0 ? 'active' : ''}`;
    coverLi.innerHTML = `
      <img src="assets/illustrations/cover.jpg" class="toc-thumb" alt="Cover">
      <div class="toc-info">
        <span class="toc-ch-num">Prologue</span>
        <div class="toc-ch-title">Front Cover &amp; Introduction</div>
      </div>
    `;
    coverLi.addEventListener('click', () => {
      goToSpread(0);
      closeToc();
    });
    tocList.appendChild(coverLi);

    // Chapter Entries
    stories.forEach((story, idx) => {
      const spreadIdx = idx + 1;
      const li = document.createElement('li');
      li.className = `toc-item ${currentSpread === spreadIdx ? 'active' : ''}`;
      li.innerHTML = `
        <img src="${story.illustration}" class="toc-thumb" alt="${story.title}">
        <div class="toc-info">
          <span class="toc-ch-num">${story.chapterBadge}</span>
          <div class="toc-ch-title">${story.title}</div>
        </div>
      `;
      li.addEventListener('click', () => {
        goToSpread(spreadIdx);
        closeToc();
      });
      tocList.appendChild(li);
    });

    // Colophon Entry
    const colophonLi = document.createElement('li');
    colophonLi.className = `toc-item ${currentSpread === 9 ? 'active' : ''}`;
    colophonLi.innerHTML = `
      <div style="width: 60px; height: 40px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.08); border-radius: 4px; font-size: 1.2rem;">🏛️</div>
      <div class="toc-info">
        <span class="toc-ch-num">Epilogue</span>
        <div class="toc-ch-title">Cultural Heritage Acknowledgments</div>
      </div>
    `;
    colophonLi.addEventListener('click', () => {
      goToSpread(9);
      closeToc();
    });
    tocList.appendChild(colophonLi);
  }

  function renderSpread(spreadIdx) {
    stopNarration();

    // Clamp
    if (spreadIdx < 0) spreadIdx = 0;
    if (spreadIdx >= totalSpreads) spreadIdx = totalSpreads - 1;
    currentSpread = spreadIdx;

    // Update Scrubber & Indicators
    pageScrubber.value = currentSpread;
    spreadIndicator.textContent = `Spread ${currentSpread + 1} of ${totalSpreads}`;
    const pct = Math.round((currentSpread / (totalSpreads - 1)) * 100);
    progressPercent.textContent = `${pct}%`;

    btnPrev.disabled = currentSpread === 0;
    btnNext.disabled = currentSpread === totalSpreads - 1;

    // SPREAD 0: FRONT COVER & INTRO
    if (currentSpread === 0) {
      currentChapterTitle.textContent = 'Legends of the Zambezi: Introduction';
      leftRunningHead.textContent = 'African Heritage Series';
      rightRunningHead.textContent = 'Legends of the Zambezi';
      leftPageNum.textContent = 'i';
      rightPageNum.textContent = 'ii';

      leftPageContent.innerHTML = `
        <div style="padding: 10px 0;">
          <span class="page-badge">Volume I • Flagship Edition</span>
          <h2 class="story-heading" style="font-size: 1.6rem; margin-bottom: 8px;">Preserving Sacred Stories of Zambia</h2>
          <div style="width: 40px; height: 2px; background: var(--accent-gold); margin-bottom: 16px;"></div>
          
          <p class="story-p lead-p">For thousands of years, the riverbanks and savannas of Zambia have echoed with the voices of elders sitting beside evening campfires. Through storytelling, generations of children were taught courage, humility, and deep reverence for the sacred waters and wildlife around them.</p>
          
          <p class="story-p">This flagship volume brings together eight of the most celebrated folktales from the BaTonga, Leya, Chishinga, Aushi, and Kunda oral traditions. Each tale is brought vividly to life with authentic hand-drawn watercolor illustrations, cultural vocabulary, and comprehension challenges.</p>
          
          <div class="moral-card" style="margin-top: 18px;">
            <h4>How to Experience This Book</h4>
            <p>Read at your own leisure, listen to voice narration using the Read Aloud button, or download the EPUB edition for your Apple Books library.</p>
          </div>
          
          <div style="margin-top: 16px; text-align: center;">
            <button id="btn-start-reading" class="btn-open-quiz" style="width: 100%;">
              Open Chapter One &rarr;
            </button>
          </div>
        </div>
      `;

      rightPageContent.innerHTML = `
        <div class="cover-spread">
          <div class="cover-image-wrap">
            <img src="assets/illustrations/cover.jpg" alt="Legends of the Zambezi Front Cover">
          </div>
          <span class="page-badge" style="margin-top: 4px;">Illustrated Storybook</span>
          <h2 style="font-family: var(--font-display); font-size: 1.3rem; color: var(--accent-terracotta);">LEGENDS OF THE ZAMBEZI</h2>
          <p style="font-family: var(--font-serif); font-style: italic; color: var(--text-secondary); font-size: 0.95rem;">Spirits, Giants &amp; Sacred Waters</p>
        </div>
      `;

      const startBtn = document.getElementById('btn-start-reading');
      if (startBtn) {
        startBtn.addEventListener('click', () => goToSpread(1));
      }
      buildToc();
      return;
    }

    // SPREAD 9: COLOPHON & ROADMAP
    if (currentSpread === 9) {
      currentChapterTitle.textContent = 'Epilogue: Cultural Acknowledgments';
      leftRunningHead.textContent = 'Legends of the Zambezi';
      rightRunningHead.textContent = 'Epilogue & Acknowledgments';
      leftPageNum.textContent = '17';
      rightPageNum.textContent = '18';

      leftPageContent.innerHTML = `
        <div style="padding: 10px 0;">
          <span class="page-badge">Cultural Preservation</span>
          <h2 class="story-heading" style="font-size: 1.5rem; margin-bottom: 8px;">Living Oral Heritage</h2>
          <div style="width: 40px; height: 2px; background: var(--accent-gold); margin-bottom: 16px;"></div>
          
          <p class="story-p lead-p">The stories within this book belong to the living heritage of the Zambian people. We extend our deepest gratitude to the elders, custodians, and oral tradition bearers of Southern, Northern, Luapula, and Eastern provinces who have kept these fires burning.</p>
          
          <p class="story-p">Every hand-drawn illustration was painted with organic pigments and delicate pencil hatching to reflect the natural warmth of the African earth, waterways, and wildlife.</p>
          
          <div class="moral-card">
            <h4>Traditional Zambian Proverb</h4>
            <p>“Umulandu wa mano tawupwa.”<br><em>(A matter of wisdom never ends — true learning continues throughout life.)</em></p>
          </div>
        </div>
      `;

      rightPageContent.innerHTML = `
        <div style="padding: 10px 0;">
          <span class="page-badge">Upcoming Companion Volumes</span>
          <h3 class="story-heading" style="font-size: 1.35rem; margin-bottom: 12px;">The Zambian Folktale Series</h3>
          
          <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 20px;">
            <div style="padding: 10px; background: rgba(0,0,0,0.04); border-radius: 6px; border-left: 3px solid var(--accent-gold);">
              <strong style="color: var(--accent-terracotta);">Volume II: Tricksters &amp; Heroes</strong>
              <div style="font-size: 0.85rem; color: var(--text-secondary);">The Complete Adventures of Kalulu the Clever Hare.</div>
            </div>
            <div style="padding: 10px; background: rgba(0,0,0,0.04); border-radius: 6px; border-left: 3px solid var(--accent-gold);">
              <strong style="color: var(--accent-terracotta);">Volume III: Savanna Echoes</strong>
              <div style="font-size: 0.85rem; color: var(--text-secondary);">Animal Origins &amp; Why the Lion Roars.</div>
            </div>
            <div style="padding: 10px; background: rgba(0,0,0,0.04); border-radius: 6px; border-left: 3px solid var(--accent-gold);">
              <strong style="color: var(--accent-terracotta);">Volume IV: Children of the Plateau</strong>
              <div style="font-size: 0.85rem; color: var(--text-secondary);">Stories of Jelita, Mulenga &amp; Northwestern Province.</div>
            </div>
          </div>
          
          <div style="text-align: center; margin-top: 10px;">
            <a href="../Legends-of-the-Zambezi.epub" download class="btn-open-quiz" style="text-decoration: none;">
              Download EPUB Edition &darr;
            </a>
          </div>
        </div>
      `;
      buildToc();
      return;
    }

    // CHAPTER SPREADS: 1 to 8
    const storyIdx = currentSpread - 1;
    const story = stories[storyIdx];
    if (!story) return;

    currentChapterTitle.textContent = `${story.chapterBadge}: ${story.title}`;
    leftRunningHead.textContent = 'Legends of the Zambezi';
    rightRunningHead.textContent = story.title;

    const leftNum = (currentSpread * 2) - 1;
    const rightNum = currentSpread * 2;
    leftPageNum.textContent = String(leftNum);
    rightPageNum.textContent = String(rightNum);

    // Left Page: Chapter Header, Hand-drawn illustration, and opening narrative
    const p1 = story.paragraphs[0] || '';
    const p2 = story.paragraphs[1] || '';
    const p3 = story.paragraphs[2] || '';

    leftPageContent.innerHTML = `
      <div style="padding: 4px 0;">
        <span class="page-badge">${story.chapterBadge}</span>
        <h2 class="story-heading">${story.title}</h2>
        <p class="story-sub">${story.subtitle}</p>
        <p class="story-region">📍 ${story.region}</p>
        
        <div class="story-art-frame">
          <img src="${story.illustration}" alt="${story.title}">
        </div>
        <p class="art-caption">${story.illustrationCaption}</p>
        
        <p class="story-p lead-p">${p1}</p>
        <p class="story-p">${p2}</p>
      </div>
    `;

    // Right Page: Climax narrative, moral lesson, vocabulary, and interactive quiz button
    const p4 = story.paragraphs[3] || '';
    const p5 = story.paragraphs[4] || '';
    const p6 = story.paragraphs[5] || '';

    let vocabRows = '';
    (story.vocabulary || []).forEach(v => {
      vocabRows += `
        <div class="vocab-row">
          <span class="vocab-term">${v.word}:</span> ${v.definition}
        </div>
      `;
    });

    rightPageContent.innerHTML = `
      <div style="padding: 4px 0;">
        <p class="story-p">${p3}</p>
        <p class="story-p">${p4}</p>
        <p class="story-p">${p5}</p>
        <p class="story-p">${p6}</p>
        
        <div class="moral-card">
          <h4>Ancestral Moral Lesson</h4>
          <p>“${story.moral}”</p>
        </div>
        
        <div class="vocab-section">
          <h4>📖 Cultural Vocabulary</h4>
          <div class="vocab-grid">
            ${vocabRows}
          </div>
        </div>
        
        <button id="btn-chapter-quiz" class="btn-open-quiz">
          ❓ Take Chapter Wonder Quiz (${story.questions.length} Questions)
        </button>
      </div>
    `;

    // Wire Quiz Button
    const quizBtn = document.getElementById('btn-chapter-quiz');
    if (quizBtn) {
      quizBtn.addEventListener('click', () => openQuiz(story));
    }

    buildToc();
  }

  function goToSpread(idx) {
    if (idx === currentSpread) return;
    playPageTurnSound();
    renderSpread(idx);
  }

  // Quiz Modal Logic
  function openQuiz(story) {
    quizChapterTitle.textContent = `${story.title} — Comprehension Quiz`;
    quizBody.innerHTML = '';

    story.questions.forEach((q, qIndex) => {
      const card = document.createElement('div');
      card.className = 'quiz-card';

      let optionsHtml = '';
      q.options.forEach((opt, optIndex) => {
        optionsHtml += `
          <button class="quiz-option-btn" data-qindex="${qIndex}" data-optindex="${optIndex}">
            ${chr(optIndex)}. ${opt}
          </button>
        `;
      });

      card.innerHTML = `
        <div class="quiz-q-title">${qIndex + 1}. ${q.question}</div>
        <div class="quiz-options">${optionsHtml}</div>
        <div class="quiz-feedback" id="feedback-${qIndex}"></div>
      `;
      quizBody.appendChild(card);
    });

    // Wire option clicks
    const optionBtns = quizBody.querySelectorAll('.quiz-option-btn');
    optionBtns.forEach(btn => {
      btn.addEventListener('click', function () {
        const qIdx = parseInt(this.getAttribute('data-qindex'), 10);
        const chosenIdx = parseInt(this.getAttribute('data-optindex'), 10);
        const question = story.questions[qIdx];
        const feedbackEl = document.getElementById(`feedback-${qIdx}`);

        // Disable all buttons for this question
        const siblingBtns = quizBody.querySelectorAll(`.quiz-option-btn[data-qindex="${qIdx}"]`);
        siblingBtns.forEach(b => b.disabled = true);

        if (chosenIdx === question.answer) {
          this.classList.add('correct');
          feedbackEl.className = 'quiz-feedback show';
          feedbackEl.style.background = 'rgba(76, 175, 80, 0.2)';
          feedbackEl.style.border = '1px solid #4caf50';
          feedbackEl.style.color = '#a5d6a7';
          feedbackEl.innerHTML = `<strong>✨ Correct!</strong> ${question.explanation}`;
        } else {
          this.classList.add('incorrect');
          siblingBtns[question.answer].classList.add('correct');
          feedbackEl.className = 'quiz-feedback show';
          feedbackEl.style.background = 'rgba(239, 83, 80, 0.2)';
          feedbackEl.style.border = '1px solid #ef5350';
          feedbackEl.style.color = '#ef9a9a';
          feedbackEl.innerHTML = `<strong>Not quite.</strong> ${question.explanation}`;
        }
      });
    });

    quizModal.classList.remove('hidden');
  }

  function closeQuiz() {
    quizModal.classList.add('hidden');
  }

  function chr(num) {
    return String.fromCharCode(65 + num);
  }

  // Text-To-Speech (Read Aloud)
  function toggleNarration() {
    if (isSpeaking) {
      stopNarration();
    } else {
      startNarration();
    }
  }

  function startNarration() {
    if (!synth) {
      alert('Speech synthesis is not supported in this browser.');
      return;
    }
    stopNarration();

    // Extract text from visible pages
    let textToRead = '';
    if (currentSpread === 0) {
      textToRead = leftPageContent.innerText;
    } else if (currentSpread === 9) {
      textToRead = leftPageContent.innerText + ' ' + rightPageContent.innerText;
    } else {
      const story = stories[currentSpread - 1];
      if (story) {
        textToRead = `${story.title}. ${story.subtitle}. ` + story.paragraphs.join(' ') + ` Ancestral Moral Lesson: ${story.moral}`;
      }
    }

    if (!textToRead.trim()) return;

    speechUtterance = new SpeechSynthesisUtterance(textToRead);
    speechUtterance.rate = 0.95;
    speechUtterance.pitch = 1.0;

    // Pick warm English voice if available
    const voices = synth.getVoices();
    const englishVoice = voices.find(v => v.lang.startsWith('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha')));
    if (englishVoice) speechUtterance.voice = englishVoice;

    speechUtterance.onstart = () => {
      isSpeaking = true;
      ttsIconPlay.classList.add('hidden');
      ttsIconStop.classList.remove('hidden');
      ttsLabel.textContent = 'Pause';
    };

    speechUtterance.onend = () => {
      stopNarration();
    };

    speechUtterance.onerror = () => {
      stopNarration();
    };

    synth.speak(speechUtterance);
  }

  function stopNarration() {
    if (synth && synth.speaking) {
      synth.cancel();
    }
    isSpeaking = false;
    ttsIconPlay.classList.remove('hidden');
    ttsIconStop.classList.add('hidden');
    ttsLabel.textContent = 'Read Aloud';
  }

  // Theme & Font Toggles
  function toggleTheme() {
    document.body.classList.remove(...THEMES);
    currentThemeIndex = (currentThemeIndex + 1) % THEMES.length;
    document.body.classList.add(THEMES[currentThemeIndex]);
  }

  function toggleFontSize() {
    currentFontSizeIndex = (currentFontSizeIndex + 1) % FONT_SIZES.length;
    document.documentElement.style.setProperty('--reading-font-size', FONT_SIZES[currentFontSizeIndex]);
  }

  // TOC Drawer handlers
  function openToc() {
    tocDrawer.classList.remove('hidden');
  }

  function closeToc() {
    tocDrawer.classList.add('hidden');
  }

  // Event Listeners
  btnPrev.addEventListener('click', () => goToSpread(currentSpread - 1));
  btnNext.addEventListener('click', () => goToSpread(currentSpread + 1));
  pageScrubber.addEventListener('input', (e) => goToSpread(parseInt(e.target.value, 10)));

  btnToc.addEventListener('click', openToc);
  btnCloseToc.addEventListener('click', closeToc);
  tocOverlay.addEventListener('click', closeToc);

  btnCloseQuiz.addEventListener('click', closeQuiz);
  quizOverlay.addEventListener('click', closeQuiz);

  btnTheme.addEventListener('click', toggleTheme);
  btnFontSize.addEventListener('click', toggleFontSize);
  btnAudio.addEventListener('click', toggleNarration);

  // Keyboard navigation
  window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') {
      goToSpread(currentSpread - 1);
    } else if (e.key === 'ArrowRight') {
      goToSpread(currentSpread + 1);
    } else if (e.key === 'Home') {
      goToSpread(0);
    } else if (e.key === 'End') {
      goToSpread(totalSpreads - 1);
    } else if (e.key === 't' || e.key === 'T') {
      if (tocDrawer.classList.contains('hidden')) openToc();
      else closeToc();
    } else if (e.key === 'r' || e.key === 'R') {
      toggleNarration();
    } else if (e.key === 'Escape') {
      closeToc();
      closeQuiz();
    }
  });

  // Touch Swipe Support for Mobile / Tablets
  let touchStartX = 0;
  let touchEndX = 0;
  const bookContainer = document.getElementById('book-container');

  bookContainer.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });

  bookContainer.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
  }, { passive: true });

  function handleSwipe() {
    const diff = touchEndX - touchStartX;
    if (Math.abs(diff) > 50) {
      if (diff < 0) {
        goToSpread(currentSpread + 1); // Swipe left = next
      } else {
        goToSpread(currentSpread - 1); // Swipe right = prev
      }
    }
  }

  // Initialize
  renderSpread(0);
})();
